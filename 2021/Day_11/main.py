import numpy as np
from numpy.core.numeric import argwhere, array_equal


def adjacent_energy(array, args, done_args):
    if args:
        for x, y in args:
            for i, j in (
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1),
                (1, 1),
                (-1, -1),
                (1, -1),
                (-1, 1),
            ):
                if array[x + i, y + j] != -1:
                    array[x + i, y + j] += 1

        new_args = set([tuple(x) for x in np.argwhere(array > 9)])

        for x, y in args:
            done_args.add((x, y))

        new_args = new_args - done_args

        return adjacent_energy(array, new_args, done_args)

    else:
        return array


def calc_step(array, step, flashes):
    if step > 0:
        array[array != -1] += 1
        args = set([tuple(x) for x in np.argwhere(array > 9)])
        array = adjacent_energy(array, args, set())
        how_many_flashes = array > 9
        flashes += how_many_flashes.sum()
        array[array > 9] = 0
        return calc_step(array, step - 1, flashes)
    return flashes


def when_sync(array, step):
    array[array != -1] += 1
    args = set([tuple(x) for x in np.argwhere(array > 9)])
    array = adjacent_energy(array, args, set())
    how_many_flashes = array > 9
    flashes = how_many_flashes.sum()
    array[array > 9] = 0
    x, y = array.shape
    if flashes != (x - 2) * (y - 2):
        return when_sync(array, step + 1)
    return step + 1


def main():
    result = []

    energy_level = []
    with open("input.txt", "r") as f:
        for line in f:
            energy_level.append([int(x) for x in list(line)[:-1]])

    energy_level = np.pad(
        np.array(energy_level), pad_width=1, mode="constant", constant_values=-1
    )

    # Part 1
    result.append(calc_step(np.copy(energy_level), 100, 0))

    # Part 2
    result.append(when_sync(np.copy(energy_level), 0))

    with open("output.txt", "w") as f:
        for i in result:
            f.write(f"{i}\n")


if __name__ == "__main__":
    main()
