# unicUtils.py: helper functions for using unicurses in towers.py

from unicurses import *

# the pegs of the gameboard
A = 'A'
B = 'B'
C = 'C'
pegs = [A,B,C]

# the game size (the number of rings)
gs = 0

# the minimum dimensions of the terminal given the game size
minHeight = 0
minWidth = 0

# the columns of the pegs
pegCols = {peg:0 for peg in pegs}

# The game board, a dictionary.  Keys are pegs.  Values are arrays of rings.
# Rings are implemented just as numbers.
gb = {A: [], B: [], C: []}

# the unicurses running screen object
stdscr

# setup and teardown of Unicurses terminal highjacking
def initCurses():
    global stdscr
    stdscr = initscr()
    noecho()
    cbreak()
def closeCurses():
    global stdscr
    echo()
    nocbreak()
    endwin()

# make an instance of the println function for unicurses
def makePrintln(initRow, initCol):
    def println(s):
        nonlocal initRow
        mvaddstr(initRow, initCol, s)
        initRow += 1
    return println
println = makePrintln(0,0)

def refreshPrintln():
    global println
    println = makePrintln(0,0)

def calcMinNeededDims():
    global minHeight, minWidth
    minHeight = (gs * 2) + 4
    minWidth = (gs * 2) * 3 + 1
def calcPegLocations():
    global pegCols, gs
    pegCols = {pegs[i]: (i*2 + 1)*gs for i in range(3)}
def setGs(gs_p):
    global gs
    gs = gs_p

# ask the user if they want to see the next hanoi move
def askToCont():
    return chr(getch()) != 'q' # 'q' to quit

def showHanoiState(board):
    stdscr.clear()
    if terminalIsBigEnough():
        displayInstructions()
        showPegs()
        renderHanoiState()
    else:
        displayInstructions()
        mvaddstr(3,1, "This terminal is not big enough for the size of game that you entered.")

def displayInstructions():
    mvaddstr(1,1,"Type 'q' to quit")
    mvaddstr(2,1,"Type 'n' for next move")
def showPegs():
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
def terminalIsBigEnough():
    (numrows, numcols) = getmaxyx(stdscr)
    return minHeight < numrows and minWidth < numcols
