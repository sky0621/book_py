from store_info import StoreInfo
from commands import Commands

commands = Commands(StoreInfo("store.json"))


cmd_store = {}

print("Start!")
while True:
    cmd = input()

    # 以降は、引数ありコマンドの処理
    cmds = cmd.split()
    if len(cmds) < 1:
        continue

    if cmds[0] == "end" or cmds[0] == "help" or cmds[0] == "save" or cmds[0] == "clear":
        commands.exec(cmds[0], cmds[1:])
        continue

    # 取得
    if cmds[0] == "get":
        if len(cmds) != 2:
            continue
        print(cmd_store[cmds[1]])

    # 削除
    if cmds[0] == "remove":
        if len(cmds) != 2:
            continue
        del cmd_store[cmds[1]]

    # 一覧
    if cmds[0] == "list":
        print('"key","value"')
        for k, v in cmd_store.items():
            print(f'"{k}","{v}"')
