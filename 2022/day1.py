def part1():
    with open("input") as f:
        fr = f.read().split("\n\n")
        l = []
        for i in fr:
            i = i.split("\n")
            x = 0
            for j in i: x += int(j)
            l.append(x)
    return max(l)


def part2():
    with open("input") as f:
        fr = f.read().split("\n\n")
        l=[]
        for i in fr:
            i=i.split("\n")
            x=0
            for j in i: x+=int(j)
            l.append(x)
        l=sorted(l)
        return sum(l[-3:])
