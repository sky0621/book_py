import json

from command import Command
from store_info import StoreInfo


class List(Command):
    def __init__(self, store_info: StoreInfo):
        self.store_info = store_info

    def exec(self, args):
        with open(self.store_info.get_name(), 'r') as fr:
            json_data = json.load(fr)
            print('"key","value"')
            for k, v in json_data.items():
                print(f'"{k}","{v}"')
