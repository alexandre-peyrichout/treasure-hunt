from src.setup import Setup
from src.carte import Carte


class Game:
    map = None
    setup_tasks = []

    def __init__(
        self, input_filename="input.txt", output_filename="output.txt"
    ) -> None:
        self.input_filename = input_filename
        self.output_filename = output_filename

    def read_input(self) -> None:
        input_file = open(self.input_filename, "r")
        for line in input_file:
            steps = line.split(" - ")
            if "#" in line[0]:
                pass
            elif "C" in line[0]:
                largeur = int(steps[1])
                hauteur = int(steps[2])
                self.map = Carte(largeur, hauteur)
            else:
                self.setup_tasks.append(Setup(steps))

    def write_output(self) -> None:
        output_file = open(self.output_filename, "w")
        output_file.write(f"{self.map.to_result()}\n")
        for mountain in self.map.mountains:
            output_file.write(f"{mountain.to_result()}\n")
        for treasure in self.map.treasures:
            if treasure.count:
                output_file.write(f"{treasure.to_result()}\n")
        for adventurer in self.map.adventurers:
            output_file.write(f"{adventurer.to_result()}\n")

    def play(self) -> None:
        self.read_input()
        if not self.map:
            return
        else:
            self.map.process_setup(self.setup_tasks)
            self.map.release_adventurers()
            self.write_output()
