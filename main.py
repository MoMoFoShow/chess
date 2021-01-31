from pieces import *
from helper import *
turn = True  # True represents white, False represents black

while True:
    desiredmove = statemove()
    if desiredmove == '0000':
        dump()
        continue
    else:
        piecefound = find(desiredmove)
        if piecefound == False:
            print('This piece cannot be found, please try again. \n')
            continue
        if turn == True:
            if piecefound.color == 'black':
                print('The specified piece to move is black, however it is white\'s turn. \n')
                continue
        else:
            if piecefound.color == 'white':
                print('The specified piece to move is white, however it is black\'s turn. \n')
                continue
        if piecefound.move(int(desiredmove[2]), int(desiredmove[3])) == False:
            print('This move is invalid, please try again. \n')
            continue
    turn = not turn





