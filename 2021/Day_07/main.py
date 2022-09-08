import numpy as np


def main():
    result = []

    with open("input.txt", "r") as f:
        crabs = [int(i) for i in f.readline().split(",")]

    max_crab_pos = max(crabs)
    min_crab_pos = min(crabs)

    # Part 1
    fuel = np.zeros(max_crab_pos + 1, dtype=int)
    for i in range(len(fuel)):
        for crab in crabs:
            fuel[i] += abs(crab - i)

    result.append(min(fuel))

    # Part 2
    fuel = np.zeros(max_crab_pos + 1, dtype=int)
    for i in range(len(fuel)):
        for crab in crabs:
            fuel[i] += (lambda x: x * (x + 1) / 2)(abs(crab - i))

    result.append(min(fuel))

    with open("output.txt", "w") as f:
        for i in result:
            f.write(f"{i}\n")


if __name__ == "__main__":
    main()
