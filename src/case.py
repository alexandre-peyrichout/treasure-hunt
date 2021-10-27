class Case:
    visitor = None
    has_treasure = False

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Plaine(Case):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.is_cross_allowed = True if self.visitor is None else False


class Montagne(Case):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.is_cross_allowed = False

    def to_result(self) -> str:
        return " - ".join(["M", str(self.x), str(self.y)])

    @staticmethod
    def register(steps, map, mountains) -> None:
        x = int(steps[1])
        y = int(steps[2])
        mountain = Montagne(x, y)
        mountains.append(mountain)
        map[y][x] = mountain


class Tresor(Case):
    def __init__(self, x, y, count) -> None:
        super().__init__(x, y)
        self.is_cross_allowed = True if self.visitor is None else False
        self.has_treasure = count > 0
        self.count = count

    def to_result(self) -> str:
        return " - ".join(["T", str(self.x), str(self.y), str(self.count)])

    @staticmethod
    def register(steps, map, treasures) -> None:
        x = int(steps[1])
        y = int(steps[2])
        count = int(steps[3])
        treasure = Tresor(x, y, count)
        treasures.append(treasure)
        map[y][x] = treasure
