import json

from command import Command
from store_info import StoreInfo


class Clear(Command):
    def __init__(self, store_info: StoreInfo):
        self.store_info = store_info

    def exec(self, args):
        with open(self.store_info.get_name(), 'w') as f:
            json.dump({}, f, ensure_ascii=False)
