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
    with open("input") as f:
        fr = f.read().split("\n")

    oxygen = fr
    co2 = fr

    for i in range(len(fr[0])):
        c1 = 0
        c0 = 0
        for j in fr:
            if j[i] == "0":
                c0 += 1
            else:
                c1 += 1
        common = "1"
        if c0 > c1:
            common = "0"

        if common == "0":
            least = "1"
        else:
            least = "0"
        for j in oxygen:
            if j[i] == least and len(oxygen) != 1:
                oxygen.remove(j)
        for j in co2:
            if j[i] == common and len(co2) != 1:
                co2.remove(j)
        print(i,c1,c0, least, common)
        print(oxygen)
        print(co2)

    return int(oxygen[0],2) * int(co2[0],2)


print(part2())
