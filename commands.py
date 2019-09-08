from help import Help


class Commands:
    def __init__(self, store_info):
        self.commands = {
            "help": Help
        }

    def exec(self, cmd, *args):
        self.commands[cmd].exec(*args)
