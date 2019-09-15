import json

from command import Command
from store_info import StoreInfo


class Save(Command):
    def __init__(self, store_info: StoreInfo):
        self.store_info = store_info

    def exec(self, args):
        if len(args) != 2:
            print("not valid")
            return

        with open(self.store_info.get_name(), 'r') as fr:
            json_data = json.load(fr)
            json_data[args[0]] = args[1]
            with open(self.store_info.get_name(), 'w') as fw:
                json.dump(json_data, fw)
