def main():
    with open("input.txt", "r") as f:
        for l in f:
            line = l.strip("\n")

    result = []

    # Part 1
    for i in range(3, len(line)):
        packet = line[i - 3 : i + 1]
        packet_cnt = [[packet.count(x), x] for x in set(packet)]
        if len(packet_cnt) == 4:
            break
    result.append(i + 1)

    # Part 2
    for i in range(13, len(line)):
        packet = line[i - 13 : i + 1]
        packet_cnt = [[packet.count(x), x] for x in set(packet)]
        if len(packet_cnt) == 14:
            break
    result.append(i + 1)

    with open("output.txt", "w") as f:
        for i in result:
            f.write(f"{i}\n")


if __name__ == "__main__":
    main()
