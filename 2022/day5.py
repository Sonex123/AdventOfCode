def part1():
    with open("input") as f:
        fr = f.read().split("\n")
    stacks = [["D", "H", "N", "Q", "T", "W", "V", "B"], ["D", "W", "B"], ["T", "S", "Q", "W", "J", "C"],
              ["F", "J", "R", "N", "Z", "T", "P"], ["G", "P", "V", "J", "M", "S", "T"], ["B", "W", "F", "T", "N"],
              ["B", "L", "D", "Q", "F", "H", "V", "N"], ["H", "P", "F", "R"], ["Z", "S", "M", "B", "L", "N", "P", "H"]]

    for i in fr:
        x = i.replace("move ", "").replace(" from", "").replace(" to", "").split()
        f = int(x[1]) - 1
        t = int(x[2]) - 1
        for _ in range(int(x[0])):
            stacks[t].append(stacks[f][-1])
            stacks[f].pop()

    return "".join(i[-1] for i in stacks)


def part2():
    with open("input") as f:
        fr = f.read().split("\n")
    stacks = [["D", "H", "N", "Q", "T", "W", "V", "B"], ["D", "W", "B"], ["T", "S", "Q", "W", "J", "C"],
              ["F", "J", "R", "N", "Z", "T", "P"], ["G", "P", "V", "J", "M", "S", "T"], ["B", "W", "F", "T", "N"],
              ["B", "L", "D", "Q", "F", "H", "V", "N"], ["H", "P", "F", "R"], ["Z", "S", "M", "B", "L", "N", "P", "H"]]

    for i in fr:
        x = i.replace("move ", "").replace(" from", "").replace(" to", "").split()
        v = int(x[0])
        f = int(x[1]) - 1
        t = int(x[2]) - 1
        while v != 0:
            stacks[t].append(stacks[f][-v])
            del stacks[f][-v]
            v -= 1

    return "".join(i[-1] for i in stacks)
