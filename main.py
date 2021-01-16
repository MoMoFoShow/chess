from pieces import *
desiredmove = [-1,-1,-1,-1]
piecefound = Rook('black', 1, 0)

for piece in gamestate:
    if (piece.xpos, piece.ypos) == (desiredmove[0], desiredmove[1]):
        piecefound = piece
        break
dump()
while not piecefound.move(int(desiredmove[2]), int(desiredmove[3])):
    desiredmove = input('Please state move \n')
    if desiredmove == '0000':
        dump()
        desiredmove = list(input('Please state move \n'))
        continue
    desiredmove = list(desiredmove)
    continue




