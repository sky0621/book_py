from command import Command
from store_info import StoreInfo


class Help(Command):
    def __init__(self, store_info: StoreInfo):
        self.store_info = store_info

    def exec(self, args):
        msg = """
        [usage]
        キーバリュー形式で文字列情報を管理するコマンドです。
        以下のサブコマンドが利用可能です。

        list   ... 保存済みの内容を一覧表示します。
        save   ... keyとvalueを渡して保存します。
        get    ... keyを渡してvalueを表示します。
        remove ... keyを渡してvalueを削除します。
        clear  ... 保存済みの内容を初期化します。
        help   ... ヘルプ情報（当内容と同じ）を表示します。

        """
        print(msg)
