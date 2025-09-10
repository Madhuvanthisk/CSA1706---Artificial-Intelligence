N = 8  

def print_solution(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")

def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j]:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j]:
            return False

    return True

def solve(board, row):
    if row == N:
        print_solution(board)
        return True  
    res = False
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            res = solve(board, row + 1) or res
            board[row][col] = 0  
    return res

board = [[0]*N for _ in range(N)]
solve(board, 0)
