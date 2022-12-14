def generate_rocks(rocks, line, max_y, min_x, max_x):
    path = line.split(" -> ")
    for i in range(len(path) - 1):
        x1, y1 = path[i].split(",")
        x2, y2 = path[i + 1].split(",")
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        sx = 1 if x1 <= x2 else -1
        sy = 1 if y1 <= y2 else -1
        for x in range(x1, x2 + sx, sx):
            for y in range(y1, y2 + sy, sy):
                rocks.add((x, y))
                if y > max_y:
                    max_y = y
            if x > max_x:
                max_x = x
            if x < min_x:
                min_x = x
    return rocks, max_y, min_x, max_x     


def pour_the_sand(rocks, source_x, source_y, max_y, sand, not_a_source=False, part_2=False):
    while True:
        x = source_x
        y = source_y
        if (source_x, source_y) in sand:
            break
        while (x, y + 1) not in rocks and (x, y + 1) not in sand:
            y += 1
            if not part_2:
                if (y > max_y):
                    return sand, True
        if (x - 1, y + 1) not in rocks and (x - 1, y + 1) not in sand:
            sand, check = pour_the_sand(rocks, x - 1, y + 1, max_y, sand, True, part_2)
            if check:
                break
        elif (x + 1, y + 1) not in rocks and not (x + 1, y + 1) in sand:
            sand, check = pour_the_sand(rocks, x + 1, y + 1, max_y, sand, True, part_2)
            if check:
                break
        else:
            sand.add((x, y))
            if not_a_source:
                return sand, False
    return sand, True


def main():
    rocks = set()
    max_y = 0
    min_x = 1000
    max_x = 0
    with open("input.txt", "r") as f:
        for line in f:
            rocks, max_y, min_x, max_x = generate_rocks(rocks, line.strip("\n"), max_y, min_x, max_x)
    
    result = []
    
    sand_source = (500, 0)
    x, y = sand_source
    
    # Part 1
    sand = set()
    sand, _ = pour_the_sand(rocks, x, y, max_y, sand)
    result.append(len(sand))
    
    # Part 2
    for xr in range(min_x - 1000, max_x + 1001):
        rocks.add((xr, max_y + 2))
    
    sand = set()
    sand, _ = pour_the_sand(rocks, x, y, max_y, sand, part_2=True)
    result.append(len(sand))
    
    
    with open("output.txt", "w") as f:
        for i in result:
            f.write(f"{i}\n")



if __name__ == "__main__":
    main()
