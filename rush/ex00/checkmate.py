def change_to_2d_array(board):          # แปลง string -> array 2D
    parsed_board = board.split('\n')
    two_d_list = []
    for row in parsed_board:
        new_row = []
        for col in row:
            new_row.append(col)
        two_d_list.append(new_row)

    return two_d_list


def find_the_king(board):               # หาพิกัด king
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'K':
                k_row = row
                k_col = col
                return k_row, k_col

    return None


def check_threats(board, k_row, k_col):     # หาศัตรูโดยเริ่มเลื่อนจาก king
    row = len(board)
    col = len(board[0])

    # up
    for r in range(k_row - 1, -1, -1):
        each = board[r][k_col]
        if each == 'R' or each == 'Q':
            return True
        elif each == '.':
            continue
        else:
            break

    # down
    for r in range(k_row + 1, row):
        each = board[r][k_col]
        if each == 'R' or each == 'Q':
            return True
        elif each == '.':
            continue
        else:
            break

    # left
    for c in range(k_col - 1, -1, -1):
        each = board[k_row][c]
        if each == 'R' or each == 'Q':
            return True
        elif each == '.':
            continue
        else:
            break

    # right
    for c in range(k_col + 1, col):
        each = board[k_row][c]
        if each == 'R' or each == 'Q':
            return True
        elif each == '.':
            continue
        else:
            break

    # ทแยงบนซ้าย
    r = k_row - 1
    c = k_col - 1
    while r >= 0 and c >= 0:
        each = board[r][c]
        if each == 'B' or each == 'Q':
            return True
        elif each == '.':
            r -= 1
            c -= 1
        else:
            break

    # ทแยงบนขวา
    r = k_row - 1
    c = k_col + 1
    while r >= 0 and c < col:
        each = board[r][c]
        if each == 'B' or each == 'Q':
            return True
        elif each == '.':
            r -= 1
            c += 1
        else:
            break

    # ทแยงล่างซ้าย
    r = k_row + 1
    c = k_col - 1
    while r < row and c >= 0:
        each = board[r][c]
        if each == 'B' or each == 'Q':
            return True
        elif each == '.':
            r += 1
            c -= 1
        else:
            break

    # ทแยงล่างขวา
    r = k_row + 1
    c = k_col + 1
    while r < row and c < col:
        each = board[r][c]
        if each == 'B' or each == 'Q':
            return True
        elif each == '.':
            r += 1
            c += 1
        else:
            break

    # pawn ทแยงล่างซ้าย
    if k_row + 1 < row and k_col - 1 >= 0:
        if board[k_row + 1][k_col - 1] == 'P':
            return True

    # pawn ทแยงล่างขวา
    if k_row + 1 < row and k_col + 1 < col:
        if board[k_row + 1][k_col + 1] == 'P':
            return True

    # pawn ทแยงบนซ่าย (ดัก)
    if k_row - 1 >= 0 and k_col - 1 >= 0:
        if board[k_row - 1][k_col - 1] == 'P':
            return True

    # pawn ทแยงบนขวา (ดัก)
    if k_row - 1 >= 0 and k_col + 1 < col:
        if board[k_row - 1][k_col + 1] == 'P':
            return True

    return False


def checkmate(board):
    # ไม่มีข้อมูล หรือ board ไม่เป็น string
    if not board or not isinstance(board, str):
        print("Error!!!")
        return

    new_board = change_to_2d_array(board)

    # check square
    row_count = len(new_board)  # only row
    for each_col in new_board:
        if len(each_col) != row_count:  # ไล่แต่ละหลักเทียบกับแถว
            print("Error!!!")
            return

    # check king
    king = find_the_king(new_board)
    if king is None:
        print("Error!!!")
        return

    k_row, k_col = king
    if check_threats(new_board, k_row, k_col):
        print("Success")
    else:
        print("Fail")
