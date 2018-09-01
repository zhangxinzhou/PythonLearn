class TVshow:
    def __init__(self, show):
        self.__show = show

    @property
    def show(self):
        return self.__show


tvshow = TVshow("正在播放<战狼>")
print("默认:", tvshow.show)

tvshow.show = "正在播放<123>"
print("修改后:", tvshow.show)
