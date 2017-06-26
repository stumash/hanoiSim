# towers.py: a program that
# beats a game of Towers of Hano

# imports
from unicUtils import *

def main():
    # get-input-loop
    while True:
        try:
            gs = int(input("How tall should this Towers of Hanoi be? "))
            if (gs <= 0 or gs % 1 != 0 or gs >= 10): # if neg or float
                raise ValueError

            break
        except ValueError:
            print("Must input a positive integer under 10.")

    # initizialize the first peg of the game board
    gb[A] = [x for x in list(reversed(range(1, gs+1)))]

    # calculate the minimum terminal dimensions required
    global minHeight, minWidth
    minHeight = (gs * 2) + 4
    minWidth = (gs * 2) * 3 + 1

    # calculate the columns of the pegs
    global pegCols
    pegCols = {pegs[i]: (i*2 + 1)*gs for i in range(3)}

    # some initial printing
    print("initial state: " + str(gb))

    # initialize curses
    initCurses()

    showHanoiState(gb) # see initial gameboard state
    doHanoiMove(gs, A, C) # RUN HANOI

    if (gb[A] == [] and gb[B] == []): # if done
        askToCont() # see final gameboard state

    # shutdown curses
    closeCurses()

    # some final printing
    print("final state: " + str(gb))
    return 0

# helper functions for the doHanoiMove function
def otherPeg(fromPeg, toPeg): # given 2 of the 3 pegs, return the 3rd
    for peg in pegs:
        if peg not in [fromPeg, toPeg]:
            return peg
def moveRing(fromPeg, toPeg): # on the game board gb, move a ring from fromPeg to toPeg
    ring = gb[fromPeg].pop()
    gb[toPeg].append(ring)

# the recursive hanoi function
userChoseExit = False
def doHanoiMove(ringNum, fromPeg, toPeg):
    global userChoseExit

    if (ringNum == 1):
        if (userChoseExit or not askToCont()):
            userChoseExit = True
            return

        moveRing(fromPeg, toPeg)
        showHanoiState(gb)

    else:
        intermediatePeg = otherPeg(fromPeg, toPeg)

        doHanoiMove(ringNum-1, fromPeg, intermediatePeg)

        if (userChoseExit or not askToCont()):
            userChoseExit = True
            return

        moveRing(fromPeg, toPeg)
        showHanoiState(gb)

        doHanoiMove(ringNum-1, intermediatePeg, toPeg)

if __name__ == "__main__":
    main()
