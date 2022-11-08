import Piece

class Pawn(Piece):
    def __init__(self, color):
        super.__init__("pawn", 1, color)

    def validate_move(initial_pos, final_pos):
        pass