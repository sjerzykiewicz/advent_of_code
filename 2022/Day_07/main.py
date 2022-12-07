class File:
    def __init__(self, name, parent, size, type):
        self.name = name
        self.parent = parent
        self.size = size
        self.type = type
        self.sons = []

    def addSon(self, son):
        self.sons.append(son)


def main():
    lines = []
    with open("input.txt", "r") as f:
        for line in f:
            lines.append(line.strip("\n"))

    result = []

    # Part 1
    tree = []
    currentDir = File(None, None, None, None)
    new = File("/", currentDir, 0, "dir")
    tree.append(new)
    currentDir.addSon(new)
    for line in lines:
        if line[0] == "$":
            if len(line.split(" ")) == 3:
                _, _, dir = line.split(" ", 3)
                if dir == "..":
                    currentDir = currentDir.parent
                else:
                    currentDir = [x for x in currentDir.sons if x.name == dir][0]
            else:
                continue
        else:
            info, name = line.split(" ", 2)
            if info == "dir":
                new = File(name, currentDir, 0, "dir")
                tree.append(new)
                currentDir.addSon(new)
            else:
                new = File(name, currentDir, int(info), "file")
                tree.append(new)
                par = currentDir
                while par.parent != None:
                    par.size += int(info)
                    par = par.parent
                currentDir.addSon(new)

    size_sum = 0
    for file in tree:
        if file.type == "dir" and file.size <= 100000:
            size_sum += file.size
    result.append(size_sum)

    # Part 2
    disk_space = 70000000
    need = 30000000
    used = tree[0].size
    free_space = disk_space - used
    to_delete = need - free_space
    min = used

    for file in tree:
        if file.type == "dir":
            if file.size < min and file.size > to_delete:
                min = file.size
    result.append(min)

    with open("output.txt", "w") as f:
        for i in result:
            f.write(f"{i}\n")


if __name__ == "__main__":
    main()
