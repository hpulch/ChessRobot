import cv2 as vision
import numpy


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
            ('A', 1 * self.board.shape[1] // 8 - self.board.shape[1] // 16),
            ('B', 2 * self.board.shape[1] // 8 - self.board.shape[1] // 16),
            ('C', 3 * self.board.shape[1] // 8 - self.board.shape[1] // 16),
            ('D', 4 * self.board.shape[1] // 8 - self.board.shape[1] // 16),
            ('E', 5 * self.board.shape[1] // 8 - self.board.shape[1] // 16),
            ('F', 6 * self.board.shape[1] // 8 - self.board.shape[1] // 16),
            ('G', 7 * self.board.shape[1] // 8 - self.board.shape[1] // 16),
            ('H', 8 * self.board.shape[1] // 8 - self.board.shape[1] // 16),
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

        self.squares_dictionary["A1"][1], self.squares_dictionary["A1"][2] = 1, rook
        self.squares_dictionary["B1"][1], self.squares_dictionary["B1"][2] = 1, knight
        self.squares_dictionary["C1"][1], self.squares_dictionary["C1"][2] = 1, bishop
        self.squares_dictionary["D1"][1], self.squares_dictionary["D1"][2] = 1, queen
        self.squares_dictionary["E1"][1], self.squares_dictionary["E1"][2] = 1, king
        self.squares_dictionary["G1"][1], self.squares_dictionary["G1"][2] = 1, bishop
        self.squares_dictionary["F1"][1], self.squares_dictionary["F1"][2] = 1, knight
        self.squares_dictionary["H1"][1], self.squares_dictionary["H1"][2] = 1, rook

        self.squares_dictionary["A2"][1], self.squares_dictionary["A2"][2] = 1, pawn
        self.squares_dictionary["B2"][1], self.squares_dictionary["B2"][2] = 1, pawn
        self.squares_dictionary["C2"][1], self.squares_dictionary["C2"][2] = 1, pawn
        self.squares_dictionary["D2"][1], self.squares_dictionary["D2"][2] = 1, pawn
        self.squares_dictionary["E2"][1], self.squares_dictionary["E2"][2] = 1, pawn
        self.squares_dictionary["G2"][1], self.squares_dictionary["G2"][2] = 1, pawn
        self.squares_dictionary["F2"][1], self.squares_dictionary["F2"][2] = 1, pawn
        self.squares_dictionary["H2"][1], self.squares_dictionary["H2"][2] = 1, pawn

        self.squares_dictionary["A8"][1], self.squares_dictionary["A8"][2] = 2, rook
        self.squares_dictionary["B8"][1], self.squares_dictionary["B8"][2] = 2, knight
        self.squares_dictionary["C8"][1], self.squares_dictionary["C8"][2] = 2, bishop
        self.squares_dictionary["D8"][1], self.squares_dictionary["D8"][2] = 2, queen
        self.squares_dictionary["E8"][1], self.squares_dictionary["E8"][2] = 2, king
        self.squares_dictionary["G8"][1], self.squares_dictionary["G8"][2] = 2, bishop
        self.squares_dictionary["F8"][1], self.squares_dictionary["F8"][2] = 2, knight
        self.squares_dictionary["H8"][1], self.squares_dictionary["H8"][2] = 2, rook

        self.squares_dictionary["A7"][1], self.squares_dictionary["A7"][2] = 2, pawn
        self.squares_dictionary["B7"][1], self.squares_dictionary["B7"][2] = 2, pawn
        self.squares_dictionary["C7"][1], self.squares_dictionary["C7"][2] = 2, pawn
        self.squares_dictionary["D7"][1], self.squares_dictionary["D7"][2] = 2, pawn
        self.squares_dictionary["E7"][1], self.squares_dictionary["E7"][2] = 2, pawn
        self.squares_dictionary["G7"][1], self.squares_dictionary["G7"][2] = 2, pawn
        self.squares_dictionary["F7"][1], self.squares_dictionary["F7"][2] = 2, pawn
        self.squares_dictionary["H7"][1], self.squares_dictionary["H7"][2] = 2, pawn

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

    def move(self, mvf, mvt):
        self.squares_dictionary[mvt][1] = self.squares_dictionary[mvf][1]
        self.squares_dictionary[mvt][2] = self.squares_dictionary[mvf][2]
        self.squares_dictionary[mvf][1] = 0
        self.squares_dictionary[mvf][2] = (0, 0, 0)


board = Board((400, 400, 3))
board.move('E2', 'E4')
board.move('D7', 'D5')
board.move('E4', 'D5')

board.draw()
vision.imshow('Board', board.board)
vision.waitKey(0)