import os

from store_info import StoreInfo
from end import End
from help import Help
from clear import Clear
from save import Save


class Commands:
    def __init__(self, store_info: StoreInfo):
        self.commands = {
            "end": End,
            "help": Help,
            "clear": Clear(store_info),
            "save": Save(store_info),
        }
        if not os.path.isfile(store_info.get_name()):
            self.commands.get("clear").exec(self)

    def exec(self, cmd, args):
        c = self.commands.get(cmd)
        if c is None:
            print("no target")
            return
        c.exec(args)
