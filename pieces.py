from helper import check

gamestate = [] # when variable is used add global if not working

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

    def nocheck(self): # validates that intended move will not put player in check - uses check func from helper, on altered position where move has already been made.
        '''intendedState = gamestate
        # make the move in intendedState
        if check(intendedState):
            return False
        else:
            return True'''
        pass

    def validate(self, x, y):  # validates move path specific to piece
        if self.inmap(x, y):
            if self.nocheck():
                return True

    def move(self, x, y):
        if self.validate(x, y):
            for piece in gamestate:
                if (piece.xpos, piece.ypos) == (x, y):
                    del piece
                    break
            self.xpos = x
            self.ypos = y
            return True
        else:
            return False

class Bishop(Piece):
    def __str__(self):
        superstr = super().__str__()
        output = 'bishop \n'
        output = output + superstr
        return output

    def validate(self, x, y):
        if super().validate(x, y):
            dx = x - self.xpos
            dy = y - self.ypos
            pdx = abs(dx)
            pdy = abs(dy)
            if pdx != pdy:
                return False
            for squares in range(pdx):
                nxtx = self.xpos + (dx / pdx) * (squares + 1)
                nxty = self.ypos + (dy / pdy) * (squares + 1)
                squarestate = self.opensquare(nxtx, nxty)
                if not squarestate:
                    if nxtx != x:
                        return False
                    if self.color == squarestate:
                        return False
        return True

class Rook(Piece):
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
                    nxtx = self.xpos + (dx / abs(dx)) * (squares + 1)
                    squarestate = self.opensquare(nxtx, y)
                    if not squarestate:
                        if nxtx != x:
                            return False
                        if self.color == squarestate:
                            return False  # Some common code here - at the end of coding optimize
            elif dx == 0 and dy != 0:
                for squares in range(dy):
                    nxty = self.ypos + (dy / abs(dy)) * (squares + 1)
                    squarestate = self.opensquare(x, nxty)
                    if not squarestate:
                        if nxty != y:
                            return False
                        if self.color == squarestate:
                            return False
        return True

class Queen(Piece):
    def __str__(self):
        superstr = super().__str__()
        output = 'queen \n'
        output = output + superstr
        return output

    def validate(self, x, y):
        if super().validate(x, y):
            dx = x - self.xpos
            dy = y - self.xpos
            pdx = abs(dx)
            pdy = abs(dy)
            if dx != 0 and dy == 0:
                for squares in range(dx):
                    nxtx = self.xpos + (dx / abs(dx)) * (squares + 1)
                    squarestate = self.opensquare(nxtx, y)
                    if not squarestate:
                        if nxtx != x:
                            return False
                        if self.color == squarestate:
                            return False  # Some common code here - at the end of coding optimize
            elif dx == 0 and dy != 0:
                for squares in range(dy):
                    nxty = self.ypos + (dy / abs(dy)) * (squares + 1)
                    squarestate = self.opensquare(x, nxty)
                    if not squarestate:
                        if nxty != y:
                            return False
                        if self.color == squarestate:
                            return False
            elif pdx != pdy:
                return False
            for squares in range(pdx):
                nxtx = self.xpos + (dx / pdx) * (squares + 1)
                nxty = self.ypos + (dy / pdy) * (squares + 1)
                squarestate = self.opensquare(nxtx, nxty)
                if not squarestate:
                    if nxtx != x:
                        return False
                    if self.color == squarestate:
                        return False
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
            dx = x - self.xpos
            dy = y - self.xpos
            pdx = abs(dx)
            pdy = abs(dy)
            if dx != 0 and dy == 0:
                for squares in range(dx):
                    nxtx = self.xpos + (dx / abs(dx)) * (squares + 1)
                    squarestate = self.opensquare(nxtx, y)
                    if not squarestate:
                        if nxtx != x:
                            return False
                        if self.color == squarestate:
                            return False  # Some common code here - at the end of coding optimize
            elif dx == 0 and dy != 0:
                for squares in range(dy):
                    nxty = self.xpos + (dy / abs(dy)) * (squares + 1)
                    squarestate = self.opensquare(x, nxty)
                    if not squarestate:
                        if nxty != y:
                            return False
                        if self.color == squarestate:
                            return False
            elif pdx != pdy:
                return False
            for squares in range(pdx):
                nxtx = self.xpos + (dx / pdx) * (squares + 1)
                nxty = self.ypos + (dy / pdy) * (squares + 1)
                squarestate = self.opensquare(nxtx, nxty)
                if not squarestate:
                    if nxtx != x:
                        return False
                    if self.color == squarestate:
                        return False
        return True

class Pawn(Piece):
    def __str__(self):
        superstr = super().__str__()
        output = 'Pawn \n'
        output = output + superstr
        return output



class King(Piece):
    def __str__(self):
        superstr = super().__str__()
        output = 'King \n'
        output = output + superstr
        return output

    def validate(self, x, y):
        if super().validate(x, y):
            if self.opensquare(x, y):
                pdx = abs(x - self.xpos)
                pdy = abs(y - self.xpos)
                if (pdx == 1 and pdy == 1) or (pdx+pdy == 1):
                    return True
                else:
                    return False




class Knight(Piece):
    def __str__(self):
        superstr = super().__str__()
        output = 'Knight \n'
        output = output + superstr
        return output




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







