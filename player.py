from settings import Settings


class Player:
    """"""

    def __init__(self):
        """"""
        self.__set__: Settings.PlayerSet = Settings.PlayerSet()

        self.lives: int = self.__set__.lives

        self.health: int = self.__set__.health

        self.num: list[int] = self.__set__.num

        self.numbers: tuple = self.__set__.numbers

        self.ban: list[int] = self.__set__.ban

        pass

    def get_lives(self, l_type: int = 0):
        """获取玩家当前血量"""
        match l_type:
            case 0:
                return self.lives
            case 1:
                return self.__set__.lives_max
            case -1:
                return self.__set__.lives_min
            case 2:
                return self.__set__.lives
            case _:
                raise RuntimeError(f"ArgumentError from Player.get_lives: {l_type=:}")

    def add_lives(self, lives_num: int = 1):
        """增加玩家生命数
        返回 实际增减生命数（生命数不能超过最大值）
        """
        if lives_num < 0:
            raise RuntimeError(f"ArgumentError from Player.add_lives: {lives_num=:}")

        r_lives: int = lives_num

        if self.lives + lives_num <= self.get_lives(1):
            self.lives += lives_num
        else:
            r_lives = self.get_lives(1) - self.lives
            self.lives = self.get_lives(1)

        return r_lives

    def sub_lives(self, lives_num: int = 1):
        """减少玩家血量 lives_num >= 0
        返回 实际增减血量（血量不能低于最小值）
        """
        if lives_num < 0:
            raise RuntimeError(f"ArgumentError from Player.sub_lives: {lives_num=:}")

        r_lives: int = lives_num

        if self.lives - lives_num > self.get_lives(-1):
            self.lives -= lives_num
        else:
            r_lives = self.lives - self.get_lives(-1)
            self.lives = self.get_health(-1)

        return r_lives

    def get_health(self, h_type: int = 0):
        """获取玩家当前血量"""
        match h_type:
            case 0:
                return self.health
            case 1:
                return self.__set__.health_max
            case -1:
                return self.__set__.health_min
            case 2:
                return self.__set__.health
            case _:
                raise RuntimeError(f"ArgumentError from Player.get_health: {h_type=:}")

    def add_health(self, health_num: int):
        """增加玩家血量
        返回 实际增减血量（血量不能超过最大值）
        """
        if health_num < 0:
            raise RuntimeError(f"ArgumentError from Player.add_health: {health_num=:}")

        rhealth: int = health_num

        if self.health + health_num <= self.get_health(1):
            self.health += health_num
        else:
            rhealth = self.get_health(1) - self.health
            self.health = self.get_health(1)

        return rhealth

    def sub_health(self, health_num: int):
        """减少玩家血量 health_num >= 0
        返回 实际增减血量（血量不能低于最小值）
        """
        if health_num < 0:
            raise RuntimeError(f"ArgumentError from Player.sub_health: {health_num=:}")

        rhealth: int = health_num

        if self.health - health_num > self.get_health(-1):
            self.health -= health_num
        else:
            rhealth = self.health - self.get_health(-1)
            self.health = self.get_health(-1)
            self.on_death(health_num)

        return rhealth

    def set_health(self, health_num: int):
        """"""
        if health_num > self.get_health(-1):
            self.health = health_num
            return True
        else:
            raise RuntimeError(f"ArgumentError from Player.set_health: {health_num=:}")

    def get_num(self, n_type: int = 0):
        """"""
        if n_type == 0:
            return self.num[:]
        elif n_type == 1:
            return self.__set__.num[:]
        else:
            raise RuntimeError(f"ArgumentError from Player.get_num: {n_type=:}")

    def get_number(self, num_id: int):
        """"""
        if num_id in (0, 1):
            return self.get_num()[num_id]
        else:
            raise RuntimeError(f"ArgumentError from Player.get_number: {num_id=:}")

    def get_number_r(self, num_id: int):
        """"""
        if num_id in (0, 1):
            return self.numbers[self.get_num()[num_id]]
        else:
            raise RuntimeError(f"ArgumentError from Player.get_number_r: {num_id=:}")

    def get_number_r2(self, num_id: int):
        """"""
        if num_id in range(10):
            return self.get_num(1)[num_id]
        else:
            raise RuntimeError(f"ArgumentError from Player.get_number_r2: {num_id=:}")

    def set_num(self, num_id: int, new_num: int):
        """"""
        if num_id in (0, 1) and new_num in range(10):
            self.num[num_id] = new_num
            return True
        else:
            raise RuntimeError(f"ArgumentError from Player.set_num: {num_id=:} {new_num=:}")

    def set_nums(self, nums: list[int]):
        """懒"""
        self.num = nums[:]
        return True

    def add_num(self, num_id: int, opp_num: int):
        """"""
        if num_id in (0, 1) and opp_num in range(10):
            if self.can_add(num_id, opp_num):
                return self.set_num(num_id, (self.get_number(num_id) + opp_num) % 10)
            else:
                return False
        else:
            raise RuntimeError(f"ArgumentError from Player.add_num: {num_id=:} {opp_num=:}")

    def can_add(self, num_id: int, opp_num: int):
        """"""
        # 未写完
        return True

    def get_ban(self, b_type: int = 0):
        """"""
        if b_type == 0:
            return self.ban[:]
        elif b_type == 1:
            return self.__set__.ban[:]
        else:
            raise RuntimeError(f"ArgumentError from Player.get_ban: {b_type=:}")

    def get_ban_c(self, num_id: int):
        """"""
        if num_id in (0, 1):
            return self.get_ban()[num_id]
        else:
            raise RuntimeError(f"ArgumentError from Player.get_ban_c: {num_id=:}")

    def add_ban(self, num_id: int, turns: int = 1):
        """"""
        if num_id in (0, 1) and turns >= 0:
            self.ban[num_id] += turns
            return turns
        else:
            raise RuntimeError(f"ArgumentError from Player.get_ban: {num_id=:} {turns=:}")

    def sub_ban(self, num_id: int, turns: int = 1):
        """"""
        if num_id in (0, 1) and turns >= 0:
            if self.get_ban_c(num_id) - turns >= 0:
                self.ban[num_id] -= turns
                return turns
            else:
                r_turns: int = self.get_ban_c(num_id)
                self.ban[num_id] = 0
                return r_turns
        else:
            raise RuntimeError(f"ArgumentError from Player.sub_ban: {num_id=:} {turns=:}")

    def on_death(self, health_num: int = 0):
        """"""
        self.sub_lives()
        if self.get_lives() > 0:
            return self.rebirth()
        else:
            return True

    def rebirth(self):
        """"""
        self.set_health(self.get_health(2))
        self.set_nums(self.get_num(1))
        self.set_bans(self.get_ban(1))

    def set_bans(self, bans: list[int]):
        """"""
        self.ban = bans[:]


if __name__ == '__main__':
    p_t = Player()
    p_t.add_health(7)
    p_t.sub_health(10)
    p_t.sub_health(1)
    print(p_t.get_health(0))
    while True:
        exec(input())
