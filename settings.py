class Settings:
    """Settings of ZeroWithBattle"""

    class PlayerSet:
        """有关玩家的设置部分"""

        def __init__(self):
            """初始化玩家设置"""
            # 生命条数
            self.lives = 1
            self.lives_min = 0
            self.lives_max = 2

            # 血量
            self.health = 3
            self.health_min = 0
            self.health_max = 10

            # 数字
            self.num = [1, 1]
            self.numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

            # 其它
            self.ban = [0, 0]
            pass

    def __init__(self):
        """初始化游戏设置"""
        pass


if __name__ == '__main__':
    print(Settings.__doc__)
