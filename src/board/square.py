from piece import Piece


class Square:
    MAP = {
        "0": "A",
        "1": "B",
        "2": "C",
        "3": "D",
        "4": "E",
        "5": "F",
        "6": "G",
        "7": "H",
    }

    def __init__(self, row: int, col: int, piece: Piece) -> None:
        self.location = (row, col)
        self.piece = piece

    def __str__(self) -> str:
        return str(Piece) + self.MAP[str(self.location[1])] + (self.location[0]+1)