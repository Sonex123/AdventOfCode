def part1():
    with open("input") as f:
        fr = f.read().split("\n")
    c = 0
    cur = 0
    for i in fr:
        if int(i) > cur:
            c += 1
        cur = int(i)

    return c - 1


def part2():
    with open("input") as f:
        fr = [int(i) for i in f.read().split("\n")]
    cur = 0
    c = 0
    for i in range(3, len(fr)+1):
        s = sum(fr[i - 3:i])
        if cur < s:
            c += 1
        cur = s

    return c - 1
