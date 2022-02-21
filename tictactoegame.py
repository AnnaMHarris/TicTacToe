from random import randint

a = " "
b = " "
c = " "
d = " "
e = " "
f = " "
g = " "
h = " "
i = " "
yourCharacter = ' '
computerCharacter = ' '
youWin = False
computerWin = False
wantToPlay = True


def columnLine():
    print("\t     |     |")

def rowLine():
    print('\t_____|_____|_____')

#the tic tac toe board used to play on
def print_tic_tac_toe():
    print("\n")
    columnLine()
    print("\t  " + a + "  |  " + b + "  |  "+ c + "  ")
    rowLine()
    columnLine()
    print("\t  " + d + "  |  " + e + "  |  " + f + "  ")
    rowLine()
    columnLine()
    print("\t  " + g + "  |  " + h + "  |  " + i + "  ")
    columnLine()
    print("\n")

#the tic tac toe board used as reference
def print_example_tic_tac_toe():
    print("\n")
    columnLine()
    print("\t  1  |  2  |  3  ")
    rowLine()
    columnLine()
    print("\t  4  |  5  |  6  ")
    rowLine()
    columnLine()
    print("\t  7  |  8  |  9  ")
    columnLine()
    print("\n")

def yourMove():
    global yourCharacter
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i
    yourError = 1
    while (yourError == 1):
        try:
            block = int(input("Which block?"))
        except ValueError:
            print("Sorry that's not a valid entry.  Please try again.")
            continue
        if block == 1:
            if a == " ":
                a = yourCharacter
                yourError = 0
            else:
                print("Sorry that block is taken.  Please try again.")
                yourError = 1
        elif block == 2:
            if b == " ":
                b = yourCharacter
                yourError = 0
            else:
                print("Sorry that block is taken.  Please try again.")
                yourError = 1
        elif block == 3:
            if c == " ":
                c = yourCharacter
                yourError = 0
            else:
                print("Sorry that block is taken.  Please try again.")
                yourError = 1
        elif block == 4:
            if d == " ":
                d = yourCharacter
                yourError = 0
            else:
                print("Sorry that block is taken.  Please try again.")
                yourError = 1
        elif block == 5:
            if e == " ":
                e = yourCharacter
                yourError = 0
            else:
                print("Sorry that block is taken.  Please try again.")
                yourError = 1
        elif block == 6:
            if f == " ":
                f = yourCharacter
                yourError = 0
            else:
                print("Sorry that block is taken.  Please try again.")
                yourError = 1
        elif block == 7:
            if g == " ":
                g = yourCharacter
                yourError = 0
            else:
                print("Sorry that block is taken.  Please try again.")
                yourError = 1
        elif block == 8:
            if h == " ":
                h = yourCharacter
                yourError = 0
            else:
                print("Sorry that block is taken.  Please try again.")
                yourError = 1
        elif block == 9:
            if i == " ":
                i = yourCharacter
                yourError = 0
            else:
                print("Sorry that block is taken.  Please try again.")
                yourError = 1
        else:
            print("Sorry that's not a valid block number")
            yourError = 1

def askForCharacter():
    global yourCharacter
    yourCharacter = str(input("Would you like to be x or o?"))

#checks that the user entered either x or o
def checkCharacter():
    global yourCharacter
    global computerCharacter
    while yourCharacter.lower() not in ['x', 'o']:
        print("This is not a valid character.  Please try again")
        askForCharacter()
    else:
        print("Okay")
    if yourCharacter == "x":
        computerCharacter = "o"
    elif yourCharacter == "o":
        computerCharacter = "x"

def computerMove():
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i
    global computerCharacter
    passthru = 0
    computerError = 1
    while computerError == 1:
        computerChoice = randint(1, 9)
        if computerChoice == 1:
            if a == " ":
                a = computerCharacter
                computerError = 0
            else:
                computerError = 1
        elif computerChoice == 2:
            if b == " ":
                b = computerCharacter
                computerError = 0
            else:
                computerError = 1
        elif computerChoice == 3:
            if c == " ":
                c = computerCharacter
                computerError = 0
            else:
                computerError = 1
        elif computerChoice == 4:
            if d == " ":
                d = computerCharacter
                computerError = 0
            else:
                computerError = 1
        elif computerChoice == 5:
            if e == " ":
                e = computerCharacter
                computerError = 0
            else:
                computerError = 1
        elif computerChoice == 6:
            if f == " ":
                f = computerCharacter
                computerError = 0
            else:
                computerError = 1
        elif computerChoice == 7:
            if g == " ":
                g = computerCharacter
                computerError = 0
            else:
                computerError = 1
        elif computerChoice == 8:
            if h == " ":
                h = computerCharacter
                computerError = 0
            else:
                computerError = 1
        elif computerChoice == 9:
            if i == " ":
                i = computerCharacter
                computerError = 0
            else:
                computerError = 1


def checkIfWon():
    global yourCharacter
    global computerCharacter
    global youWin
    global computerWin
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i
    if a == computerCharacter:
        if b == computerCharacter:
            if c == computerCharacter:
                computerWin = True
    if a == yourCharacter:
        if b == yourCharacter:
            if c == yourCharacter:
                youWin = True
    if a == computerCharacter:
        if e == computerCharacter:
            if i == computerCharacter:
                computerWin = True
    if a == yourCharacter:
        if e == yourCharacter:
            if i == yourCharacter:
                youWin = True
    if g == computerCharacter:
        if e == computerCharacter:
            if c == computerCharacter:
                computerWin = True
    if g == yourCharacter:
        if e == yourCharacter:
            if c == yourCharacter:
                youWin = True
    if a == computerCharacter:
        if d == computerCharacter:
            if g == computerCharacter:
                computerWin = True
    if a == yourCharacter:
        if d == yourCharacter:
            if g == yourCharacter:
                youWin = True
    if g == computerCharacter:
        if h == computerCharacter:
            if i == computerCharacter:
                computerWin = True
    if g == yourCharacter:
        if h == yourCharacter:
            if i == yourCharacter:
                youWin = True
    if c == computerCharacter:
        if f == computerCharacter:
            if i == computerCharacter:
                computerWin = True
    if c == yourCharacter:
        if f == yourCharacter:
            if i == yourCharacter:
                youWin = True
    if d == computerCharacter:
        if e == computerCharacter:
            if f == computerCharacter:
                computerWin = True
    if d == yourCharacter:
        if e == yourCharacter:
            if f == yourCharacter:
                youWin = True

#calls functions to print the board, prompt the moves, and determine who won
def Game():
    global youWin
    global computerWin

    print_tic_tac_toe()
    print("Refer to the below chart for the number that corresponds to the box\n")
    print_example_tic_tac_toe()

    askForCharacter()
    checkCharacter()
    while computerWin == False & youWin == False:
        checkIfWon()
        yourMove()
        print_tic_tac_toe()
        checkIfWon()
        computerMove()
        print_tic_tac_toe()
        if youWin | computerWin:
            break
    if computerWin:
        print("You lose")
    elif youWin:
        print("You win")

def playAgain():
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i
    global youWin
    global computerWin
    global wantToPlay
    repeatGame = str(input("Would you like to play again? y or n?"))
    while repeatGame not in ['n', 'y']:
        print("Sorry that's not a valid entry.  Please try again.")
        repeatGame = str(input("Would you like to play again? y or n?"))
    if repeatGame == "y":
        a = " "
        b = " "
        c = " "
        d = " "
        e = " "
        f = " "
        g = " "
        h = " "
        i = " "
        youWin = False
        computerWin = False
    else:
        wantToPlay = False

def main():
    global wantToPlay
    while wantToPlay == True:
        Game()
        playAgain()
    else:
        exit

main()
