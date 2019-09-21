# Ruby同様、Pythonも言語仕様にinterfaceを持たないのでclassで定義
# このクラスをそのまま使うことは想定していないため、デフォルトの処理としてエラースローしておく
from store_info import StoreInfo


class Command:
    def __init__(self, store_info: StoreInfo):
        self.store_info = store_info

    def exec(self, args):
        raise NotImplementedError
