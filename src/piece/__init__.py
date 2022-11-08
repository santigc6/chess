from abc import ABC

class Piece(ABC):
    def __init__(self, name, points, color):
        self.name = name
        self.points = points
        self.color = color

    def validate_move(initial_pos, final_pos):
        pass
