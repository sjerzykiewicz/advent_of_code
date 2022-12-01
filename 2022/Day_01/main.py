def main():
    with open("input.txt", "r") as f:
        calories = [0]
        i = 0
        for line in f:
            if line == "\n":
                i += 1
                calories.append(0)
            else:
                calories[i] += int(line)
    
    result = []

    # Part 1
    result.append(max(calories))
    
    # Part 2
    calories.sort(reverse=True)
    sum = calories[0] + calories[1] + calories[2]
    result.append(sum)

    with open("output.txt", "w") as f:
        for i in result:
            f.write(f"{i}\n")


if __name__ == "__main__":
    main()