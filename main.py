from store_info import StoreInfo
from commands import Commands

commands = Commands(StoreInfo("store.json"))


cmd_store = {}

print("Start!")
while True:
    commands.exec(input().split())
