import json

from command import Command


class List(Command):
    def exec(self, args):
        with open(self.store_info.get_name(), 'r') as fr:
            json_data = json.load(fr)
            print('"key","value"')
            for k, v in json_data.items():
                print(f'"{k}","{v}"')
        return True
