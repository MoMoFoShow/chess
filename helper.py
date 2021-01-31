from pieces import *

def dump():
    for piece in gamestate:
        print(piece)

def find(desiredmove):
    for piece in gamestate:
        if (piece.xpos, piece.ypos) == (int(desiredmove[0]), int(desiredmove[1])):
            return piece
    return False

def statemove():
    return input('Please state move. \n')

def check(gamestate): # sees if there is a check in given gamestate.
    pass
# if there is a check, return True, else return False.
