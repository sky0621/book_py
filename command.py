# Ruby同様、Pythonも言語仕様にinterfaceを持たないのでclassで定義
# このクラスをそのまま使うことは想定していないため、デフォルトの処理をエラースローしておく


class Command:
    def exec(self, *args):
        raise NotImplementedError
