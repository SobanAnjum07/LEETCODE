def is_valid(arr: list[str]) -> bool:
    arr = [i for i in arr if i != "."]
    return len(arr) == len(set(arr))

def isValidSudoku(board: list[list[str]]) -> bool:
    # Check rows
    for row in board:
        if not is_valid(row):
            return False

    # Check columns
    for col in range(9):
        if not is_valid([row[col] for row in board]):
            return False

    # Check 3x3 squares
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not is_valid(square):
                return False

    return True

if __name__ == "__main__":

    board = [


         ["5", "3", ".",    ".", "7", ".",    ".", ".", "."] ,
         ["6", ".", ".",    "1", "9", "5",    ".", ".", "."] ,
         [".", "9", "8",    ".", ".", ".",    ".", "6", "."] ,


         ["8", ".", ".",    ".", "6", ".",    ".", ".", "3"] ,
         ["4", ".", ".",    "8", ".", "3",    ".", ".", "1"] ,
         ["7", ".", ".",    ".", "2", ".",    ".", ".", "6"] ,


         [".", "6", ".",    ".", ".", ".",    "2", "8", "."] ,
         [".", ".", ".",    "4", "1", "9",    ".", ".", "5"] ,
         [".", ".", ".",    ".", "8", ".",    ".", "7", "9"] ,


    ]
    print(isValidSudoku(board))
