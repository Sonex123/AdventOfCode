def part1():
    with open("input") as f:
        fr = f.read().split("\n")
        x = 0
        for i in fr:
            i = i.split()
            a, b = i[0], i[1]
            if b == "X": x += 1
            if b == "Y": x += 2
            if b == "Z": x += 3

            if a == b.replace("X", "A").replace("Y", "B").replace("Z", "C"): x += 3
            if a == "A" and b == "Y": x += 6
            if a == "B" and b == "Z": x += 6
            if a == "C" and b == "X": x += 6
        return x


def part2():
    with open("input") as f:
        fr = f.read().split("\n")
        x = 0
        for i in fr:
            i = i.split()
            a, b = i[0], i[1]
            if b == "X":
                if a == "A": x += 3
                if a == "B": x += 1
                if a == "C": x += 2
            if b == "Y":
                if a == "A": x += 4
                if a == "B": x += 5
                if a == "C": x += 6

            if b == "Z":
                if a == "A": x +=6+2
                if a == "B": x +=6+3
                if a == "C": x +=6+1

        return x
