from commands import Commands
from store_info import StoreInfo


def main():
    commands = Commands(StoreInfo("store.json"))

    print("Start!")

    running = True
    while running:
        running = commands.exec(input().split())


if __name__ == '__main__':
    main()
