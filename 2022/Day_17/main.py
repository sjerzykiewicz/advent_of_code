def rock_edges(rock):
    min_x, max_x = float("inf"), 0
    for x, y in rock:
        min_y = y
        if x < min_x:
            min_x = x
            min_y = y
        max_y = y
        if x > max_x:
            max_x = x
            max_y = y
    return (min_x, min_y), (max_x, max_y)


def move_rock(rock, jet, chamber):
    min_edge, max_edge = rock_edges(rock)
    if (
        jet == "<"
        and min_edge[0] > 0
        and all((x - 1, y) not in chamber for x, y in rock)
    ):
        return [(x - 1, y) for x, y in rock]
    if (
        jet == ">"
        and max_edge[0] < 6
        and all((x + 1, y) not in chamber for x, y in rock)
    ):
        return [(x + 1, y) for x, y in rock]
    return rock


def get_highest(chamber):
    max_y = 0
    for _, y in chamber:
        max_y = max(max_y, y)
    return max_y


def get_height(rocks, jet_of_gas, num_of_rocks):
    chamber = set()
    for floor in [(x, 0) for x in range(7)]:
        chamber.add(floor)
    i = 0
    j = 0

    cycles = {}

    while i < num_of_rocks:
        rock = rocks[i % len(rocks)]
        jet = jet_of_gas[j % len(jet_of_gas)]

        highest = get_highest(chamber)
        rock = [(x, y + highest) for x, y in rock]

        while True:
            pattern = f"{i % len(rocks)} {j % len(jet_of_gas)}"
            if pattern in cycles:
                cycles[pattern].append((i, highest))
            else:
                cycles[pattern] = [(i, highest)]

            rock = move_rock(rock, jet, chamber)
            j += 1
            jet = jet_of_gas[j % len(jet_of_gas)]
            if all((x, y - 1) not in chamber for x, y in rock):
                rock = [(x, y - 1) for x, y in rock]
            else:
                break

        chamber = chamber | set(rock)

        i += 1

    max_y = 0
    for _, y in chamber:
        max_y = max(max_y, y)

    return max_y


def main():
    with open("input.txt", "r") as f:
        jet_of_gas = [x for x in f.readline().strip("\n")]

    rocks = [
        [(2, 4), (3, 4), (4, 4), (5, 4)],
        [(3, 4), (3, 5), (2, 5), (4, 5), (3, 6)],
        [(2, 4), (3, 4), (4, 4), (4, 5), (4, 6)],
        [(2, 4), (2, 5), (2, 6), (2, 7)],
        [(2, 4), (2, 5), (3, 4), (3, 5)],
    ]

    result = []

    chamber = set()
    for floor in [(x, 0) for x in range(7)]:
        chamber.add(floor)

    # Part 1
    result.append(get_height(rocks, jet_of_gas, 2022))

    # Part 2
    # Found cycles in 'tetris' like this 0 (rock id) 4612 (jet id) [(805, 1316), (2500, 3987)]
    # 1,000,000,000,000 - 2500 = 999,999,997,500
    # 999,999,997,500 / (2500 - 805) = 589,970,500
    # 3987 + 589,970,500 * (3987 - 1316) = 1,575,811,209,487
    # Height after 10^12 rocks 1,575,811,209,487 

    with open("output.txt", "w") as f:
        for i in result:
            f.write(f"{i}\n")


if __name__ == "__main__":
    main()
