# unicUtils.py: helper functions for using unicurses in towers.py

from unicurses import *
import sys

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

# ask the user if they want to see the next hanoi move
def askToCont():
    return chr(getch()) != 'q' # 'q' to quit

def showHanoiState(board):
    stdscr.clear()
    if terminalIsBigEnough():
        displayInstructions()
        renderHanoiState()
    else:
        displayInstructions()

    println(str(board))

def terminalIsBigEnough():
    (numrows, numcols) = getmaxyx(stdscr)
    return numrows < minHeight and numcols < minWidth

def displayInstructions():
    mvaddstr(1,1,"Type 'q' to quit")
    mvaddstr(2,1,"Type 'n' for next move")
def renderHanoiState():
    (numrows, numcols) = getmaxyx(stdscr)
    pegCols = {pegs[i]: (i*2 + 1)*gs for i in range(3)}
