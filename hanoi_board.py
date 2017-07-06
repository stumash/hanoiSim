from unicurses import *

class HanoiBoard():

    def __init__(self):

        #-------------
        #  string constants
        #-------------

        self.INSTRCTN_QUIT = "Type 'q' to quit"
        self.INSTRCTN_NEXT = "Type 'n' for next move"
        self.WARNING_MESSAGE = "SCREEN TOO SMALL"

        #-------------
        #  the board
        #-------------

        self.pegA = 'A' # left peg
        self.pegB = 'B' # middle peg
        self.pegC = 'C' # right peg

        # convenient data structure
        self.pegs = [self.pegA, self.pegB, self.pegC]

        # colum location of peg on screen, 0 for now
        self.pegCols = {peg:0 for peg in self.pegs}
        # board data structure, empty pegs for now
        self.board = {peg:[] for peg in self.pegs}

        # the number of rings in the game, 0 for now
        self.towerHeight = 0

        #-------------------------------------------------------------
        #  functions needing initialization/having internal state
        #-------------------------------------------------------------

        # asks user if continue. once user says no, never ask again
        self.askUserIfContinue = self.makeUserActionAsker()

        # prints in unicurses, new line for each print
        self.println = self.makePrintln()


    #---------------------------------------------------
    #  utilities
    #---------------------------------------------------

    def initCurses(self):
        self.stdscr = initscr()
        noecho()
        cbreak()

    def closeCurses(self):
        echo()
        cbreak()
        endwin()

    # make a function that returns True until the user
    # types 'n' or 'q', and then only returns False
    def makeUserActionAsker(self):
        userWantsNextMove = True

        def askUserToContinue():
            nonlocal userWantsNextMove
            if userWantsNextMove:
                while (True):
                    c = chr(getch())
                    if c == 'n': # user chose to see next move
                        break
                    elif c == 'q': # user chose to quit
                        userWantsNextMove = false
                        break
            return userWantsNextMove
        return askUserToContinue

    # make an instance of the println function for unicurses
    def makePrintln(self, initRow=0, initCol=0):
        def println(s):
            nonlocal initRow, initCol
            mvaddstr(initRow, initCol, s)
            initRow += 1 # print on the next line next time
        return println

    # base on game size, calculate the column locations of the
    # three pegs of the board
    def calcPegLocations(self, th = None):
        if (th == None):
            th = self.towerHeight
        for (i,peg) in enumerate(self.pegs):
            self.pegCols[peg] = ((i * 2) + 1) * th

    # use towerHeight to determine the minimum needed terminal
    # dimensions to be able to display the board and instructions
    def calcMinNeededDims(self, th = None):
        if (th == None):
            th = self.towerHeight
        self.minScreenHeight = (th * 2) + 4
        self.minScreenWidth= (th * 2) * 3 + 1

    # determine if terminal is big enough given tower height
    def terminalIsTallEnough(self):
        (numrows, numcols) = getmaxyx(self.stdscr)
        return self.minScreenHeight < numrows
    def terminalIsWideEnough(self):
        (numrows, numcols) = getmaxyx(self.stdscr)
        return self.minScreenWidth < numcols

    # high level function to make all animation appear on screen
    def displayGame(self):
        self.stdscr.clear()
        if self.terminalIsWideEnough():
            self.displayInstructions()
            if self.terminalIsTallEnough():
                self.displayPegs()
                self.renderHanoiState()
            else:
                self.displayWarningMessage()
        else: # Uh oh
            mvaddstr(0,0,'!')

    def displayInstructions(self):
        quitMsg, nextMsg = self.INSTRCTN_QUIT, self.INSTRCTN_NEXT
        mvaddstr(1, 1, quitMsg)
        mvaddstr(2, 1, nextMsg)
    def displayWarningMessage(self):
        warningMsg = self.WARNING_MESSAGE
        mvaddstr(3, 1, warningMsg)

    def displayPegs(self):
        (numrows, numcols) = getmaxyx(self.stdscr)
        pegCols, th = self.pegCols, self.towerHeight
        for i in reversed(range(numrows-(th*2),numrows-1)):
            for peg in self.pegs:
                mvaddstr(i, pegCols[peg], '|')

    def renderHanoiState(self):
        (numrows, numcols) = getmaxyx(self.stdscr)
        for peg in self.pegs:
            row = numrows - 2
            for ring in self.board[peg]:
                startCol = self.pegCols[peg] - ring + 1
                for col in range(startCol, startCol + ring * 2 - 1):
                    mvaddstr(row,col,"#")
                row -= 2

    # helper functions for the doHanoiMove function
    def otherPeg(self, fromPeg, toPeg): # given 2 of the 3 pegs, return the 3rd
        for peg in self.pegs:
            if peg not in [fromPeg, toPeg]:
                return peg
    # on the game board, move a ring from fromPeg to toPeg
    def moveRing(self, fromPeg, toPeg):
        ring = self.board[fromPeg].pop()
        self.board[toPeg].append(ring)

    def getChar(self):
        getch()

