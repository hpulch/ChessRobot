import cv2 as vision
import numpy
import chess.engine
 

def _toggle(bit):
    black = 10, 72, 137
    white = 101, 166, 209
    if bit == white:
        bit = black
    else:
        bit = white
    return bit


class Board:
    def __init__(self, dimensions):
        self.board_size = dimensions
        self.board = numpy.zeros(self.board_size, dtype='uint8')
        self.squares_dictionary = {}
        self.detailSquares()
        self.reset()
        self.draw()

    def __str__(self):
        pass

    def makeBoard(self):
        tile = int(self.board.shape[0] // 8)
        square = 10, 72, 137
        for column in range(8):
            for row in range(8):
                if row == 0:
                    square = _toggle(square)
                self.board[column * tile:(column + 1) * tile, (row * tile):((row + 1) * tile)] = square
                square = _toggle(square)

    def detailSquares(self):
        alphabet = [
            ('a', 1 * self.board.shape[1] // 8 - self.board.shape[1] // 16),
            ('b', 2 * self.board.shape[1] // 8 - self.board.shape[1] // 16),
            ('c', 3 * self.board.shape[1] // 8 - self.board.shape[1] // 16),
            ('d', 4 * self.board.shape[1] // 8 - self.board.shape[1] // 16),
            ('e', 5 * self.board.shape[1] // 8 - self.board.shape[1] // 16),
            ('f', 6 * self.board.shape[1] // 8 - self.board.shape[1] // 16),
            ('g', 7 * self.board.shape[1] // 8 - self.board.shape[1] // 16),
            ('h', 8 * self.board.shape[1] // 8 - self.board.shape[1] // 16),
        ]
        numbers = [
            ('1', 8 * self.board.shape[0] // 8 - self.board.shape[0] // 16),
            ('2', 7 * self.board.shape[0] // 8 - self.board.shape[0] // 16),
            ('3', 6 * self.board.shape[0] // 8 - self.board.shape[0] // 16),
            ('4', 5 * self.board.shape[0] // 8 - self.board.shape[0] // 16),
            ('5', 4 * self.board.shape[0] // 8 - self.board.shape[0] // 16),
            ('6', 3 * self.board.shape[0] // 8 - self.board.shape[0] // 16),
            ('7', 2 * self.board.shape[0] // 8 - self.board.shape[0] // 16),
            ('8', 1 * self.board.shape[0] // 8 - self.board.shape[0] // 16)
        ]
        square = {}
        for letter in alphabet:
            for digit in numbers:
                square = {letter[0] + digit[0]: [(letter[1], digit[1]), 0, (0, 0, 0)]}
                self.squares_dictionary = self.squares_dictionary | square

    def reset(self):
        rook = (0, 0, 255)
        knight = (0, 255, 255)
        bishop = (0, 255, 0)
        queen = (255, 255, 0)
        king = (255, 0, 0)
        pawn = (255, 0, 255)

        self.squares_dictionary["a1"][1], self.squares_dictionary["a1"][2] = 1, rook
        self.squares_dictionary["b1"][1], self.squares_dictionary["b1"][2] = 1, knight
        self.squares_dictionary["c1"][1], self.squares_dictionary["c1"][2] = 1, bishop
        self.squares_dictionary["d1"][1], self.squares_dictionary["d1"][2] = 1, queen
        self.squares_dictionary["e1"][1], self.squares_dictionary["e1"][2] = 1, king
        self.squares_dictionary["g1"][1], self.squares_dictionary["g1"][2] = 1, bishop
        self.squares_dictionary["f1"][1], self.squares_dictionary["f1"][2] = 1, knight
        self.squares_dictionary["h1"][1], self.squares_dictionary["h1"][2] = 1, rook

        self.squares_dictionary["a2"][1], self.squares_dictionary["a2"][2] = 1, pawn
        self.squares_dictionary["b2"][1], self.squares_dictionary["b2"][2] = 1, pawn
        self.squares_dictionary["c2"][1], self.squares_dictionary["c2"][2] = 1, pawn
        self.squares_dictionary["d2"][1], self.squares_dictionary["d2"][2] = 1, pawn
        self.squares_dictionary["e2"][1], self.squares_dictionary["e2"][2] = 1, pawn
        self.squares_dictionary["g2"][1], self.squares_dictionary["g2"][2] = 1, pawn
        self.squares_dictionary["f2"][1], self.squares_dictionary["f2"][2] = 1, pawn
        self.squares_dictionary["h2"][1], self.squares_dictionary["h2"][2] = 1, pawn

        self.squares_dictionary["a8"][1], self.squares_dictionary["a8"][2] = 2, rook
        self.squares_dictionary["b8"][1], self.squares_dictionary["b8"][2] = 2, knight
        self.squares_dictionary["c8"][1], self.squares_dictionary["c8"][2] = 2, bishop
        self.squares_dictionary["d8"][1], self.squares_dictionary["d8"][2] = 2, queen
        self.squares_dictionary["e8"][1], self.squares_dictionary["e8"][2] = 2, king
        self.squares_dictionary["g8"][1], self.squares_dictionary["g8"][2] = 2, bishop
        self.squares_dictionary["f8"][1], self.squares_dictionary["f8"][2] = 2, knight
        self.squares_dictionary["h8"][1], self.squares_dictionary["h8"][2] = 2, rook

        self.squares_dictionary["a7"][1], self.squares_dictionary["a7"][2] = 2, pawn
        self.squares_dictionary["b7"][1], self.squares_dictionary["b7"][2] = 2, pawn
        self.squares_dictionary["c7"][1], self.squares_dictionary["c7"][2] = 2, pawn
        self.squares_dictionary["d7"][1], self.squares_dictionary["d7"][2] = 2, pawn
        self.squares_dictionary["e7"][1], self.squares_dictionary["e7"][2] = 2, pawn
        self.squares_dictionary["g7"][1], self.squares_dictionary["g7"][2] = 2, pawn
        self.squares_dictionary["f7"][1], self.squares_dictionary["f7"][2] = 2, pawn
        self.squares_dictionary["h7"][1], self.squares_dictionary["h7"][2] = 2, pawn

    def draw(self):
        self.makeBoard()
        for tile in self.squares_dictionary:
            if self.squares_dictionary[tile][1] == 1:
                vision.circle(self.board, self.squares_dictionary[tile][0], 20, self.squares_dictionary[tile][2], thickness=-1)
                vision.circle(self.board, self.squares_dictionary[tile][0], 5, (255, 255, 255), thickness=-1)
            elif self.squares_dictionary[tile][1] == 2:
                vision.circle(self.board, self.squares_dictionary[tile][0], 20, self.squares_dictionary[tile][2], thickness=-1)
                vision.circle(self.board, self.squares_dictionary[tile][0], 5, (0, 0, 0), thickness=-1)
            else:
                pass

    def move(self, mv: str):
        move = list(mv)
        mvf = str(move[0] + move[1])
        mvt = str(move[2] + move[3])
        self.squares_dictionary[mvt][1] = self.squares_dictionary[mvf][1]
        self.squares_dictionary[mvt][2] = self.squares_dictionary[mvf][2]
        self.squares_dictionary[mvf][1] = 0
        self.squares_dictionary[mvf][2] = (0, 0, 0)

path = r'C:\Users\pulchihd\Desktop\PythonChess\stockfish-windows-x86-64-modern\stockfish\stockfish-windows-x86-64-modern'
engine = chess.engine.SimpleEngine.popen_uci(path)
logical_board = chess.Board()
physical_board = Board((400, 400, 3))
physical_board.draw()

while True:
    print(logical_board)
    physical_board.draw()
    vision.imwrite('Board.png', physical_board.board)
    # vision.imshow('Board', physical_board.board)
    # vision.waitKey(0)
    print("White to play, please enter a move using the UCI protocol format.")
    try:
        user_input = input("Move: ")
        move = chess.Move.from_uci(user_input)
    except Exception:
        print("An error occurred:", Exception)
        continue
    if move in logical_board.legal_moves:
        logical_board.push(move)
        physical_board.move(user_input)
    else:
        print("Illegal move, try again")
        continue

    print("Black to play, calculating...") 
    try:
        limit = chess.engine.Limit(time=5.0)
        best_move = engine.play(logical_board, limit=limit)
    except Exception:
        print("An error occurred:", Exception)
        print("ChessBot has resigned")
        break
    logical_board.push(chess.Move.from_uci(str(best_move.move)))
    physical_board.move(str(best_move.move))
