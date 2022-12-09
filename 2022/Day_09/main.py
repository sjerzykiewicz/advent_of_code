import math


def check_adj(head, tail):
    xh, yh = head
    xt, yt = tail
    return abs(xh - xt) <= 1 and abs(yh - yt) <= 1


def update_position(rope, i, j):
    if math.dist(rope[i], rope[j]) <= math.sqrt(2):
        return

    xi, yi = rope[i]
    xj, yj = rope[j]

    if math.dist(rope[i], rope[j]) == 2:
        if xi > xj:
            rope[j] = (xj + 1, yj)
        elif xi < xj:
            rope[j] = (xj - 1, yj)
        elif yi > yj:
            rope[j] = (xj, yj + 1)
        else:
            rope[j] = (xj, yj - 1)

    else:
        if xi > xj:
            if yi > yj:
                rope[j] = (xj + 1, yj + 1)
            else:
                rope[j] = (xj + 1, yj - 1)
        else:
            if yi > yj:
                rope[j] = (xj - 1, yj + 1)
            else:
                rope[j] = (xj - 1, yj - 1)


def create_path(instructions, rope_len):
    rope = [(0, 0) for x in range(rope_len)]
    visited = set()

    for ins in instructions:
        direction, steps = ins.split(" ")
        steps = int(steps)

        for _ in range(0, steps):
            temp = rope[0]
            x, y = rope[0]
            if direction == "R":
                rope[0] = (x, y + 1)
            if direction == "L":
                rope[0] = (x, y - 1)
            if direction == "U":
                rope[0] = (x + 1, y)
            if direction == "D":
                rope[0] = (x - 1, y)

            if not check_adj(rope[0], rope[1]):
                rope[1] = temp

            visited.add(rope[-1])

            for i in range(1, len(rope) - 1):
                update_position(rope, i, i + 1)
                visited.add(rope[-1])

    return len(visited)


def main():
    instructions = []
    with open("input.txt", "r") as f:
        for line in f:
            instructions.append(line.strip("\n"))

    result = []

    # Part 1
    result.append(create_path(instructions, 2))

    # Part 2
    result.append(create_path(instructions, 10))

    with open("output.txt", "w") as f:
        for i in result:
            f.write(f"{i}\n")


if __name__ == "__main__":
    main()
