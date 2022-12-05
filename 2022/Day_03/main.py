def main():
    lines = []

    with open("input.txt", "r") as f:
        for line in f:
            lines.append(line.strip("\n"))

    result = []

    # Part 1
    sum = 0
    for line in lines:
        r_1 = line[: len(line) // 2]
        r_2 = line[len(line) // 2 :]
        common_char = "".join(set(r_1).intersection(r_2))
        sum += calc_value(common_char)
    result.append(sum)

    # Part 2
    sum = 0
    for i in range(0, len(lines) - 2, 3):
        common_char = "".join(set(lines[i]) & set(lines[i + 1]) & set(lines[i + 2]))
        sum += calc_value(common_char)
    result.append(sum)

    with open("output.txt", "w") as f:
        for i in result:
            f.write(f"{i}\n")


def calc_value(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38


if __name__ == "__main__":
    main()
