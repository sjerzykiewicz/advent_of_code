import numpy as np
import scipy

np.set_printoptions(threshold=np.inf)


def main():
    lines = []
    max_x, max_y, max_z = 0, 0, 0
    with open("input.txt", "r") as f:
        for line in f:
            lines.append(line.strip("\n"))
            x, y, z = (int(x) for x in line.strip("\n").split(","))
            max_x, max_y, max_z = max(max_x, x), max(max_y, y), max(max_z, z)

    result = []

    # Part 1
    grid = np.array(
        [
            [[0 for _ in range(max_z + 1)] for _ in range(max_y + 1)]
            for _ in range(max_x + 1)
        ]
    )
    for line in lines:
        x, y, z = (int(a) for a in line.strip("\n").split(","))
        grid[x, y, z] = 1

    bin = scipy.ndimage.generate_binary_structure(3, 1)
    conn_grid = grid * scipy.ndimage.convolve(grid, bin, mode="constant")

    number_of_blocks = np.count_nonzero(conn_grid > 0)
    conn_grid = conn_grid[conn_grid > 0] - 1
    result.append(number_of_blocks * 6 - conn_grid.sum())

    # Part 2

    with open("output.txt", "w") as f:
        for i in result:
            f.write(f"{i}\n")


if __name__ == "__main__":
    main()
