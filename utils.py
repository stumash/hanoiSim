# utils.py: helper functions for using unicurses in towers.py

from unicurses import *

# global vars
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

# println for unicurses
def makePrintln(initRow, initCol):
    def println(s):
        mvaddstr(initRow, initCol, s)
        initRow += 1

    return println
println = makePrintln(0,0)
