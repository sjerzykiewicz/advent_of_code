import re


def manhattan_dist(point_1, point_2):
    return abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1])


class Sensor:
    def __init__(self, pos, beacon_pos):
        self.pos = pos
        self.beacon_dist = manhattan_dist(pos, beacon_pos)


def part_1(sensors, beacons):
    not_a_beacons = set()
    row = 2000000
    for sensor in sensors:
        curr_x = sensor.pos[0]
        dist = manhattan_dist((curr_x, row), sensor.pos)
        while dist <= sensor.beacon_dist:
            not_a_beacons.add((curr_x, row))
            curr_x -= 1
            dist += 1

        curr_x = sensor.pos[0]
        dist = manhattan_dist((curr_x, row), sensor.pos)
        while dist <= sensor.beacon_dist:
            not_a_beacons.add((curr_x, row))
            curr_x += 1
            dist += 1

    return len(not_a_beacons.difference(beacons))


def main():
    sensors = []
    pattern = re.compile("^.=.+$")
    min_x = float("inf")
    max_x = 0
    beacons = set()
    sensors_s = set()
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip("\n").split(" ")
            line = [x.strip(",").strip(":") for x in line if pattern.match(x)]
            x, y, beacon_x, beacon_y = [int(x.split("=")[1]) for x in line]
            min_x = min(x, beacon_x, min_x)
            max_x = max(x, beacon_x, max_x)
            sensors.append(Sensor((x, y), (beacon_x, beacon_y)))
            beacons.add((beacon_x, beacon_y))
            sensors_s.add((x, y))

    result = []

    # Part 1
    result.append(part_1(sensors, beacons))

    # Part 2

    with open("output.txt", "w") as f:
        for i in result:
            f.write(f"{i}\n")


if __name__ == "__main__":
    main()
