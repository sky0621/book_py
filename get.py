import json

from command import Command


class Get(Command):
    def exec(self, args):
        if len(args) != 1:
            print("not valid")
            return

        with open(self.store_info.get_name(), 'r') as fr:
            json_data = json.load(fr)
            if args[0] in json_data:
                print(json_data[args[0]])
