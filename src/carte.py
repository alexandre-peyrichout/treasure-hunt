from typing import List

from src.setup import Setup
from src.case import Plaine

ORIENTATION_VALUES = {"N": -1, "O": -1, "S": 1, "E": 1}


class Carte:
    rows = []
    mountains = []
    treasures = []
    adventurers = []

    def __init__(self, largeur, hauteur) -> None:
        self.largeur = largeur
        self.hauteur = hauteur
        return self.generate()

    def to_result(self) -> str:
        return " - ".join(["C", str(self.largeur), str(self.hauteur)])

    def generate(self) -> None:
        for y in range(self.hauteur):
            buffer_row = []
            for x in range(self.largeur):
                buffer_row.append(Plaine(x, y))
            self.rows.append(buffer_row)

    def process_setup(self, tasks: List[Setup]) -> None:
        for task in tasks:
            task.process(self.rows, self.adventurers, self.mountains, self.treasures)

    def release_adventurers(self) -> None:
        while any([adventurer.is_active() for adventurer in self.adventurers]):
            for adventurer in self.adventurers:
                if adventurer.is_active():
                    adventurer.execute_next_move(self.rows)
