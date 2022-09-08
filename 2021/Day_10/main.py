def check_subsystem(subsystem):
    brackets = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<",
    }
    corrupted = []
    p2_list = []
    for line in subsystem:
        is_corrupted = False
        stack = []
        for char in line:
            if char in ("(", "[", "{", "<"):
                stack.append(char)

            if char in (")", "]", "}", ">"):
                if len(stack) > 0:
                    if stack[-1] == brackets[char]:
                        stack.pop()
                    else:
                        corrupted.append(char)
                        is_corrupted = True
                        break
                else:
                    break
        if not is_corrupted:
            p2_values = {"(": 1, "[": 2, "{": 3, "<": 4}
            p2 = 0
            for x in reversed(stack):
                p2 *= 5
                p2 += p2_values[x]
            p2_list.append(p2)

    p1_values = {")": 3, "]": 57, "}": 1197, ">": 25137}
    p1 = 0
    for x in corrupted:
        p1 += p1_values[x]

    return p1, p2_list


def main():
    result = []

    navi_subsystem = []
    with open("input.txt", "r") as f:
        for line in f:
            navi_subsystem.append(str(line)[:-1])

    p1, p2_list = check_subsystem(navi_subsystem)

    # Part 1
    result.append(p1)

    # Part 2
    p2_list.sort()
    result.append(p2_list[len(p2_list) // 2])

    with open("output.txt", "w") as f:
        for i in result:
            f.write(f"{i}\n")


if __name__ == "__main__":
    main()
