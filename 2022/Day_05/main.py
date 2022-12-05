def main():
    lines = []

    with open("input.txt", "r") as f:
        for line in f:
            lines.append(line.strip("\n"))

    result = []

    # Part 1
    msg = part_1(lines)
    result.append(msg)

    # Part 2
    msg = part_2(lines)
    result.append(msg)

    with open("output.txt", "w") as f:
        for i in result:
            f.write(f"{i}\n")


def part_1(lines):
    stacks, cnt = get_stacks(lines)
    for i in range(cnt, len(lines)):
        _, m, _, f, _, t = lines[i].split(" ")
        for _ in range(int(m)):
            temp = stacks[int(f) - 1].pop()
            stacks[int(t) - 1].append(temp)

    return get_msg(stacks)


def part_2(lines):
    stacks, cnt = get_stacks(lines)
    for i in range(cnt, len(lines)):
        _, m, _, f, _, t = lines[i].split(" ")
        temp = []
        for _ in range(int(m)):
            temp.append(stacks[int(f) - 1].pop())
        for item in reversed(temp):
            stacks[int(t) - 1].append(item)

    return get_msg(stacks)


def get_stacks(lines):
    crates_stack = []
    cnt = 0
    for line in lines:
        if line == "":
            cnt += 1
            break
        crates_stack.append(line)
        cnt += 1

    crates_stack.reverse()

    crates_stack[0] = [int(x) for x in crates_stack[0].split()]

    stacks = [[] for x in crates_stack[0]]

    for i in range(1, len(crates_stack)):
        new_stack = crates_stack[i].replace("    ", " [] ")
        crates_stack[i] = [x for x in new_stack.split()]
        for e, crate in enumerate(crates_stack[i]):
            if crate != "[]":
                stacks[e].append(crate)

    return stacks, cnt


def get_msg(stacks):
    msg = ""

    for stack in stacks:
        msg += stack[len(stack) - 1].strip("[").strip("]")

    return msg


if __name__ == "__main__":
    main()
