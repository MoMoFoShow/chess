turn = 0  # even numbers represent white, odd numbers represent black
gamestate = [] # when variable is used add global if not working

def dump():
    for piece in gamestate:
        print(piece)

class Piece:
    def __init__(self, color, xpos, ypos):
        self.color = color
        self.xpos = xpos
        self.ypos = ypos

    def __str__(self):
        output = 'color: ' + self.color + '\n'
        output = output + 'xpos: ' + str(self.xpos) + '\n'
        output = output + 'ypos: ' + str(self.ypos) + '\n'
        return output

    def opensquare(self, x, y): # validates that intended square to move to is not already occupied
        for piece in gamestate:
            if (piece.xpos, piece.ypos) == (x, y):
                return piece.color
            return True

    def inmap(self, x, y): # validates move is inside the map
        '''y = int(y)
        x = int(x)'''
        if 1 <= x <= 9:
            if 1 <= y <= 8:
                if x - abs(x) == 0:
                    if y - abs(y) == 0: # once input field is implemented, move input checking and making sure
                        # decimal isn't inputted into there to be able to tell user their mistake
                        return True

    def nocheck(self): # validates that intended move will not put player in check
        return True

    def validate(self, x, y):  # validates move path specific to piece
        # if self.opensquare(): redundant with for loop
        if self.inmap(x, y):
            if self.nocheck():
                return True

    def move(self, x, y):
        if self.validate(x, y):
            self.xpos = x
            self.ypos = y
            return True
        else:
            return False


class Bishop(Piece):
    #def __init__(self, color, xpos, ypos):
        #super.__init__(color, xpos, ypos)

    def __str__(self):
        superstr = super().__str__()
        output = 'bishop \n'
        output = output + superstr
        return output

    def validate(self, x, y):
        if super().validate(x, y):
            dx = x - super().xpos
            dy = y - super().ypos
            pdx = abs(dx)
            pdy = abs(dy)
            if pdx != pdy:
                return False
            for squares in range(pdx):
                nxtx = super().xpos + (dx / pdx) * (squares + 1)
                nxty = super().ypos + (dy / pdy) * (squares + 1)
                squarestate = super().opensquare(nxtx, nxty)
                if not squarestate:
                    if nxtx != x:
                        return False
                    if self.color != squarestate:
                        return True


class Rook(Piece):
    #def __init__(self, color, xpos, ypos):
        #super.__init__(color, xpos, ypos)

    def __str__(self):
        superstr = super().__str__()
        output = 'rook \n'
        output = output + superstr
        return output

    def validate(self, x, y):
        if super().validate(x, y):
            dx = x - self.xpos
            dy = y - self.ypos
            if dx != 0 and dy == 0:
                for squares in range(dx):
                    nxtx = super().xpos + (dx / abs(dx)) * (squares + 1)
                    squarestate = super().opensquare(nxtx, y)
                    if not squarestate:
                        if nxtx != x:
                            return False
                        if self.color != squarestate:
                            return True  # Some common code here - at the end of coding optimize
                    elif dx == 0 and dy != 0:
                        for squares in range(dy):
                            nxty = super().xpos + (dy / abs(dy)) * (squares + 1)
                            squarestate = super().opensquare(x, nxty)
                            if not squarestate:
                                if nxty != y:
                                    return False
                                if self.color != squarestate:
                                    return True

class Queen(Piece):
    def __str__(self):
        superstr = super().__str__()
        output = 'queen \n'
        output = output + superstr
        return output

    def validate(self, x, y):
        if super.validate(x, y):
            dx = x - super().xpos
            dy = y - super().xpos
            pdx = abs(dx)
            pdy = abs(dy)
            if dx != 0 and dy == 0:
                for squares in range(dx):
                    nxtx = super().xpos + (dx / abs(dx)) * (squares + 1)
                    squarestate = super().opensquare(nxtx, y)
                    if not squarestate:
                        if nxtx != x:
                            return False
                        if self.color != squarestate:
                            return True  # Some common code here - at the end of coding optimize
            elif dx == 0 and dy != 0:
                for squares in range(dy):
                    nxty = super().xpos + (dy / abs(dy)) * (squares + 1)
                    squarestate = super().opensquare(x, nxty)
                    if not squarestate:
                        if nxty != y:
                            return False
                        if self.color != squarestate:
                            return True
            elif pdx != pdy:
                return False
            for squares in range(pdx):
                nxtx = super().xpos + (dx / pdx) * (squares + 1)
                nxty = super().ypos + (dy / pdy) * (squares + 1)
                squarestate = super().opensquare(nxtx, nxty)
                if not squarestate:
                    if nxtx != x:
                        return False
                    if self.color != squarestate:
                        return True

class Advisor(Piece):
    def __str__(self):
        superstr = super().__str__()
        output = 'advisor \n'
        output = output + superstr
        return output

    def validate(self, x, y):
        if super().validate(x, y):
            if (abs(King.xpos-x) > 1 or abs(King.ypos-y) > 1) and (abs(Queen.xpos-x) > 1 or abs(Queen.ypos-y) > 1):
                # improve logic for how advisor moves after queen is dead
                return False
            dx = x - super().xpos
            dy = y - super().xpos
            pdx = abs(dx)
            pdy = abs(dy)
            if dx != 0 and dy == 0:
                for squares in range(dx):
                    nxtx = super().xpos + (dx / abs(dx)) * (squares + 1)
                    squarestate = super().opensquare(nxtx, y)
                    if not squarestate:
                        if nxtx != x:
                            return False
                        if self.color != squarestate:
                            return True  # Some common code here - at the end of coding optimize
            elif dx == 0 and dy != 0:
                for squares in range(dy):
                    nxty = super().xpos + (dy / abs(dy)) * (squares + 1)
                    squarestate = super().opensquare(x, nxty)
                    if not squarestate:
                        if nxty != y:
                            return False
                        if self.color != squarestate:
                            return True
            elif pdx != pdy:
                return False
            for squares in range(pdx):
                nxtx = super().xpos + (dx / pdx) * (squares + 1)
                nxty = super().ypos + (dy / pdy) * (squares + 1)
                squarestate = super().opensquare(nxtx, nxty)
                if not squarestate:
                    if nxtx != x:
                        return False
                    if self.color != squarestate:
                        return True

# initial piece positions below

gamestate = [Rook('white', 1, 1),
             Rook('white', 9, 1),
             Rook('black', 1, 8),
             Rook('black', 9, 8),
             Bishop('white', 3, 1),
             Bishop('white', 7, 1),
             Bishop('black', 3, 8),
             Bishop('black', 7, 8),
             Queen('white', 4, 1),
             Queen('black', 4, 8),
             Advisor('white', 6, 1),
             Advisor('black', 6, 8)]




