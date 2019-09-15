from command import Command
from store_info import StoreInfo


class End(Command):
    def __init__(self, store_info: StoreInfo):
        self.store_info = store_info

    def exec(self, args):
        print("End!")
        exit()
