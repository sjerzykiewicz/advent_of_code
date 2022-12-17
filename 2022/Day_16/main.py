class Valve:
    def __init__(self, name, flow_rate, leads_to):
        self.name = name
        self.flow_rate = flow_rate
        self.leads_to = leads_to

    def __str__(self):
        str = f"Valve: {self.name}, {self.flow_rate}; Leads to:"
        for x in self.leads_to:
            str += f"\n-{x.name}"
        return str

    def find_valves(self, valves):
        valve_list = []
        for v in self.leads_to:
            for valve in valves:
                if v == valve.name:
                    valve_list.append(valve)
                    break
        self.leads_to = valve_list


def find_valve(name, valves):
    for valve in valves:
        if name == valve.name:
            return valve


def calc_distances(valves):
    key_valves = {v for v in valves if v.flow_rate > 0 or v.name == "AA"}
    distances = {}

    for valve in valves:
        if valve not in key_valves:
            continue
        curr, next, dist = (
            set([valve]),
            set(),
            0,
        )
        distances[(valve, valve)] = 0
        while curr:
            dist += 1
            for val in curr:
                for v in val.leads_to:
                    if (valve, v) not in distances:
                        distances[(valve, v)] = dist
                        next.add(v)
            curr, next = next, set()

    return distances, key_valves


def best_total_flow(curr, minutes, visited, targets, distances):
    visited = visited | {curr}
    targets = targets - visited

    best_flow = 0
    for target in targets:
        minutes_left = minutes - distances[(curr, target)] - 1
        if minutes_left > 0:
            flow = target.flow_rate * minutes_left
            flow += best_total_flow(target, minutes_left, visited, targets, distances)
            if flow > best_flow:
                best_flow = flow
    return best_flow


def main():
    valves = []
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip("\n").split(" ")
            valve = line[1]
            flow_rate = int(line[4].strip(";").split("=")[1])
            leads_to = [x.strip(",") for x in line[9:]]
            valves.append(Valve(valve, flow_rate, leads_to))

    for valve in valves:
        valve.find_valves(valves)

    result = []

    # Part 1
    distances, key_valves = calc_distances(valves)
    result.append(
        best_total_flow(find_valve("AA", valves), 30, set(), key_valves, distances)
    )

    # Part 2

    with open("output.txt", "w") as f:
        for i in result:
            f.write(f"{i}\n")


if __name__ == "__main__":
    main()
