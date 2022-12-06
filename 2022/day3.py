from string import ascii_letters as l


def part1():
    with open("input") as f:
        fr = f.read().split("\n")
    x = 0
    for i in fr:
        c1 = i[:len(i) // 2]
        c2 = i[len(i) // 2:]
        for j in c1:
            if j in c2:
                x += l.index(j) + 1
                break
    return x


def part2():
    with open("input") as f:
        fr = f.read().split("\n")
    x = 0
    for i in range(0, len(fr), 3):
        for j in fr[i]:
            if j in fr[i + 1] and j in fr[i + 2]:
                x += l.index(j) + 1
                break
    return x
