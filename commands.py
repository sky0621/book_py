import os

from store_info import StoreInfo
from end import End
from help import Help
from clear import Clear
from save import Save
from get import Get
from remove import Remove
from list import List


class Commands:
    def __init__(self, store_info: StoreInfo):
        self.commands = {
            "end": End(store_info),
            "help": Help(store_info),
            "clear": Clear(store_info),
            "save": Save(store_info),
            "get": Get(store_info),
            "remove": Remove(store_info),
            "list": List(store_info),
        }
        if not os.path.isfile(store_info.get_name()):
            self.commands.get("clear").exec(self)

    def exec(self, cmds):
        if len(cmds) < 1:
            print("no target")
            return

        c = self.commands.get(cmds[0])
        if c is None:
            print("no target")
            return

        if len(cmds) == 1:
            c.exec([])
            return
        else:
            c.exec(cmds[1:])
