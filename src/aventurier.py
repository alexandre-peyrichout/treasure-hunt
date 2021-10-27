ORIENTATION_ORDER = ["N", "E", "S", "O"]
ORIENTATION_VALUES = {"N": -1, "O": -1, "S": 1, "E": 1}


class Move:
    def __init__(self, value):
        self.value = value
        self.type = self.get_type()

    def get_type(self):
        if self.value in ["G", "D"]:
            return "change_orientation"
        elif self.value == "A":
            return "change_case"


class Aventurier:
    def __init__(self, x, y, name, orientation, sequence) -> None:
        self.x = x
        self.y = y
        self.name = name
        self.orientation = orientation
        self.sequence = sequence
        self.treasure_collected = 0

    def _collect_treasure(self, treasure) -> None:
        self.treasure_collected += 1
        treasure.count -= 1

    def _update_orientation(self, move) -> None:
        current_index = ORIENTATION_ORDER.index(self.orientation)
        if move.value == "D":
            if current_index + 1 < len(ORIENTATION_ORDER):
                self.orientation = ORIENTATION_ORDER[current_index + 1]
            else:
                self.orientation = ORIENTATION_ORDER[0]

        elif move.value == "G":
            if (current_index - 1) >= 0:
                self.orientation = ORIENTATION_ORDER[current_index - 1]
            else:
                self.orientation = ORIENTATION_ORDER[len(ORIENTATION_ORDER) - 1]

    def _update_position(self, move, rows) -> None:
        if move.value == "A":
            current_case = rows[self.y][self.x]

            if self.orientation in ["N", "S"]:
                new_y = self.y + ORIENTATION_VALUES[self.orientation]
                if 0 <= new_y < len(rows):
                    new_case = rows[new_y][self.x]
                    if new_case.is_cross_allowed:
                        new_case.visitor = self
                        current_case.visitor = None
                        self.y = new_y
                        if new_case.has_treasure:
                            self._collect_treasure(new_case)

            elif self.orientation in ["E", "O"]:
                new_x = self.x + ORIENTATION_VALUES[self.orientation]
                if 0 <= new_x < len(rows[0]):
                    new_case = rows[self.y][new_x]
                    if new_case.is_cross_allowed:
                        new_case.visitor = self
                        current_case.visitor = None
                        self.x = new_x
                        if new_case.has_treasure:
                            self._collect_treasure(new_case)

    def is_active(self) -> bool:
        return len(self.sequence) > 0

    def _fetch_next_move(self) -> Move:
        move = Move(self.sequence[0])
        self.sequence = self.sequence[1:]
        return move

    def execute_next_move(self, rows) -> None:
        move = self._fetch_next_move()
        if move.type == "change_orientation":
            self._update_orientation(move)
        elif move.type == "change_case":
            self._update_position(move, rows)

    def to_result(self) -> str:
        return " - ".join(
            [
                "A",
                self.name,
                str(self.x),
                str(self.y),
                self.orientation,
                str(self.treasure_collected),
            ]
        )

    @staticmethod
    def register(steps, map, adventurers) -> None:
        name = steps[1]
        x = int(steps[2])
        y = int(steps[3])
        orientation = steps[4]
        sequence = steps[5]
        if map[y][x].is_cross_allowed:
            adventurer = Aventurier(x, y, name, orientation, sequence)
            adventurers.append(adventurer)
            map[y][x].visitor = adventurer
