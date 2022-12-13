import ast
import functools

def compare(left, right):
    match left, right:
        case list(), list():
            for i,j in zip(left, right):
                c = compare(i, j)
                if c != 0:
                    return c
            return(compare(len(left), len(right)))
        case int(), list():
            return compare([left], right)
        case list(), int():
            return compare(left, [right])
        case int(), int():
            return left - right

def main():
    lines = []
    with open("input.txt", "r") as f:
        for line in f:
            lines.append(line.strip("\n"))

    result = []

    # Part 1
    sum_of_pairs = 0
    index = 1
    for i in range(0, len(lines), 3):
        left = ast.literal_eval(lines[i])
        right = ast.literal_eval(lines[i + 1])
        if compare(left, right) <= 0:
            sum_of_pairs += index
        index += 1

    result.append(sum_of_pairs)

    # Part 2
    packets = [ast.literal_eval(line) for line in lines if line != ""]
    packets.append([[2]])
    packets.append([[6]])
    packets = sorted(packets, key=functools.cmp_to_key(compare))
    decoder_key = 1
    decoder_key *= (packets.index([[2]]) + 1)
    decoder_key *= (packets.index([[6]]) + 1)
    result.append(decoder_key)

    with open("output.txt", "w") as f:
        for i in result:
            f.write(f"{i}\n")


if __name__ == "__main__":
    main()
