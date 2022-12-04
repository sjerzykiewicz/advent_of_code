from re import L


def main():
    lines = []

    with open("input.txt", "r") as f:
        for line in f:
            lines.append(line.strip("\n"))

    result = []

    # Part 1
    sum = 0
    for line in lines:
        elf_1, elf_2 = line.split(",", 2)
        if full_overlap(elf_1, elf_2):
            sum += 1

    result.append(sum)

    # Part 2s
    sum = 0
    for line in lines:
        elf_1, elf_2 = line.split(",", 2)
        if overlap(elf_1, elf_2):
            sum += 1
    result.append(sum)

    with open("output.txt", "w") as f:
        for i in result:
            f.write(f"{i}\n")


def full_overlap(elf_1, elf_2):
    elf_1_1, elf_1_2 = elf_1.split("-", 2)
    elf_2_1, elf_2_2 = elf_2.split("-", 2)
    elf_1_1 = int(elf_1_1)
    elf_1_2 = int(elf_1_2)
    elf_2_1 = int(elf_2_1)
    elf_2_2 = int(elf_2_2)
    len_elf_1 = elf_1_2 - elf_1_1 + 1
    len_elf_2 = elf_2_2 - elf_2_1 + 1
    if len_elf_1 > len_elf_2:
        if elf_2_1 >= elf_1_1 and elf_2_2 <= elf_1_2:
            return True
        return False
    else:
        if elf_1_1 >= elf_2_1 and elf_1_2 <= elf_2_2:
            return True
        return False


def overlap(elf_1, elf_2):
    elf_1_1, elf_1_2 = elf_1.split("-", 2)
    elf_2_1, elf_2_2 = elf_2.split("-", 2)
    elf_1_1 = int(elf_1_1)
    elf_1_2 = int(elf_1_2)
    elf_2_1 = int(elf_2_1)
    elf_2_2 = int(elf_2_2)
    if elf_1_1 >= elf_2_1 and elf_1_1 <= elf_2_2:
        return True
    if elf_1_2 >= elf_2_1 and elf_1_2 <= elf_2_2:
        return True
    if elf_2_1 >= elf_1_1 and elf_2_1 <= elf_1_2:
        return True
    if elf_2_2 >= elf_1_1 and elf_2_2 <= elf_1_2:
        return True
    return False


if __name__ == "__main__":
    main()
