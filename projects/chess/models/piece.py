# Base Piece class (abstract/parent)

class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def get_color(self):
        pass

    def get_position(self):
        pass

    def get_type(self):
        return self.type

    def move(self):
        pass

    def is_valid(self):
        pass

    def possible_moves(self, board):
        pass


