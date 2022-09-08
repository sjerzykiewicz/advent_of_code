def polymer_template(chars, pairs, inst, steps):
    if steps > 0:
        actual_pairs = {k: v for k, v in pairs.items() if v > 0}
        for x in actual_pairs:
            chars[inst[x]] += actual_pairs[x]
            pairs[x[0] + inst[x]] += actual_pairs[x]
            pairs[inst[x] + x[1]] += actual_pairs[x]
            pairs[x] -= actual_pairs[x]
        return polymer_template(chars, pairs, inst, steps - 1)
    return max(chars.values()) - min(chars.values())


def main():
    result = []

    chars = {}
    pairs = {}
    inst = {}
    with open("input.txt", "r") as f:
        for line in f:
            if " -> " in line:
                x, y = line.split(" -> ")
                inst[x] = y[:-1]
            else:
                for x in line[:-1]:
                    chars[x] = 0
                for i, x in enumerate(line[:-1]):
                    if line[i + 1] != "\n":
                        y = line[i] + line[i + 1]
                        pairs[y] = 0
                for i, x in enumerate(line[:-1]):
                    chars[x] += 1
                    if line[i + 1] != "\n":
                        y = line[i] + line[i + 1]
                        pairs[y] += 1

    for x in inst:
        if x not in pairs:
            pairs[x] = 0

    for x in inst.values():
        if x not in chars:
            chars[x] = 0

    # Part 1
    result.append(polymer_template(chars.copy(), pairs.copy(), inst, 10))

    # Part 2
    result.append(polymer_template(chars.copy(), pairs.copy(), inst, 40))

    with open("output.txt", "w") as f:
        for i in result:
            f.write(f"{i}\n")


if __name__ == "__main__":
    main()
