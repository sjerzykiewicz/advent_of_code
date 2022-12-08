import numpy as np


def is_visible(forest, i, j):
    if all(forest[i, j] > x for x in forest[i, j + 1:]):
        return True
    
    if all(forest[i, j] > x for x in forest[i, :j]):
        return True

    if all(forest[i, j] > x for x in forest[i + 1:, j]):
        return True
    
    if all(forest[i, j] > x for x in forest[:i, j]):
        return True

    return False


def calc_visible(forest):
    rows = len(forest)
    cols = len(forest[0])
    visible = 0
    visible += 2 * rows + 2 * cols - 4
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if is_visible(forest, i, j):
                visible += 1
    return visible


def get_views(forest, i, j):
    res = 1

    sum = 0
    xi = i - 1
    while xi >= 0:
        if forest[i, j] <= forest[xi, j]:
            sum += 1
            break
        sum += 1
        xi -= 1
    res *= sum

    sum = 0
    xi = i + 1
    while xi < len(forest):
        if forest[i, j] <= forest[xi, j]:
            sum += 1
            break
        sum += 1
        xi += 1
    res *= sum

    sum = 0
    xj = j - 1
    while xj >= 0:
        if forest[i, j] <= forest[i, xj]:
            sum += 1
            break
        sum += 1
        xj -= 1
    res *= sum

    sum = 0
    xj = j + 1
    while xj < len(forest[0]):
        if forest[i, j] <= forest[i, xj]:
            sum += 1
            break
        sum += 1
        xj += 1
    res *= sum

    return res


def calc_view(forest):
    viewing_dist = np.zeros((len(forest), len(forest[0])))
    rows = len(forest)
    cols = len(forest[0])
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            viewing_dist[i, j] = get_views(forest, i, j)
    x, y = np.unravel_index(viewing_dist.argmax(), viewing_dist.shape)
    return viewing_dist[x, y]

def main():
    forest = []
    with open("input.txt", "r") as f:
        for line in f:
            forest.append([int(x) for x in list(line)[:-1]])
    
    result = []

    forest = np.array(forest)

    # Part 1
    result.append(calc_visible(forest))

    # Part 2
    result.append(int(calc_view(forest)))

    with open("output.txt", "w") as f:
        for i in result:
            f.write(f"{i}\n")


if __name__ == "__main__":
    main()