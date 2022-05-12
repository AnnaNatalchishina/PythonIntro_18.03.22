import json
from random import uniform
from argparse import ArgumentParser


class WorkWithData:
    def __init__(self, config, trader_status, args):
        self.config = config
        self.trader_status = trader_status
        self.data_config = self.read_config_file()
        self.data_trader_status = self.read_trader_status_file()
        self.args = args

    def read_config_file(self):
        with open(self.config, 'r') as file:
            data_config = json.load(file)
        return data_config

    def read_trader_status_file(self):
        with open(self.trader_status, 'r') as file:
            data_trader_status = json.load(file)
            if data_trader_status == {}:
                data_trader_status = self.data_config

        return data_trader_status

    def write_trader_status_file(self) -> None:
        with open(self.trader_status, 'w') as file:
            json.dump(self.data_trader_status, file)

    def get_new_course(self):
        delta = uniform(-0.5, 0.5)
        self.data_trader_status['course'] = round(float(self.data_trader_status['course']) + delta, 2)

    def buy_money(self):
        amount_uah = float(self.data_trader_status['amount_uah'])
        amount_usd = float(self.data_trader_status['amount_usd'])
        course = self.data_trader_status['course']
        if self.args['operation_name'] == 'BUY' and self.args['money'] != 'ALL':
            if float(self.args['money']) * self.data_trader_status['course'] <= amount_uah:
                self.data_trader_status['amount_uah'] = amount_uah - float(self.args['money']) * course
                self.data_trader_status['amount_usd'] = amount_usd + float(self.args['money'])
            else:
                self.get_balance()
        elif self.args['operation_name'] == 'BUY' and self.args['money'] == 'ALL':
            residual = divmod(float(self.data_trader_status['amount_uah']), course)
            self.data_trader_status['amount_uah'] = round(residual[1], 2)
            self.data_trader_status['amount_usd'] = amount_usd + residual[0]

    def sell_money(self):
        amount_uah = float(self.data_trader_status['amount_uah'])
        amount_usd = float(self.data_trader_status['amount_usd'])
        course = self.data_trader_status['course']
        if self.args['operation_name'] == 'SELL' and self.args['money'] != 'ALL':
            if float(self.args['money']) <= amount_usd:
                self.data_trader_status['amount_uah'] = amount_uah + float(self.args['money']) * course
                self.data_trader_status['amount_usd'] = amount_usd - float(self.args['money'])
            else:
                self.get_balance()
        elif self.args['operation_name'] == 'SELL' and self.args['money'] == 'ALL':
            self.data_trader_status['amount_uah'] = amount_uah + amount_usd * course
            self.data_trader_status['amount_usd'] = 0.0

    def get_balance(self):
        print(f"UNAVAILABLE, REQUIRED BALANCE USD {float(self.args['money'])},"
              f"\nAVAILABLE {float(self.data_trader_status['amount_usd'])}")

    def restart_trader(self):
        self.data_trader_status.clear()

    def change_operation(self):
        if self.args['operation_name'] == 'RATE':
            print(self.data_trader_status['course'])
        elif self.args['operation_name'] == 'AVAILABLE':
            print(
                f"Account UAH: {self.data_trader_status['amount_uah']}"
                f"\nAccount USD: {self.data_trader_status['amount_usd']}")
        elif self.args['operation_name'] == 'BUY':
            self.buy_money()
        elif self.args['operation_name'] == 'SELL':
            self.sell_money()
        elif self.args['operation_name'] == 'NEXT':
            self.get_new_course()
        elif self.args['operation_name'] == 'RESTART':
            self.restart_trader()


config = 'config.json'
trader_status = 'trader_status.json'

args = ArgumentParser()
args.add_argument('operation_name')
args.add_argument('money', nargs='?', default=0)
args = vars(args.parse_args())

data_worker = WorkWithData(config, trader_status, args)
data_worker.change_operation()
data_worker.write_trader_status_file()
