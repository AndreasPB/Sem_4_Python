import numpy as np

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Bird:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

class Pig:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

def draw_board():
    dimentions = Board(5, 5)

    board = [['*']*dimentions.width]*dimentions.height
    np_board = np.zeros((dimentions.width)), dimentions.height)
    
    board[1][3] = 'X'
    np_board[1][3] = 'X'

    print(board)
    print(np_board)

    for i in range(dimentions.height):
        print(board[i][0])

        for j in range(dimentions.width):
            print(board[i][j], end='')