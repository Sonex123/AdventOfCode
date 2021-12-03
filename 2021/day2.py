def part1():
    with open("input") as f:
        fr = f.read().split("\n")
    x = 0
    y = 0
    for line in fr:
        line = line.split()
        task = line[0]
        val = int(line[1])
        if task == "forward":
            x += val
        elif task == "up":
            y -= val
        elif task == "down":
            y += val

    return x * y


def part2():
    with open("input") as f:
        fr = f.read().split("\n")
    x = 0
    y = 0
    aim = 0
    for line in fr:
        line = line.split()
        task = line[0]
        val = int(line[1])
        if task == "forward":
            x += val
            if aim != 0:
                y += val * aim
        elif task == "up":
            aim -= val
        elif task == "down":
            aim += val

    return x * y
