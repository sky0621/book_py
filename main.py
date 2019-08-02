def usage():
    msg = """
[usage]
キーバリュー形式で文字列情報を管理するコマンドです。
以下のサブコマンドが利用可能です。

list   ... 保存済みの内容を一覧表示します。
save   ... keyとvalueを渡して保存します。
get    ... keyを渡してvalueを表示します。
remove ... keyを渡してvalueを削除します。
help   ... ヘルプ情報（当内容と同じ）を表示します。

"""
    print(msg)


# -------------------------------------------------------------------
# ここからメイン処理
# -------------------------------------------------------------------

cmd_store = {}

print("Start!")
while True:
    cmd = input()

    # アプリ終了判定
    if cmd == "end":
        print("End!")
        exit()

    # ヘルプ
    if cmd == "help":
        usage()
        continue

    # 以降は、引数ありコマンドの処理
    cmds = cmd.split()
    if len(cmds) < 1:
        usage()
        continue

    # 保存
    if cmds[0] == "save":
        if len(cmds) != 3:
            usage()
            continue
        cmd_store[cmds[1]] = cmds[2]

    # 取得
    if cmds[0] == "get":
        if len(cmds) != 2:
            usage()
            continue
        print(cmd_store[cmds[1]])

    # 削除
    if cmds[0] == "remove":
        if len(cmds) != 2:
            usage()
            continue
        del cmd_store[cmds[1]]

    # 一覧
    if cmds[0] == "list":
        print('"key","value"')
        for k, v in cmd_store.items():
            print(f'"{k}","{v}"')
