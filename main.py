from display import *
from draw import *
from matrix import *
import random

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        matrix[row][col]=random.randint(0,600)
print("printing")
print_matrix(matrix)
draw_lines( matrix, screen, color)
display(screen)
