import random
import time
def create_board():
    return [['-' for _ in range(3)] for _ in range(3)]


def check_rowwin(board):
    for i in range(3):
        a=board[i][0]
        count=0
        if(a=='-'):
            return False
        for j in range(3):
            if(board[i][j]==a):
                count+=1
            if(count==3):
                return True
    return False

def check_colwin(board):
    for i in range(3):
        a=board[0][i]
        count=0
        if(a=='-'):
            return False
        for j in range(3):
            if(board[j][i]==a):
                count+=1
            if(count==3):
                return True
    return False

def check_diagwin(board):
    if(board[0][0]=='-'):
        return False
    if(board[0][2]=='-'):
        return False
    if(board[0][0]==board[1][1]==board[2][2]):
        return True
    if(board[0][2]==board[1][1]==board[2][0]):
        return True
    return False

def play_move(board):
    valid_in = [1, 2, 3]
    while True:
        try:
            print("Enter row and column of the element you want to play (rows: 1, 2, 3), (columns: 1, 2, 3)")
            a, b = map(int, input().split(' '))
            if a not in valid_in or b not in valid_in:
                raise ValueError("Invalid move")
            a -= 1
            b -= 1
            if board[a][b] == '-':
                board[a][b] = 'x'
                break
            else:
                raise ValueError("Invalid move")
        except ValueError as e:
            print(str(e) + ". Please play again.")

def computer_move(board):
    a=random.randint(0,2)
    b=random.randint(0,2)
    if(board[a][b]=='-'):
        board[a][b]='o'
    else:
        computer_move(board)
def tie(board):
    for i in range(3):
        for j in range(3):
            if(board[i][j]=='-'):
                return False
    return True
def print_board(board):
    for row in board:
        print(' '.join(row))

def game():
    board=create_board()
    flag=True
    print_board(board)
    while(flag):
        play_move(board)
        if(check_colwin(board) or check_rowwin(board) or check_diagwin(board)):
            print("You have won!!!")
            print_board(board)
            flag=False
            break
        if(tie(board)):
            print("Its is Tie")
            flag=False
            break
        print_board(board)
        time.sleep(2.0)
        computer_move(board)
        print("The computer has played")
        if(check_colwin(board) or check_rowwin(board) or check_diagwin(board)):
            print("Computer has won!!!")
            flag=False
            break
        if(tie(board)):
            print("Its is Tie")
            flag=False
            break
        print_board(board)

game()

    