# towers.py: a program that
# beats a game of Towers of Hano

# imports
from hanoi_board import HanoiBoard

def main():

    f = open("debugOutput.txt", "w")

    # string constants
    NUM_RINGS_ASK = "How tall should this Towers of Hanoi be? "
    BAD_INP_TYPE_MSG = "Must input positive integer."

    # initialize the hanoi board object
    b = HanoiBoard()

    # get-input-loop
    while True:
        try:
            b.towerHeight = int(input(NUM_RINGS_ASK))
            th = b.towerHeight
            # non positive or float not allowed
            if (th <= 0 or th % 1 != 0):
                raise ValueError
            break
        except ValueError:
            print(BAD_INP_TYPE_MSG)

    # initizialize peg A of the hanoi board to hold the stack of all rings
    b.board[b.pegA] = [x for x in list(reversed(range(1, b.towerHeight + 1)))]

    # initialize curses
    b.initCurses()
    b.calcMinNeededDims()
    b.calcPegLocations()

    # some initial printing
    f.write("initial state: " + str(b.board) + "\n")

    b.displayHanoiState() # see initial game state
    doHanoiMove(f, b, b.towerHeight, b.pegA, b.pegC) # RUN HANOI

    b.getChar()

    # shutdown curses
    b.closeCurses()

    # some final printing
    print("final state: " + str(b.towerHeight))
    return 0


# the recursive hanoi function
def doHanoiMove(f, b, ring, fromPeg, toPeg):

    # base case (smallest ring)
    if (ring == 1):

        if b.askUserIfContinue():
            # smallest ring never has tower above
            f.write("s\n")
            f.write("before " + str(b.board) + "\n")
            b.moveRing(fromPeg, toPeg)
            f.write("after " + str(b.board) + "\n")
            b.displayHanoiState()
            f.write("after  " + str(b.board) + "\n")
            f.write("e\n")
        else:
            return # recurse the hell outta there

    # all other rings
    else:
        intermediatePeg = b.otherPeg(fromPeg, toPeg)

        # move tower above to intermediate peg
        doHanoiMove(f, b, ring-1, fromPeg, intermediatePeg)

        if b.askUserIfContinue():
            f.write("s\n")
            f.write("before" + str(b.board) + "\n")
            b.moveRing(fromPeg, toPeg)
            f.write("after  " + str(b.board) + "\n")
            b.displayHanoiState()
            f.write("after  " + str(b.board) + "\n")
            f.write("e\n")
        else:
            return # recurse the hell outta there

        # move tower back on top
        doHanoiMove(f, b, ring-1, intermediatePeg, toPeg)

if __name__ == "__main__":
    main()
