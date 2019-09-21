import json

from command import Command


class Remove(Command):
    def exec(self, args):
        if len(args) != 1:
            print("not valid")
            return True

        with open(self.store_info.get_name(), 'r') as fr:
            json_data = json.load(fr)
            if args[0] in json_data:
                del json_data[args[0]]
                with open(self.store_info.get_name(), 'w') as fw:
                    json.dump(json_data, fw)
        return True
