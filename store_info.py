# Pythonには定数はない。ただ、全て大文字の変数を定数と扱うのが暗黙のルールとなっているらしい。
DEFAULT_STORE_NAME = "store.json"


class StoreInfo:
    # オブジェクト生成時に自動で呼ばれるメソッド（コンストラクタ扱い）
    # デフォルト引数が指定できる
    # インスタンス変数privateにする方法は無いが慣習的に「_」で始まる変数はprivate扱いとする
    def __init__(self, _store_name=DEFAULT_STORE_NAME):
        self._store_name = _store_name

    def get_name(self):
        return self._store_name
