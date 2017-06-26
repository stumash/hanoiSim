# towers.py: a program that
# beats a game of Towers of Hano

# imports
from unicUtils import *

def main():
    # get the game size
    while True:
        try:
            gs = int(input("How tall should this Towers of Hanoi be? "))
            break
        except ValueError:
            print("Must input a positive integer under 10.")

    gb[A] = [x for x in list(reversed(range(1, gs+1)))]

    print("initial state: " + str(gb))

    initCurses()

    showHanoiState(gb)
    doHanoiMove(gs, A, C)

    if (gb[A] == [] and gb[B] == []):
        askToCont()

    closeCurses()

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
