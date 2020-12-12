file = open("input.txt", "r")
content = file.read()
content = content.split("\n")


def count_occupied_seats(current):
    amount = 0
    new = current.copy()
    y = 0
    while y < len(current):
        x = 0
        while x < len(current[y]):
            if current[y][x] == "L" or current[y][x] == "#":
                adjcent = 0
                if y - 1 >= 0 and x - 1 >= 0 and current[y - 1][x - 1] == "#":
                    adjcent += 1
                if y - 1 >= 0 and current[y - 1][x] == "#":
                    adjcent += 1
                if (
                    y - 1 >= 0
                    and x + 1 < len(current[y])
                    and current[y - 1][x + 1] == "#"
                ):
                    adjcent += 1
                if y + 1 < len(current) and x - 1 >= 0 and current[y + 1][x - 1] == "#":
                    adjcent += 1
                if y + 1 < len(current) and current[y + 1][x] == "#":
                    adjcent += 1
                if (
                    y + 1 < len(current)
                    and x + 1 < len(current[y])
                    and current[y + 1][x + 1] == "#"
                ):
                    adjcent += 1
                if x - 1 >= 0 and current[y][x - 1] == "#":
                    adjcent += 1
                if x + 1 < len(current[y]) and current[y][x + 1] == "#":
                    adjcent += 1
                if adjcent == 0 and current[y][x] == "L":
                    new[y] = new[y][:x] + "#" + new[y][x + 1 :]
                elif adjcent >= 4 and current[y][x] == "#":
                    new[y] = new[y][:x] + "L" + new[y][x + 1 :]
            x += 1
        y += 1
    equilibrium = False
    if new == current:
        equilibrium = True
    amount = 0
    for y in new:
        for x in y:
            if x == "#":
                amount += 1
    while not equilibrium:
        equilibrium, amount = count_occupied_seats(new)
    else:
        return equilibrium, amount


def count_occupied_seats_again(current):
    amount = 0
    new = current.copy()
    y = 0
    while y < len(current):
        x = 0
        while x < len(current[y]):
            if current[y][x] == "L" or current[y][x] == "#":
                adjcent = 0
                # Check Up
                y1 = -1
                visible_seat = "."
                while visible_seat == "." and y + y1 >= 0:
                    visible_seat = current[y + y1][x]
                    y1 -= 1
                if visible_seat == "#":
                    adjcent += 1
                # Check Down
                y1 = 1
                visible_seat = "."
                while visible_seat == "." and y + y1 < len(current):
                    visible_seat = current[y + y1][x]
                    y1 += 1
                if visible_seat == "#":
                    adjcent += 1
                # Check Left
                x1 = -1
                visible_seat = "."
                while visible_seat == "." and x + x1 >= 0:
                    visible_seat = current[y][x + x1]
                    x1 -= 1
                if visible_seat == "#":
                    adjcent += 1
                # Check Right
                x1 = 1
                visible_seat = "."
                while visible_seat == "." and x + x1 < len(current[y]):
                    visible_seat = current[y][x + x1]
                    x1 += 1
                if visible_seat == "#":
                    adjcent += 1
                # Check Top Left
                y1 = -1
                x1 = -1
                visible_seat = "."
                while visible_seat == "." and y + y1 >= 0 and x + x1 >= 0:
                    visible_seat = current[y + y1][x + x1]
                    y1 -= 1
                    x1 -= 1
                if visible_seat == "#":
                    adjcent += 1
                # Check Top Right
                y1 = -1
                x1 = 1
                visible_seat = "."
                while visible_seat == "." and y + y1 >= 0 and x + x1 < len(current[y]):
                    visible_seat = current[y + y1][x + x1]
                    y1 -= 1
                    x1 += 1
                if visible_seat == "#":
                    adjcent += 1
                # Check Bottom Left
                y1 = 1
                x1 = -1
                visible_seat = "."
                while visible_seat == "." and y + y1 < len(current) and x + x1 >= 0:
                    visible_seat = current[y + y1][x + x1]
                    y1 += 1
                    x1 -= 1
                if visible_seat == "#":
                    adjcent += 1
                # Check Bottom Right
                y1 = 1
                x1 = 1
                visible_seat = "."
                while (
                    visible_seat == "."
                    and y + y1 < len(current)
                    and x + x1 < len(current[y])
                ):
                    visible_seat = current[y + y1][x + x1]
                    y1 += 1
                    x1 += 1
                if visible_seat == "#":
                    adjcent += 1
                # Make changes
                if adjcent == 0 and current[y][x] == "L":
                    new[y] = new[y][:x] + "#" + new[y][x + 1 :]
                elif adjcent >= 5 and current[y][x] == "#":
                    new[y] = new[y][:x] + "L" + new[y][x + 1 :]
            x += 1
        y += 1
    equilibrium = False
    if new == current:
        equilibrium = True
    amount = 0
    for y in new:
        for x in y:
            if x == "#":
                amount += 1
    while not equilibrium:
        equilibrium, amount = count_occupied_seats_again(new)
    else:
        return equilibrium, amount


print(count_occupied_seats(content))
print(count_occupied_seats_again(content))