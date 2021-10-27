from src.case import Montagne, Tresor
from src.aventurier import Aventurier


class Setup:
    def __init__(self, steps) -> None:
        self.steps = steps

    def process(self, map, adventurers, mountains, treasures) -> None:
        if not map:
            return
        else:
            if self.steps[0] == "M":
                Montagne.register(self.steps, map, mountains)

            elif self.steps[0] == "T":
                Tresor.register(self.steps, map, treasures)

            elif self.steps[0] == "A":
                Aventurier.register(self.steps, map, adventurers)
