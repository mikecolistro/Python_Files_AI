import random
# Prints the board in a pretty format.
# Input: Board.
# Output: None.
def printBoard(b):
    for r in range(3):
        print "[", b[r][0], b[r][1], b[r][2], "]"

# Returns the other player.
# Input: Player "O" or "X".
# Output: Other player.
def otherPlayer(p):
    if p == "O":
        return "X"
    else:
        return "O"

# Detects whether a given player has won the game.
# Input: Board. Player "O" or "X".
# Output: Boolean.
def hasWon(b,p):
    i = 0
    j = 0
    for i in range(2):
        if b[i][0] == p and b[i][1] == p and b[i][2] == p:
            return True
    for j in range(2):
        if b[0][j] == p and b[1][j] == p and b[2][j] == p:
            return True
    if b[0][0] == p and b[1][1 ]== p and b[2][2] == p:
        return True
 #   print(b[0][2]+b[1][1]+b[2][0])
    if b[0][2] == p and b[1][1] == p and b[2][0] == p:
        return True
    return False

# Selects the next move for the given player.
# Input: Board. Player "O" or "X".
# Output: Pair of 0, 1, or 2, indicating space in which to move, or None.
def move(b, p):
    counter = 0
    o = otherPlayer(p)
    randomFlag = True
    print("Player " + p)
    print("Checking to see if we can win")
    #check to see if we can win
    val = checkWin(b,p)

    if val == None:
        #check loss
        val = checkWin(b,o)
    else:
        return val

    if val != None:
        return val
    num1 = 0
    num2 = 0
    for num1 in range(3):
        for num2 in range(3):
            if b[num1][num2] != " ":
                counter = counter + 1

    if (counter == 3 and b[0][0] == o and b[2][2] == o) or (counter == 3 and b[0][2] == o and b[2][0] == o) :
        if b[1][0] == " ":
            return [1, 0]
        elif b[1][2] == " ":
            return [1, 2]
        else:
            counter += 1

    if b[1][1] == " ":
        return [1, 1]
    if b[0][2] == " ":
        return [0, 2]
    if b[0][0] == " ":
        return [0,0]
    if b[2][0] == " ":
        return [2, 0]
    if b[2][2] == " ":
        return [2,2]

    print("Getting random spot")
    while randomFlag:
        row = random.randint(0,2)
        col = random.randint(0,2)
        if b[row][col] == " ":
            return [row, col]

def checkWin(b , p):
    o = otherPlayer(p)
    if b[0][0] == p and b[0][1] == p and b[0][2] != o:
        return [0, 2]
    if b[0][0] == p and b[0][2] == p and b[0][1] != o:
        return [0, 1]
    if b[0][1] == p and b[0][2] == p and b[0][0] != o:
        return [0,0]
    if b[1][0] == p and b[1][1] == p and b[1][2] != o:
        return [1, 2]
    if b[1][0] == p and b[1][2] == p and b[1][1] != o:
        return [1, 1]
    if b[1][1] == p and b[1][2] == p and b[1][0] != o:
        return [1,0]
    if b[2][0] == p and b[2][1] == p and b[2][2] != o:
        return [2, 2]
    if b[2][0] == p and b[2][2] == p and b[2][1] != o:
        return [2, 1]
    if b[2][1] == p and b[2][2] == p and b[2][0] != o:
        return [2,0]
    if b[0][0] == p and b[1][0] == p and b[2][0] != o:
        return [2, 0]
    if b[0][0] == p and b[2][0] == p and b[1][0] != o:
        return [1, 0]
    if b[1][0] == p and b[2][0] == p and b[0][0] != o:
        return [0, 0]
    if b[0][1] == p and b[1][1] == p and b[2][1] != o:
        return [2, 1]
    if b[0][1] == p and b[2][1] == p and b[1][1] != o:
        return [1, 1]
    if b[1][1] == p and b[2][1] == p and b[0][1] != o:
        return [0, 1]
    if b[0][2] == p and b[1][2] == p and b[2][2] != o:
        return [2, 2]
    if b[0][2] == p and b[2][2] == p and b[1][2] != o:
        return [1, 2]
    if b[1][2] == p and b[2][2] == p and b[0][2] != o:
        return [0, 2]
    if b[0][0] == p and b[1][1] == p and b[2][2] != o:
        return [2,2]
    if b[0][0] == p and b[2][2] == p and b[1][1] != o:
        return [1,1]
    if b[2][2] == p and b[1][1] == p and b[0][0] != o:
        return [0,0]
    else:
        None

def checkLoss(b , p):
    o = otherPlayer(p)
    #check to see if we can lose
    if b[0][0] == o and b[0][1] == o and b[0][2] != p:
        return [0, 2]
    if b[0][0] == o and b[0][2] == o and b[0][1] != p:
        return [0, 1]
    if b[0][1] == o and b[0][2] == o and b[0][0] != p:
        return [0,0]
    if b[1][0] == o and b[1][1] == o and b[1][2] != p:
        return [1, 2]
    if b[1][0] == o and b[1][2] == o and b[1][2] != p:
        return [1, 2]
    if b[1][1] == o and b[1][2] == o and b[1][0] != p:
        return [1,0]
    if b[2][0] == o and b[2][1] == o and b[2][2] != p:
        return [2, 2]
    if b[2][0] == o and b[2][2] == o and b[2][1] != p:
        return [2, 1]
    if b[2][1] == o and b[2][2] == o and b[2][0] != p:
        return [2,0]
    if b[0][0] == o and b[1][0] == o and b[2][0] != p:
        return [2, 0]
    if b[0][0] == o and b[2][0] == o and b[1][0] != p:
        return [1, 0]
    if b[1][0] == o and b[2][0] == o and b[0][0] != p:
        return [0, 0]
    if b[0][1] == o and b[1][1] == o and b[2][1] != p:
        return [2, 1]
    if b[0][1] == o and b[2][1] == o and b[1][1] != p:
        return [1, 1]
    if b[1][1] == o and b[2][1] == o and b[0][1] != p:
        return [0, 1]
    if b[0][2] == o and b[1][2] == o and b[2][2] != p:
        return [2, 2]
    if b[0][2] == o and b[2][2] == o and b[1][2] != p:
        return [1, 2]
    if b[1][2] == o and b[2][2] == o and b[0][2] != p:
        return [0, 2]
    if b[0][0] == o and b[1][1] == o and b[2][2] != p:
        return [2,2]
    if b[0][0] == o and b[2][2] == o and b[1][1] != p:
        return [1,1]
    if b[2][2] == o and b[1][1] == o and b[0][0] != p:
        return [0,0]
    else:
        return None

# Plays the computer against itself.
# Input: None.
# Output: None.
def computerVsComputer():
    # Initialize the game.
    board = [[" ", " " ," "], [" ", " " ," "], [" ", " " ," "]]
    player = "O"
    turns = 0
    printBoard(board)
    # Run the game.
    while turns < 9 and not hasWon(board, "X") and not hasWon(board, "O"):
        m = move(board, player)
        if m == None or board[m[0]][m[1]] != " ":
            print "Invalid move", m, "by player", player, "on this board:"
            printBoard(board)
            return
        board[m[0]][m[1]] = player
        print
        printBoard(board)
        player = otherPlayer(player)
        turns = turns + 1
    # Finish the game.
    if hasWon(board, "O"):
        print "O wins."
    elif hasWon(board, "X"):
        print "X wins."
    else:
        print "Draw."

# If the user ran this file directly, then this code will be executed.
# If the user imported this file, then this code will not be executed.
if __name__ == "__main__":
    computerVsComputer()


