import json

from command import Command


class Clear(Command):
    def exec(self, args):
        with open(self.store_info.get_name(), 'w') as f:
            json.dump({}, f, ensure_ascii=False)
