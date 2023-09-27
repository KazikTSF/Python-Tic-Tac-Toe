def rules():
    print("Below you have grid with corresponding numbers\n"
          "You can choose any of this numbers to draw your symbol on it")
    start = ' 0 | 1 | 2 \n-----------\n 3 | 4 | 5 \n-----------\n 6 | 7 | 8 \n'
    print(start)


def checkInput(userInput: str) -> bool:
    if userInput == '0' and board[0] == ' ':
        return True
    elif userInput == '1' and board[1] == ' ':
        return True
    elif userInput == '2' and board[2] == ' ':
        return True
    elif userInput == '3' and board[3] == ' ':
        return True
    elif userInput == '4' and board[4] == ' ':
        return True
    elif userInput == '5' and board[5] == ' ':
        return True
    elif userInput == '6' and board[6] == ' ':
        return True
    elif userInput == '7' and board[7] == ' ':
        return True
    elif userInput == '8' and board[8] == ' ':
        return True
    else:
        print("Incorrect input")
        return False


def checkWinner() -> bool:
    for i in range(0, 6, 3):
        if board[i] == symbol and board[i + 1] == symbol and board[i + 1] == symbol:
            return True
    for i in range(0, 3):
        if board[i] == symbol and board[i + 3] == symbol and board[i + 6] == symbol:
            return True
    if board[0] == symbol and board[4] == symbol and board[8] == symbol:
        return True
    if board[2] == symbol and board[4] == symbol and board[6] == symbol:
        return True
    return False


def move(choice: int) -> str:
    board[choice] = symbol
    if checkWinner():
        return symbol
    tieCheck = 0
    for i in range(9):
        if board[i] == 'x' or board[i] == 'o':
            tieCheck += 1
    if tieCheck == 9:
        return "No one"
    return ' '


def drawBoard():
    b = ' {0} | {1} | {2} \n-----------\n {3} | {4} | {5} \n-----------\n {6} | {7} | {8} \n'
    print(b.format(*board))


rules()
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
winner = ' '
symbol = ' '
while winner == ' ':
    if symbol == 'x':
        symbol = 'o'
    else:
        symbol = 'x'
    correct = False
    s = ''
    while not correct:
        s = input("Choose a number to draw your symbol into: ")
        correct = checkInput(s)
    winner = move(int(s))
    drawBoard()

print("%s wins!" % symbol)
