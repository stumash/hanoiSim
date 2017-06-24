# towers.py: a program that
# beats a game of Towers of Hano

# imports
from utils import *

# The 3 pegs of the Towers of Hanoi game board
A = 'A'
B = 'B'
C = 'C'
pegs = [A, B, C]

# helper functions for the doHanoiMove function
def otherPeg(fromPeg, toPeg): # given 2 of the 3 pegs, return the 3rd
    for peg in pegs:
        if peg not in [fromPeg, toPeg]:
            return peg
def moveRing(fromPeg, toPeg): # on the game board gb, move a ring from fromPeg to toPeg
    ring = gb[fromPeg].pop()
    gb[toPeg].append(ring)

# dat recursive glory
def doHanoiMove(d, fromPeg, toPeg):
    if (d == 0):
        println(str(gb[fromPeg][-1]) + " from " + fromPeg + " to " + toPeg)

        moveRing(fromPeg, toPeg)
    else:
        intermediatePeg = otherPeg(fromPeg, toPeg)
        doHanoiMove(d-1, fromPeg, intermediatePeg)

        println(str(gb[fromPeg][-1]) + " from " + fromPeg + " to " + toPeg)

        moveRing(fromPeg, toPeg)

        doHanoiMove(d-1, intermediatePeg, toPeg)


## main method:

initCurses()

gs = 5
# The game board, a dictionary.  Keys are pegs.  Values are arrays of rings.
# Rings are implemented just as numbers.
gb = {'A': list([x for x in list(reversed(range(gs)))]), 'B': [], 'C': []}

doHanoiMove(gs-1, A, C) 

closeCurses()

print(gb)
