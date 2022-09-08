import numpy as np


def check(array):
    risk_level = 0
    basins = []
    for i in range(1, len(array) - 1):
        for j in range(1, len(array[i]) - 1):
            if all(
                array[i, j] < array[i + xi, j + xj]
                for xi, xj in [(1, 0), (-1, 0), (0, 1), (0, -1)]
            ):
                risk_level += 1 + array[i, j]
                basins.append(calc_basin(array, i, j))

    return risk_level, basins


def calc_basin(array, i, j, done=set()):
    if array[i, j] == 9 or array[i, j] == 10 or (i, j) in done:
        return 0
    done.add((i, j))
    return 1 + sum(
        calc_basin(array, i + xi, j + xj, done)
        for xi, xj in [(1, 0), (-1, 0), (0, 1), (0, -1)]
    )


def main():
    result = []

    heightmap = []
    with open("input.txt", "r") as f:
        for line in f:
            heightmap.append([int(x) for x in str(line[:-1])])

    heightmap = np.pad(
        np.array(heightmap), pad_width=1, mode="constant", constant_values=10
    )

    risk_level, basins = check(heightmap)

    # Part 1
    result.append(risk_level)

    # Part 2
    basins.sort()
    result.append(np.prod(basins[-3:]))

    with open("output.txt", "w") as f:
        for i in result:
            f.write(f"{i}\n")


if __name__ == "__main__":
    main()
