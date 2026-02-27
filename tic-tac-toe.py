import random

board = [["*", "*", "*"],
         ["*", "*", "*"],
         ["*", "*", "*"]]
n = random.randint(1, 2)
cnt = 0
ai = 'O' if n == 1 else 'X'
human = 'X' if n == 1 else 'O'


def aimove(who):
    global ai
    flag = False
    q = [0, 0, 0]
    for i in range(3):
        for j in board[i]:
            if j == who:
                q[i] += 1
            elif j != '*':
                q[i] = 0
                break

    for i in range(3):
        if q[i] == 2:
            flag = True
            for j in range(3):
                if board[i][j] == '*':
                    board[i][j] = ai
                    break
        if flag:
            break
    if flag:
        return(flag)

    q = [board[0][0], board[1][1], board[2][2]]
    s = 0
    for i in q:
        if i == who:
            s += 1
    if s == 2:
        for i in range(3):
            if q[i] == '*':
                board[i][i] = ai
                flag = True
                break
    if flag:
        return(flag)

    q = [board[0][2], board[1][1], board[2][0]]
    s = 0
    for i in q:
        if i == who:
            s += 1
    if s == 2:
        flag = True
        if q[0] == '*':
            board[0][2] = ai
        elif q[1] == '*':
            board[1][2] = ai
        else:
            board[2][0] = ai
    if flag:
        return(flag)

    while True:
        f = random.randint(0, 2)
        s = random.randint(0, 2)
        if board[f][s] == '*':
            board[f][s] = ai
            return True


def printBoard():
    for i in range(3):
        print(*board[i])


def draw():
    flag = True
    for i in board:
        for j in i:
            if j == '*':
                flag = False
    return flag


def move(row, col):
    if n == 2 and choise == 2:
        if aimove(human):
            return
        aimove(ai)
        return

    who = 'X' if cnt % 2 != 0 else 'O'
    if board[row][col] == "*":
        board[row][col] = who
    else:
        return ("Invalid move")


def whowin():
    flag = False
    q = None
    for i in board:
        if (i[0] == 'X' and i[1] == 'X' and i[2] == 'X') or (i[0] == 'O' and i[1] == 'O' and i[2] == 'O'):
            flag = True
            q = i[0]
    s = [board[0][0], board[1][1], board[2][2]]
    if s[0] == s[1] == s[2] != "*":
        flag = True
        q = s[0]
    if q != None:
       return q
    ss = [board[0][2], board[1][1], board[2][0]]
    if ss[0] == ss[1] == ss[2] != "*":
        flag = True
        q = ss[0]
    return q


print('hello to tic-tac-toe')
a = input("choice: with ai or with friend? (ai/friend) ")
print()

if a == "friend":
    choise = 1
else:
    choise = 2

while True:
    print(str(n) + ' player choose')
    cnt += 1
    if choise == 1 or (choise == 2 and n == 1):
        playerMv = list(map(int, input().split()))
        if (abs(playerMv[0]) != playerMv[0]) or (abs(playerMv[1]) != playerMv[1]):
            print('Invalid move')
            print()
            continue
        if move(playerMv[0] - 1, playerMv[1] - 1) == 'Invalid move':
            print('Invalid move')
            print()
            continue
    else:
        move(12, 12)
    printBoard()
    if whowin():
        print('Winner is player ' + str(n))
        break
    if draw():
        print('draw')
        break

    if n == 1:
        n = 2
    else:
        n = 1
    print()






