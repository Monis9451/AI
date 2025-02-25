def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_n_queens_util(board, row, n):
    if row >= n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'
            if solve_n_queens_util(board, row + 1, n):
                return True
            board[row][col] = '.'

    return False

def solve_n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    if solve_n_queens_util(board, 0, n):
        for row in board:
            print(' '.join(row))
        return True
    else:
        print("No solution exists")
        return False

n = 8
solve_n_queens(n)