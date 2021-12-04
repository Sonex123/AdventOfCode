def part1():
    with open("input") as f:
        fr = f.read().split("\n")

    gamma = ""
    epsilon = ""

    for i in range(len(fr[0])):
        c1 = 0
        c0 = 0
        for j in fr:
            if j[i] == "0":
                c0 += 1
            else:
                c1 += 1
        if c1 > c0:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    return gamma * epsilon


def part2():
    # Failed until moment
    pass
