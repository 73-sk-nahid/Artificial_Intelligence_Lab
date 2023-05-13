# get the number of grid

N = int(input("Enter the size of grid : "))
#board = [[0] * N for i in range(N)]
board = [ [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0]
        ]


def is_attack(row, col):
    for k in range(0, N):  # checking in row and column
        if (board[row][k] == 1 or board[k][col] == 1):
            return True

    for k in range(0, N):
        for l in range(0, N):  # checking diagonal
            if (k + l == row + col) or (k - l == row - col):
                if board[k][l] == 1:
                    return True
    return False


def n_queen(queen):
    if queen == 0:  # if n is 0 return found
        return True
    for i in range(0, N):    # getting row
        for j in range(0, N):   # getting column
            if (not (is_attack(i, j))) and (board[i][j] != 1):    # if row , column not touched a
                # nd in board its value is not 1 means its empty yet
                board[i][j] = 1    # then declare it with a queen

                if n_queen(queen - 1) == True:
                    return True
                board[i][j] = 0

    return False


n_queen(N)  # Calling solving function

for i in board:
    print(i)
