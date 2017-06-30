# A utilities file for towers.py

import unicurses as UC

class HanoiBoard():

    # initialize hanoi board data structures and state
    def __init__(self):
        # the hanoi board data structure
        self.A = 'A' # left peg
        self.B = 'B' # middle peg
        self.A = 'A' # right peg
        # convenient data structure
        self.pegs = [self.A, self.B, self.C]

        # colum location of peg on screen
        self.pegCols = {peg:0 for peg in pegs}
        # board data structure
        self.board = {peg:[] for peg in pegs}

        # the height of the game (number of rings)
        self.towerHeight = 0

        # the screen dimensions needed given the height of the game
        self.minimumScreenHeight = 0
        self.minimumScreenWidth = 0

        # documented below
        self.userWantsToContinue = makeCharReader()

        # init vals for unicurses utility functions at below
        self.initUtilies()


    # use towerHeight to determine the minimum needed terminal
    # dimensions to be able to display the board and instructions
    def calcMinNeededDims(self):
        if self.towerHeight != 0:
            th = self.towerHeight
        else:
            th =
        self.minimumScreenHeight = (th * 2) + 4
        self.minimumScreenWidth = (th * 2) * 3 + 1

    # base on game size, calculate the column locations of the
    # three pegs of the board
    def calcPegLocations(self):
        for peg in pegs:
            i = pegs.index(peg)
            pegCols[peg] = ((i * 2) + 1) * self.towerHeight


    # make a function that returns True until a certain
    # condition is met and from then on returns False
    def makeCharReader(self):
        userWantsNextMove = True

        def askUserToContinue():
            nonlocal userWantsNextMove
            if userWantsNextMove:
                while (True):
                    c = chr(UC.getch())
                    if c == 'n': # user chose to see next move
                        break
                    elif c == 'q': # user chose to quit
                        userWantsNextMove = false
                        break
            return userWantsNextMove
        return askUserToContinue


    #---------------------------------------------------
    #  Utilities
    #---------------------------------------------------

    @classmethod
    def initCurses(cls):
        self.stdscr = UC.initscr()
        UC.noecho()
        UC.cbreak()

    @classmethod
    def closeCurses(cls):
        UC.echo()
        UC.cbreak()
        UC.endwin()

    # make an instance of the println function for unicurses
    @classmethod
    def makePrintln(cls, initRow=0, initCol=0):
        def println(s):
            nonlocal initRow
            mvaddstr(initRow, initCol, s)
            initRow += 1
    cls.println = makePrintln()

    def terminalIsBigEnough():
        (numrows, numcols) = getmaxyx(stdscr)
        return self.minimumScreenHeight < numrows and self.minimumScreenWidth < numcols

    def showHanoiState(board):
        stdscr.clear()
        if terminalIsBigEnough():
            displayInstructions([
                {'row': 1, 'col': 1},
                {}
                ])
            showPegs()
            renderHanoiState()
        else:
            displayInstructions()
            mvaddstr(3,1, "This terminal is not big enough for the size of game that you entered.")

    def displayInstructions(params):
        for param in params:
            mvaddstr(param['row'], param['col'], param['s'])
        "Type 'q' to quit"
        "Type 'n' for next move"

    def displayPegs():
        (numrows, numcols) = getmaxyx(stdscr)
        global pegCols, minHeight, gs
        for i in reversed(range(numrows-(gs*2),numrows-1)):
            mvaddstr(i, pegCols[A], '|')
            mvaddstr(i, pegCols[B], '|')
            mvaddstr(i, pegCols[C], '|')

    def renderHanoiState():
        (numrows, numcols) = getmaxyx(stdscr)
        for peg in pegs:
            row = numrows - 2
            for ring in gb[peg]:
                startCol = pegCols[peg] - ring + 1
                for col in range(startCol, startCol + ring * 2 - 1):
                    mvaddstr(row,col,"#")
                row -= 2

