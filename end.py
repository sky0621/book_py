from command import Command


class End(Command):
    def exec(self, args):
        print("End!")
        exit()
