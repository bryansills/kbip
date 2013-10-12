from random import choice

def openSpots(board, side):
    result = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == '-':  
                result.append((row, col))

    print("These spots are open: " + str(result))

    return result

def winningSpots(board, side):
    result = []

    # check horizontal x
    for row in range(3):
        count = 0
        for ind in range(3):
            if board[row][ind] == side:
                count = count + 1

        if count >= 2:
            for ind in range(3):
                if board[row][ind] == '-':
                    result.append((row, ind))

    # check vertical x
    for col in range(3):
        count = 0
        for ind in range(3):
            if board[ind][col] == side:
                count = count + 1

        if count >= 2:
            for ind in range(3):
                if board[ind][col] == '-':
                    result.append((ind, col))

    # check diagonal x
    count = 0
    for ind in range(3):
        if board[ind][ind] == side:
            count = count + 1

    if count >= 2:
        for ind in range(3):
            if board[ind][ind] == '-':
                result.append((ind, ind))


    count = 0
    for ind in range(3):
        if board[2 - ind][ind] == side:
            count = count + 1

    if count >= 2:
        for ind in range(3):
            if board[2 - ind][ind] == '-':
                result.append((2 - ind, ind))

    print("These are winning spots: " + str(result))

    return result


def blockLosingSpots(board, side):
    result = []

    # check horizontal x
    for row in range(3):
        count = 0
        for ind in range(3):
            if board[row][ind] != side and board[row][ind] != '-':
                count = count + 1

        if count >= 2:
            for ind in range(3):
                if board[row][ind] == '-':
                    result.append((row, ind))

    # check vertical x
    for col in range(3):
        count = 0
        for ind in range(3):
            if board[ind][col] != side and board[ind][col] != '-':
                count = count + 1

        if count >= 2:
            for ind in range(3):
                if board[ind][col] == '-':
                    result.append((ind, col))

    # check diagonal x
    count = 0
    for ind in range(3):
        if board[ind][ind] != side and board[ind][ind] != '-':
            count = count + 1

    if count >= 2:
        for ind in range(3):
            if board[ind][ind] == '-':
                result.append((ind, ind))


    count = 0
    for ind in range(3):
        if board[2 - ind][ind] != side and board[2 - ind][ind] != '-':
            count = count + 1

    if count >= 2:
        for ind in range(3):
            if board[2 - ind][ind] == '-':
                result.append((2 - ind, ind))


    print("These spots block the opponent from winning: " + str(result))

    return result

def oppositeCornerSpots(board, side):
    result = []

    if board[2][2] == side and board[0][0] == '-':
        result.append((0,0))

    if board[0][2] == side and board[2][0] == '-':
        result.append((2,0))

    if board[2][0] == side and board[0][2] == '-':
        result.append((0,2))

    if board[0][0] == side and board[2][2] == '-':
        result.append((2,2))


    print("These spots are open corner spots and the agent controls the opposite: " + str(result))

    return result


def cornerSpots(board, side):
    result = []

    if board[0][0] == '-':
        result.append((0,0))

    if board[2][0] == '-':
        result.append((2,0))

    if board[0][2] == '-':
        result.append((0,2))

    if board[2][2] == '-':
        result.append((2,2))


    print("These spots are open corner spots: " + str(result))

    return result
