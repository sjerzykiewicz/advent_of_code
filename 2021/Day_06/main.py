def create_lanternfish(fish_shoal, day):
    while day > 0:
        new_fish = fish_shoal[0]
        fish_shoal[0] = fish_shoal[1]
        fish_shoal[1] = fish_shoal[2]
        fish_shoal[2] = fish_shoal[3]
        fish_shoal[3] = fish_shoal[4]
        fish_shoal[4] = fish_shoal[5]
        fish_shoal[5] = fish_shoal[6]
        fish_shoal[6] = fish_shoal[7] + new_fish
        fish_shoal[7] = fish_shoal[8]
        fish_shoal[8] = new_fish
        day -= 1
    return sum(fish_shoal.values())


def main():
    result = []

    with open("input.txt", "r") as f:
        lanternfish = [int(i) for i in f.readline().split(",")]

    fish_shoal = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

    for fish in lanternfish:
        fish_shoal[fish] += 1

    # Part 1
    result.append(create_lanternfish(fish_shoal.copy(), 80))

    # Part 2
    result.append(create_lanternfish(fish_shoal.copy(), 256))

    with open("output.txt", "w") as f:
        for i in result:
            f.write(f"{i}\n")


if __name__ == "__main__":
    main()
