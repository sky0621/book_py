import json

from command import Command
from store_info import StoreInfo


class Get(Command):
    def __init__(self, store_info: StoreInfo):
        self.store_info = store_info

    def exec(self, args):
        if len(args) != 1:
            print("not valid")
            return

        with open(self.store_info.get_name(), 'r') as fr:
            json_data = json.load(fr)
            if args[0] in json_data:
                print(json_data[args[0]])
