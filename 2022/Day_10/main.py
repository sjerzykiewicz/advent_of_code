import numpy as np


def calc_x(program):
    cycles = np.zeros(242, dtype=int)
    cycles[0] = 1
    cycles[1] = 1
    i = 2
    for process in program:
        cycles[i] = cycles[i - 1]
        if len(process.split(" ")) > 1:
            _, val = process.split(" ")
            i += 1
            cycles[i] = cycles[i - 1] + int(val)
        i += 1
        if i >= 242:
            break

    indexes = [20, 60, 100, 140, 180, 220]
    calc = [cycles[x] * x for x in indexes]

    return sum(calc)


def render(program):
    screen = [["."] * 40 for i in range(6)]
    sprite = np.array([0, 1, 2])

    col = 0
    row = 0
    for process in program:
        if col > 39:
            row += 1
            col = col % 40

        if col in sprite:
            screen[row][col] = "#"

        if len(process.split(" ")) > 1:
            _, val = process.split(" ")

            col += 1

            if col > 39:
                row += 1
                col = col % 40

            if col in sprite:
                screen[row][col] = "#"

            sprite += int(val)

        col += 1

    return screen


def main():
    program = []
    with open("input.txt", "r") as f:
        for line in f:
            program.append(line.strip("\n"))

    result = []

    # Part 1
    result.append(calc_x(program))

    # Part 2
    screen = render(program)
    for row in screen:
        result.append("".join(row))

    with open("output.txt", "w") as f:
        for i in result:
            f.write(f"{i}\n")


if __name__ == "__main__":
    main()
