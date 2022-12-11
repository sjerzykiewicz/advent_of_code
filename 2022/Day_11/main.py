class Monkey:
    def __init__(self, items, operation, test, true, false):
        self.items = [int(x) for x in items]
        self.operation = operation
        self.test = int(test)
        self.true = int(true)
        self.false = int(false)
        self.inspected_items = 0

    def addItem(self, item):
        self.items.append(item)

    def getItem(self):
        item = self.items[0]
        self.items = self.items[1:]
        return item

    def calc_worry_level(self, old):
        # Not a safe way
        return eval(self.operation)


def monkey_business(monkeys, rounds, worried=False):
    lcm = 1
    for monkey in monkeys:
        lcm *= monkey.test

    for _ in range(rounds):
        for monkey in monkeys:
            for _ in monkey.items:
                worry_lvl = monkey.getItem()
                worry_lvl = monkey.calc_worry_level(worry_lvl)
                worry_lvl = worry_lvl % lcm if worried else worry_lvl // 3
                dest = monkey.true if worry_lvl % monkey.test == 0 else monkey.false
                monkeys[dest].addItem(worry_lvl)
                monkey.inspected_items += 1

    inspects = []
    for monkey in monkeys:
        inspects.append(monkey.inspected_items)

    inspects.sort(reverse=True)
    return inspects[0] * inspects[1]


def main():
    lines = []
    with open("input.txt", "r") as f:
        i = 0
        for line in f:
            lines.append(line.strip("\n"))

    monkeys_1 = []
    monkeys_2 = []
    for i in range(0, len(lines), 7):
        items = lines[i + 1].replace(",", "").split(" ")[4:]
        operation = lines[i + 2][19:]
        test = lines[i + 3].split(" ")[-1]
        true = lines[i + 4].split(" ")[-1]
        false = lines[i + 5].split(" ")[-1]
        monkeys_1.append(Monkey(items, operation, test, true, false))
        monkeys_2.append(Monkey(items, operation, test, true, false))

    result = []

    # Part 1
    result.append(monkey_business(monkeys_1, 20))

    # Part 2
    result.append(monkey_business(monkeys_2, 10000, True))

    with open("output.txt", "w") as f:
        for i in result:
            f.write(f"{i}\n")


if __name__ == "__main__":
    main()
