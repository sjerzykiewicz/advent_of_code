import numpy as np


def dijkstras_pathfinding(board, n):
    dist_map = np.ones((n, n), dtype=int) * np.Infinity
    dist_map[0, 0] = 0
    back_track = np.ones((n, n), dtype=int) * np.NaN
    visited = np.zeros((n, n), dtype=bool)
    finished = False
    x = y = 0
    count = 0

    while not finished:
        if x < n - 1:
            if (
                dist_map[x + 1, y] > board[x + 1, y] + dist_map[x, y]
                and not visited[x + 1, y]
            ):
                dist_map[x + 1, y] = board[x + 1, y] + dist_map[x, y]
                back_track[x + 1, y] = np.ravel_multi_index([x, y], (n, n))
        if x > 0:
            if (
                dist_map[x - 1, y] > board[x - 1, y] + dist_map[x, y]
                and not visited[x - 1, y]
            ):
                dist_map[x - 1, y] = board[x - 1, y] + dist_map[x, y]
                back_track[x - 1, y] = np.ravel_multi_index([x, y], (n, n))
        if y < n - 1:
            if (
                dist_map[x, y + 1] > board[x, y + 1] + dist_map[x, y]
                and not visited[x, y + 1]
            ):
                dist_map[x, y + 1] = board[x, y + 1] + dist_map[x, y]
                back_track[x, y + 1] = np.ravel_multi_index([x, y], (n, n))
        if y > 0:
            if (
                dist_map[x, y - 1] > board[x, y - 1] + dist_map[x, y]
                and not visited[x, y - 1]
            ):
                dist_map[x, y - 1] = board[x, y - 1] + dist_map[x, y]
                back_track[x, y - 1] = np.ravel_multi_index([x, y], (n, n))
        visited[x, y] = True
        dist_map_temp = dist_map
        dist_map_temp[np.where(visited)] = np.Infinity
        min_length = np.unravel_index(np.argmin(dist_map_temp), np.shape(dist_map_temp))
        x, y = min_length[0], min_length[1]
        if x == n - 1 and y == n - 1:
            finished = True
        count += 1

    map_temp = board.astype(float)
    x = y = n - 1
    path = []
    map_temp[x, y] = np.nan

    while x > 0.0 or y > 0.0:
        path.append([int(x), int(y)])
        temp = np.unravel_index(int(back_track[int(x), int(y)]), (n, n))
        x, y = temp[0], temp[1]
        map_temp[int(x), int(y)] = np.nan
    # path.append([int(x), int(y)])  # Starting point

    return path


def calc_risk(board, path):
    risk_level = 0
    for x, y in path:
        risk_level += board[x, y]
    return risk_level


def enlarge_cave(board):
    board_copy = np.copy(board)
    for x in range(4):
        board_copy += 1
        board_copy[board_copy > 9] = 1
        board = np.concatenate((board, board_copy), axis=1)
    board_copy = np.copy(board)
    for x in range(4):
        board_copy += 1
        board_copy[board_copy > 9] = 1
        board = np.concatenate((board, board_copy), axis=0)

    return board


def main():
    result = []

    board = []
    with open("input.txt", "r") as f:
        for line in f:
            board.append([int(x) for x in list(line)[:-1]])

    board = np.array(board)

    # Part 1
    result.append(calc_risk(board, dijkstras_pathfinding(board, len(board))))

    # Part 2
    result.append(
        calc_risk(
            enlarge_cave(board),
            dijkstras_pathfinding(enlarge_cave(board), len(enlarge_cave(board))),
        )
    )

    with open("output.txt", "w") as f:
        for i in result:
            f.write(f"{i}\n")


if __name__ == "__main__":
    main()

