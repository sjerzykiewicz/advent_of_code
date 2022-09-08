def main():
    result = []

    codes = []
    with open("input.txt", "r") as f:
        for i, line in enumerate(f):
            codes.append(line.split("|"))
            codes[i][0] = codes[i][0].split()
            codes[i][1] = codes[i][1].split()

    # Part 1
    counter = 0
    for code in codes:
        for x in code[1]:
            if len(x) in (2, 3, 4, 7):
                counter += 1

    result.append(counter)

    # Part 2
    num_codes = {0: {}, 1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}, 9: {}}
    sum_values = 0
    for code in codes:
        for x in code[0]:
            if len(x) == 2:
                num_codes[1] = set(x)
            if len(x) == 3:
                num_codes[7] = set(x)
            if len(x) == 4:
                num_codes[4] = set(x)
            if len(x) == 7:
                num_codes[8] = set(x)

        for x in code[0]:
            if len(x) == 5:
                if (
                    len(set(x).intersection(num_codes[4])) == 3
                    and len(set(x).intersection(num_codes[1])) == 2
                ):
                    num_codes[3] = set(x)
                if (
                    len(set(x).intersection(num_codes[4])) == 2
                    and len(set(x).intersection(num_codes[1])) == 1
                ):
                    num_codes[2] = set(x)
                if (
                    len(set(x).intersection(num_codes[4])) == 3
                    and len(set(x).intersection(num_codes[1])) == 1
                ):
                    num_codes[5] = set(x)
            if len(x) == 6:
                if (
                    len(set(x).intersection(num_codes[4])) == 3
                    and len(set(x).intersection(num_codes[1])) == 1
                ):
                    num_codes[6] = set(x)
                if (
                    len(set(x).intersection(num_codes[4])) == 4
                    and len(set(x).intersection(num_codes[1])) == 2
                ):
                    num_codes[9] = set(x)
                if (
                    len(set(x).intersection(num_codes[4])) == 3
                    and len(set(x).intersection(num_codes[1])) == 2
                ):
                    num_codes[0] = set(x)
        value = 0
        for x in code[1]:
            for i in range(0, 10):
                if set(x) == num_codes[i]:
                    value = value * 10 + i
        sum_values += value

    result.append(sum_values)

    with open("output.txt", "w") as f:
        for i in result:
            f.write(f"{i}\n")


if __name__ == "__main__":
    main()
