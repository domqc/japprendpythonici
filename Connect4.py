import numpy as np
COL = 7
ROW = 6
N = 4

def create_board():
    board = np.zeros((ROW,COL))
    return board

def drop_piece(board, row, col, turn):
    board[row][col] = turn

def next_row(board, col):
    for r in range(ROW):
        if board[r][col] == 0:
            return r
        
def is_valid(board, col):
    return board[ROW-1][col] == 0

def print_board(board):
    print(np.flip(board,0))
    
def winning_move(board, piece, N):
    for i in range(N):
        if all(board[i][j] == piece for j in range(N)):
            return (i, 0), (i, N-1)
        if all(board[j][i] == piece for j in range(N)):
            return (0, i), (N-1, i)
        if all(board[i][i] == piece for i in range(N)):
            return (0, 0), (N-1, N-1)
        if all(board[i][N-1-i] == piece for i in range(N)):
            return (0, N-1), (N-1, 0)
    return None, None

board = create_board()
game_over = False
turn = 1
print_board(board)
while not game_over:
    if turn == 1:
        col = int(input("player 1 : "))-1
        if is_valid(board, col):
            row = next_row(board, col)
            drop_piece(board, row, col, turn)
            if winning_move(board, turn, N) != (None, None):
                print("player 1 win")
                game_over = True
            turn = 2
            print_board(board)
        else:
            print("Colonne pleine, veuillez en choisir une autre")
            

    else:
        col = int(input("player 2 : "))-1
        if is_valid(board, col):
            row = next_row(board, col)
            drop_piece(board, row, col, turn)
            if winning_move(board, turn, N) != (None, None):
                print("player 2 win")
                game_over = True
            turn = 1
            print_board(board)
        else:
            print("Colonne pleine, veuillez en choisir une autre")
