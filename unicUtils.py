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

# The game board, a dictionary.  Keys are pegs.  Values are arrays of rings.
# Rings are implemented just as numbers.
gb = {A: [], B: [], C: []}

# the unicurses running screen object
stdscr

# setup and teardown of Unicurses terminal highjacking
def initCurses():
    global stdscr
    stdscr = initscr()
    stdscr.keypad(1)
    noecho()
    cbreak()
def closeCurses():
    global stdscr
    stdscr.keypad(0)
    echo()
    nocbreak()
    endwin()

# println for unicurses
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
    c = chr(getch()) # keycode
    return  c != 'q' # 'q' to quit

def showHanoiState(board):
    scrRowCol = getmaxyx(stdscr)
    #
    println(str(board))
