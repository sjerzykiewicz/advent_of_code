Points = {"A": 1, "B": 2, "C": 3}


def main():
    sum_1 = 0
    sum_2 = 0

    with open("input.txt", "r") as f:
        for line in f:
            sum_1 += fight_p1(line)
            sum_2 += fight_p2(line)

    result = []

    # Part 1
    result.append(sum_1)

    # Part 2
    result.append(sum_2)

    with open("output.txt", "w") as f:
        for i in result:
            f.write(f"{i}\n")


def fight_p1(line):
    opponent, me = line.split(" ", 2)
    me = me.strip("\n")

    change = {"X": "A", "Y": "B", "Z": "C"}
    new_me = change[me]
    if opponent == new_me:
        # DRAW
        return 3 + Points[new_me]
    if (
        (opponent == "A" and new_me == "B")
        or (opponent == "B" and new_me == "C")
        or (opponent == "C" and new_me == "A")
    ):
        # WIN
        return 6 + Points[new_me]
    else:
        # LOSE
        return Points[new_me]


def fight_p2(line):
    win = {"A": "B", "B": "C", "C": "A"}
    lose = {"A": "C", "B": "A", "C": "B"}
    opponent, res = line.split(" ", 2)
    res = res.strip("\n")

    if res == "X":
        return Points[lose[opponent]]
    if res == "Y":
        return 3 + Points[opponent]
    if res == "Z":
        return 6 + Points[win[opponent]]


if __name__ == "__main__":
    main()
