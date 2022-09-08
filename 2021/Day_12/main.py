from collections import defaultdict


def find_paths(current, path):
    if current == "end":
        routes.add(tuple(path))
        return
    for x in paths[current]:
        if (x.islower() and x in path) or x == "start":
            continue
        find_paths(x, path + [x])
    return routes


def find_paths_2(current, path):
    if current == "end":
        routes.add(tuple(path))
        return
    for x in paths[current]:
        if (
            x.islower()
            and x in path
            and any(path.count(y) > 1 for y in path if y.islower())
        ) or x == "start":
            continue
        find_paths_2(x, path + [x])
    return routes


def main():
    result = []

    global paths
    paths = defaultdict(list)
    with open("input.txt", "r") as f:
        for line in f:
            a, b = line[:-1].split("-")
            paths[a] += [b]
            paths[b] += [a]

    global routes
    routes = set()

    # Part 1
    result.append(len(find_paths("start", ["start"])))

    # Part 2
    result.append(len(find_paths_2("start", ["start"])))

    with open("output.txt", "w") as f:
        for i in result:
            f.write(f"{i}\n")


if __name__ == "__main__":
    main()
