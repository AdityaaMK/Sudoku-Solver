def computer_solve(bo):
    # display_board(bo)
    # print("\n\n\n")
    empty = get_empty(bo)
    if not empty:
        return False
    else:
        row, col = empty

    # backtracking algorithm
    for i in range(1, 10):
        if is_legal(bo, i, (row, col)):
            # print(row, col)
            bo[row][col] = i  # adds into board

            if not computer_solve(bo):  # recursively try to finish solution with new board
                return False

            bo[row][col] = 0

    return True


def is_legal(bo, num, pos):
    # Checking if row is valid
    for i in range(len(bo[0])):
        # first part of if statement checks if there is a duplicate of num and second part ignores the spot where we
        # inserted num in the row
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Checking if column is valid
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Checking is square is valid
    sq_x = pos[1] // 3
    sq_y = pos[0] // 3

    for i in range(sq_y * 3, sq_y * 3 + 3):
        for j in range(sq_x * 3, sq_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def display_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0:
            print("- - - - - - - - - - - - -")

        for j in range(len(bo[0])):
            if j % 3 == 0:
                print("| ", end="")

            if j == 8:
                print(bo[i][j], end="")
                print(" |")
            else:
                print(str(bo[i][j]) + " ", end="")

        if i == 8:
            print("- - - - - - - - - - - - -")


def get_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j  # returns row, column


def is_valid(bo):
    # Checks that all rows contain no repeats
    for row in bo:
        found = []
        for i in row:
            if i in found:
                return False
            if i != 0:
                found.append(i)

    # Checks that all columns contain no repeats
    for c in range(9):
        found = []
        for r in range(9):
            i = bo[r][c]
            if i in found:
                return False
            if i != 0:
                found.append(i)

    return True


grid = []

if len(grid) == 0:
    temp_grid = []
    board = ""
    while len(board) != 81:
        temp_grid = []
        board = input("Type in the board, going left to right row by row, 0 = empty: ")
        if len(board) != 81:
            print("Not 81 characters.")
        else:
            for row in range(9):
                r = []
                for col in range(9):
                    r.append(int(board[row * 9 + col]))  # getting each value in the row
                temp_grid.append(r)
            if not is_valid(temp_grid):
                data = ""
                print("Please enter a valid board.")

    grid = temp_grid

if is_valid(grid):
    print(grid)
    display_board(grid)
    computer_solve(grid)
    print("\n\n\n")
    display_board(grid)

sample_board = [
    [0, 7, 0, 8, 0, 3, 0, 5, 0],
    [5, 0, 0, 0, 1, 0, 2, 0, 3],
    [0, 0, 3, 6, 0, 0, 8, 0, 0],
    [0, 0, 0, 0, 0, 0, 6, 8, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [9, 3, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 7, 0, 0, 1, 3, 0, 0],
    [8, 0, 6, 0, 2, 0, 0, 0, 1],
    [0, 1, 0, 5, 0, 6, 0, 7, 0]
]


