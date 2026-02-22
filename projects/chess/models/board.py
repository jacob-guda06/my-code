# Board class - manages the 8x8 grid

class Board:
    def __init__(self):
        self.board = []
        for i in range(8):
            row = []
            for j in range(8):
                row.append(0)
            self.board.append(row)
    
    # Takes the values in init and converts them into boxes
    def display(self):
        print("   a  b  c  d  e  f  g  h")
        for i in range(8):
            row = self.board[i]
            row_num = str(8 - i)
            row_string = row_num + " "
            for square in row:
                if square == 0:
                    row_string = row_string + "[ ]"
                else:
                    row_string = row_string + f"[{square}]"
            print(row_string)

    # Assigns the pieces
    def setup_board(self):
        # Black back row (row 8, index 0)
        black_pieces = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        for j in range(8):
            self.board[0][j] = black_pieces[j]

        # Black pawns (row 7, index 1)
        for j in range(8):
            self.board[1][j] = 'p'
        
        # White pawns (row 2, index 6)
        for j in range(8):
            self.board[6][j] = 'P'
        
        # White back row (row 1, index 7)
        white_pieces = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        for j in range(8):
            self.board[7][j] = white_pieces[j]

# Temporary main method
board = Board()
board.setup_board()
board.display()
