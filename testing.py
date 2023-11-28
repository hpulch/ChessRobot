import numpy
import cv2 as vision
from matplotlib import pyplot as plt

image = vision.imread('board0.jpg')
gray = vision.cvtColor(image, vision.COLOR_BGR2GRAY)
_, thresh = vision.threshold(gray, 12, 255, vision.THRESH_BINARY)
contours, _ = vision.findContours(thresh, vision.RETR_EXTERNAL, vision.CHAIN_APPROX_SIMPLE)

board = numpy.zeros((500,500,3), dtype='uint8')
vision.drawContours(board, contours, -1, (0, 255, 0), 1)


vision.imshow('Board', board)

vision.waitKey(0)