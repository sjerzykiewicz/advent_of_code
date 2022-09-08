import numpy as np


def check_board(board):
    for i in range(5):
        if np.all(board[i, :] == -1):
            return True
        if np.all(board[:, i] == -1):
            return True
    return False


def check_last_board(board, boards):
    counter = 0
    winner = False
    for b in boards:
        if b[0, 0] == -2:
            counter += 1
    if counter == len(boards) - 1:
        winner = True

    for i in range(5):
        if np.all(board[i, :] == -1):
            if winner:
                return True
            board.fill(-2)
        if np.all(board[:, i] == -1):
            if winner:
                return True
            board.fill(-2)
    return False


def main():
    result = []

    boards = []
    with open("input.txt", "r") as f:
        nums = np.fromstring(f.readline(), dtype=int, sep=",")
        lines = f.readlines()
        line_count = sum(1 for line in lines)
        for i in range(0, line_count, 6):
            boards.append(np.loadtxt(lines[i : i + 6], dtype=int))

    # Part 1
    boards_1 = boards.copy()
    loop = False
    for num in nums:
        for board in boards_1:
            board[board == num] = -1
            if check_board(board):
                board_sum = board[board != -1].sum()
                print(
                    f"Winner!\n{board}\nnumber: {num}\nsum: {board_sum}\nresult: {board_sum * num}\n"
                )
                loop = True
                break
        if loop:
            break

    result.append(board_sum * num)

    # Part 2
    boards_2 = boards.copy()
    loop = False
    for num in nums:
        for board in boards_2:
            board[board == num] = -1
            if check_last_board(board, boards_2):
                board_sum = board[board != -1].sum()
                print(
                    f"Last winner!\n{board}\nnumber: {num}\nsum: {board_sum}\nresult: {board_sum * num}\n"
                )
                loop = True
                break
        if loop:
            break

    result.append(board_sum * num)

    with open("output.txt", "w") as f:
        for i in result:
            f.write(f"{i}\n")


if __name__ == "__main__":
    main()
