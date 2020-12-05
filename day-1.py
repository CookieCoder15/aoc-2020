file = open("input.txt", "r")
content = file.read()
content = content.split("\n")


def sum_2():
    for x in content:
        for y in content:
            if int(x) + int(y) == 2020:
                return int(x)*int(y)


def sum_3():
    for x in content:
        for y in content:
            for z in content:
                if int(x) + int(y) + int(z) == 2020:
                    return int(x)*int(y)*int(z)


print("Part 1: " + str(sum_2()))
print("Part 2: " + str(sum_3()))
