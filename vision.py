import numpy
import cv2 as vision

height = 480
width = 640

canvas = numpy.zeros((height, width, 3), numpy.uint8)
canvas[:] = (255,255,255)

vision.rectangle(canvas, (0,0), (300, 200), (0, 255, 0), -1)


vision.imshow('Blank Image', canvas)
vision.waitKey(0)
vision.destroyAllWindows()