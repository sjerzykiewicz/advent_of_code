import numpy as np
import re


def fold_board(board, fold_instructions, one_time=False):
    for a, b in fold_instructions:
        if a == "x":
            for i in range(len(board)):
                for j in range(b, len(board[i])):
                    if board[i, j] == 1:
                        board[i, j - ((j - b) * 2)] = 1
            board = np.delete(board, np.s_[b:], axis=1)

        if a == "y":
            for i in range(b, len(board)):
                for j in range(len(board[i])):
                    if board[i, j] == 1:
                        board[i - ((i - b) * 2), j] = 1
            board = np.delete(board, np.s_[b:], axis=0)
        if one_time:
            return board
    return board


def main():
    result = []

    manual = []
    fold_instructions = []
    with open("input.txt", "r") as f:
        for line in f:
            try:
                manual.append([int(x) for x in re.split(",|\n", line)[:-1]])
            except ValueError:
                if line != "\n":
                    fold_instructions.append([x for x in re.split(" |=|\n", line)[2:4]])
    for i, x in enumerate(fold_instructions):
        fold_instructions[i][1] = int(fold_instructions[i][1])

    board = np.zeros((np.max(manual) + 1, np.max(manual) + 1), dtype=int)
    for y, x in manual:
        board[x, y] = 1

    # Part 1
    result.append(np.count_nonzero(fold_board(board, fold_instructions, True) == 1))

    result.append(fold_board(board, fold_instructions))

    with open("output.txt", "w") as f:
        for i in result:
            f.write(f"{i}\n")


if __name__ == "__main__":
    main()
