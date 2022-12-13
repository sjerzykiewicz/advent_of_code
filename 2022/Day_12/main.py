import numpy as np


class Point:
    def __init__(self, row, col, dist):
        self.row = row
        self.col = col
        self.dist = dist


def BFS(heightmap, start, end):
    visited = [[False for _ in range(len(heightmap[0]))] for _ in range(len(heightmap))]
    current = Point(start[0], start[1], 0)
    queue = []
    queue.append(current)
    visited[current.row][current.col] = True

    while queue:
        current = queue.pop(0)

        if current.row == end[0] and current.col == end[1]:
            return current.dist

        for xi, yi in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if (
                ord(heightmap[current.row + xi][current.col + yi])
                - ord(heightmap[current.row][current.col])
                <= 1
                and not visited[current.row + xi][current.col + yi]
            ):
                queue.append(
                    Point(current.row + xi, current.col + yi, current.dist + 1)
                )
                visited[current.row + xi][current.col + yi] = True
    return float("inf")


def main():
    heightmap = []
    with open("input.txt", "r") as f:
        for line in f:
            line = [x for x in line.strip("\n")]
            heightmap.append(line)

    heightmap = np.pad(heightmap, pad_width=1, mode="constant", constant_values="~")
    start = (np.where(heightmap == "S")[0][0], np.where(heightmap == "S")[1][0])
    end = (np.where(heightmap == "E")[0][0], np.where(heightmap == "E")[1][0])
    heightmap[start[0]][start[1]] = "a"
    heightmap[end[0]][end[1]] = "z"

    result = []

    # Part 1
    result.append(BFS(heightmap, start, end))

    # Part 2
    all_a = np.where(heightmap == "a")
    listOfCoordinates = list(zip(all_a[0], all_a[1]))
    dists = [BFS(heightmap, x, end) for x in listOfCoordinates]
    result.append(min(dists))

    with open("output.txt", "w") as f:
        for i in result:
            f.write(f"{i}\n")


if __name__ == "__main__":
    main()
