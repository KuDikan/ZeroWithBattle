from settings import Settings
from player import Player


class State:
    """"""

    def __init__(self):
        """"""
        self.__p1__ = Player()
        self.__p2__ = Player()
        self.player = [self.__p1__, self.__p2__]
        pass
