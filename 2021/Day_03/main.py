import numpy as np


def arr_tester(array, t):
    arr = np.array(list(map(sum, zip(*array))))
    if t == 1:
        arr[arr < len(array) / 2] = 0
        arr[arr >= len(array) / 2] = 1
    else:
        arr[arr < len(array) / 2] = 1
        arr[arr >= len(array) / 2] = 0
    return arr


def arr_find(array, t):
    n, m = array.shape
    j = 0
    while j < m:
        i = 0
        tester = arr_tester(array, t)
        while i < n & n > 1:
            if array[i, j] != tester[j]:
                array = np.delete(array, i, 0)
                n, m = array.shape
                i -= 1
            i += 1
        j += 1
    return array[n - 1]


def main():
    result = []

    binary = []
    with open("input.txt", "r") as f:
        for line in f:
            new_list = list(line)
            binary.append([int(x) for x in new_list[:-1]])

    # Part 1
    # Gamma rate
    gamma_arr = arr_tester(binary.copy(), 1)
    gamma_rate = int("".join(str(x) for x in gamma_arr), 2)

    # Epsilon rate
    epsilon_arr = arr_tester(binary.copy(), 0)
    epsilon_rate = int("".join(str(x) for x in epsilon_arr), 2)

    result.append(str(gamma_rate * epsilon_rate))

    # Part 2
    oxygen_arr = arr_find(np.array(binary), 1)
    oxygen = int("".join(str(x) for x in oxygen_arr), 2)

    co2_arr = arr_find(np.array(binary), 0)
    co2 = int("".join(str(x) for x in co2_arr), 2)

    result.append(str(oxygen * co2))

    with open("output.txt", "w") as f:
        for i in result:
            f.write(f"{i}\n")


if __name__ == "__main__":
    main()
