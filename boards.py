import cv2 as cv
import numpy as np


def makeBoard(blk, wht, surf):
    tile = int(board.shape[0]//8)
    black = blk
    white = wht

    toggle = black
    for col in range(8):
        for row in range(8):
            if row == 0:
                if toggle == white:
                    toggle = black
                else:
                    toggle = white
            surf[col * tile:(col + 1) * tile, (row * tile):((row + 1) * tile)] = toggle
            if toggle == white:
                toggle = black
            else:
                toggle = white


board_size = (400, 400, 3)
coffee = 10, 72, 137
cream = 101, 166, 209

board = np.zeros(board_size, dtype='uint8')
makeBoard(coffee, cream, board)

cv.circle(board, ((board.shape[1]//16), (board.shape[0]//16)+(board.shape[0]//4)), 20, (0, 0, 255), thickness=-1)

cv.imshow('Board', board)

# cv.imwrite('board1.jpg', board)

cv.waitKey(0)


