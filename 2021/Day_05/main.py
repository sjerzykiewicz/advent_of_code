import numpy as np
import re


def main():
    result = []

    with open("input.txt", "r") as f:
        lines = f.readlines()

    # Part 1
    board = np.zeros((1000, 1000)).astype(int)
    for line in lines:
        cords = [int(i) for i in list(filter(lambda a: a != "", re.split(r"\D", line)))]
        x1, y1, x2, y2 = cords
        if x1 == x2:
            if y1 > y2:
                board[y2 : y1 + 1, x1] += 1
            else:
                board[y1 : y2 + 1, x1] += 1
        elif y1 == y2:
            if x1 > x2:
                board[y1, x2 : x1 + 1] += 1
            else:
                board[y1, x1 : x2 + 1] += 1

    board_gt_2 = board >= 2
    result.append(board_gt_2.sum())

    # Part 2
    board = np.zeros((1000, 1000)).astype(int)
    for line in lines:
        cords = [int(i) for i in list(filter(lambda a: a != "", re.split(r"\D", line)))]
        x1, y1, x2, y2 = cords
        if x1 == x2:
            if y1 > y2:
                board[y2 : y1 + 1, x1] += 1
            else:
                board[y1 : y2 + 1, x1] += 1
        elif y1 == y2:
            if x1 > x2:
                board[y1, x2 : x1 + 1] += 1
            else:
                board[y1, x1 : x2 + 1] += 1
        elif x1 > x2:
            if y1 > y2:
                np.fill_diagonal(
                    board[y2 : y1 + 1, x2 : x1 + 1],
                    board[y2 : y1 + 1, x2 : x1 + 1].diagonal() + 1,
                )
            else:
                np.fill_diagonal(
                    np.fliplr(board[y1 : y2 + 1, x2 : x1 + 1]),
                    np.fliplr(board[y1 : y2 + 1, x2 : x1 + 1]).diagonal() + 1,
                )
        elif x2 > x1:
            if y1 > y2:
                np.fill_diagonal(
                    np.fliplr(board[y2 : y1 + 1, x1 : x2 + 1]),
                    np.fliplr(board[y2 : y1 + 1, x1 : x2 + 1]).diagonal() + 1,
                )
            else:
                np.fill_diagonal(
                    board[y1 : y2 + 1, x1 : x2 + 1],
                    board[y1 : y2 + 1, x1 : x2 + 1].diagonal() + 1,
                )

    board_gt_2 = board >= 2
    result.append(board_gt_2.sum())

    with open("output.txt", "w") as f:
        for i in result:
            f.write(f"{i}\n")


if __name__ == "__main__":
    main()
