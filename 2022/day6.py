def part1():
    with open("input") as f:
        fr = f.read()
    for i in range(13, len(fr), 1):
        x = fr[i] + fr[i - 1] + fr[i - 2] + fr[i - 3]
        c = 1
        for j in x:
            if x.count(j) != 1:
                c = 0
                break
        if c:
            return i + 1


def part2():
    with open("input") as f:
        fr = f.read()
    for i in range(13, len(fr), 1):
        x = fr[i] + fr[i - 1] + fr[i - 2] + fr[i - 3] + fr[i - 4] + fr[i - 5] + fr[i - 6] + fr[i - 7] + fr[i - 8] + fr[i - 9] + fr[i - 10] + fr[i - 11] + fr[i - 12] + fr[i - 13]
        c = 1
        for j in x:
            if x.count(j) != 1:
                c = 0
                break
        if c:
            return i + 1
