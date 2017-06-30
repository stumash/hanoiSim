# towers.py: a program that
# beats a game of Towers of Hano

# imports
from unicUtils import HanoiBoard 

class UnreasonableInputError(ValueError):
    pass

def main():

    # string constants
    NUM_RINGS_ASK = "How tall should this Towers of Hanoi be?"
    BAD_INP_TYPE_MSG = 'Must input positive integer.'
    INP_TOO_LARGE_MSG = 'Input too big for screen size.'

    # the board object
    b = HanoiBoard()

    # get-input-loop
    while True:
        try:
            b.towerHeight = int(input(NUM_RINGS_ASK))

            th = b.towerHeight
            if (th <= 0 or th % 1 != 0):
                raise ValueError
            elif (): # th is too big
                raise UnreasonableInputError

            break # break the while-loop
        except UnreasonableInputError:
            print(INP_TOO_LARGE_MSG)
        except ValueError:
            print(BAD_INP_TYPE)


    # initizialize peg A of the hanoi board
    b.board[b.A] = [x for x in list(reversed(range(1, gs+1)))]

    b.calcMinNeededDims()
    b.calcPegLocations()

    # some initial printing
    print("initial state: " + str(gb))

    # initialize curses
    mucu.initCurses()

    showHanoiState(gb) # see initial gameb state
    doHanoiMove(gs, A, C) # RUN HANOI

    if (gb[A] == [] and gb[B] == []): # if done
        askToCont() # see final gameb state

    # shutdown curses
    mucu.closeCurses()

    # some final printing
    print("final state: " + str(gb))
    return 0

# helper functions for the doHanoiMove function
def otherPeg(fromPeg, toPeg): # given 2 of the 3 pegs, return the 3rd
    for peg in pegs:
        if peg not in [fromPeg, toPeg]:
            return peg
def moveRing(fromPeg, toPeg): # on the game b gb, move a ring from fromPeg to toPeg
    ring = gb[fromPeg].pop()
    gb[toPeg].append(ring)

# the recursive hanoi function
userChoseExit = False
def doHanoiMove(ringNum, fromPeg, toPeg):
    global userChoseExit

    # base case (smallest ring)
    if (ringNum == 1):
        if (userChoseExit or not askToCont()):
            return # let's recurse the hell outta here!
            userChoseExit = True

        # smallest ring never has tower above
        moveRing(fromPeg, toPeg)
        showHanoiState(gb)

    # all other rings
    else:
        intermediatePeg = otherPeg(fromPeg, toPeg)

        # move tower above to intermediate peg
        doHanoiMove(ringNum-1, fromPeg, intermediatePeg)

        if (userChoseExit or not askToCont()):
            return # let's recurse the hell outta here!
            userChoseExit = True

        # move to open peg
        moveRing(fromPeg, toPeg)
        showHanoiState(gb)

        # move tower back on top
        doHanoiMove(ringNum-1, intermediatePeg, toPeg)


if __name__ == "__main__":
    main()
