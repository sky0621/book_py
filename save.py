import json

from command import Command


class Save(Command):
    def exec(self, args):
        if len(args) != 2:
            print("not valid")
            return

        with open(self.store_info.get_name(), 'r') as fr:
            json_data = json.load(fr)
            json_data[args[0]] = args[1]
            with open(self.store_info.get_name(), 'w') as fw:
                json.dump(json_data, fw)
