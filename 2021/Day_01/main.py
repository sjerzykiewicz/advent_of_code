import numpy as np


def main():
    with open("input.txt", "r") as f:
        nums = np.array([int(i) for i in f.readlines()])

    result = []

    # Part 1
    counter = 0
    for i in range(nums.size - 1):
        if nums[i] < nums[i + 1]:
            counter += 1
    result.append(str(counter))

    # Part 2
    counter = 0
    for i in range(0, nums.size - 3):
        if nums[i : i + 3].sum() < nums[i + 1 : i + 4].sum():
            counter += 1
    result.append(str(counter))

    with open("output.txt", "w") as f:
        for i in result:
            f.write(f"{i}\n")


if __name__ == "__main__":
    main()
