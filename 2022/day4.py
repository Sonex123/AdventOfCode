def part1():
    with open("input") as f:
        fr = f.read().split("\n")
    x = 0
    for i in fr:
        ranges = i.split(",")
        elv1 = list(range(int(ranges[0].split("-")[0]), int(ranges[0].split("-")[1]) + 1))
        elv2 = list(range(int(ranges[1].split("-")[0]), int(ranges[1].split("-")[1]) + 1))
        y = 1
        for j in elv1:
            if j not in elv2:
                y = 0
        if not y:
            y = 1
            for j in elv2:
                if j not in elv1:
                    y = 0
        if y:
            x += 1
    return x


def part2():
    with open("input") as f:
        fr = f.read().split("\n")
    x = 0
    for i in fr:
        ranges = i.split(",")
        elv1 = list(range(int(ranges[0].split("-")[0]), int(ranges[0].split("-")[1]) + 1))
        elv2 = list(range(int(ranges[1].split("-")[0]), int(ranges[1].split("-")[1]) + 1))
        for j in elv1:
            if j in elv2:
                x += 1
                break
    return x
