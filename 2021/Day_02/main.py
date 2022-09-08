def main():
    result = []

    # Part 1
    commands = {'forward': 0, 'down': 0, 'up': 0}

    with open("input.txt", "r") as f:
        for line in f:
            k, v = line.split()
            commands[k] += int(v)
    
    result.append(str(commands['forward'] * (commands['down'] - commands['up'])))
    
    # Part 2
    possition = {'horizontal': 0, 'depth': 0, 'aim': 0}

    with open("input.txt", "r") as f:
        for line in f:
            k, v = line.split()
            if k == 'forward':
                possition['horizontal'] += int(v)
                possition['depth'] += int(v) * possition['aim']
            if k == 'down':
                possition['aim'] += int(v)
            if k == 'up':
                possition['aim'] -= int(v)

    result.append(str(possition['horizontal'] * possition['depth']))

    with open("output.txt", "w") as f:
        for i in result:
            f.write(f"{i}\n")


if __name__ == "__main__":
    main()
