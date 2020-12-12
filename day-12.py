file = open("input.txt", "r")
content = file.read()
content = content.split("\n")


def process_instructions(lines):
    instructions = []
    for i in lines:
        instructions.append([i[0], int(i[1:])])
    return instructions


def find_manhattan_distance():
    coords = [0, 0]
    deg = 90  # Start facing east.
    x_or_y = 0  # 0 is x, 1 is y
    facing = 1  # 1 is up/right, -1 is down/left
    instructions = process_instructions(content)
    for i in instructions:
        if deg == 0:
            x_or_y = 1
            facing = 1
        elif deg == 180:
            x_or_y = 1
            facing = -1
        elif deg == 90:
            x_or_y = 0
            facing = 1
        elif deg == 270:
            x_or_y = 0
            facing = -1
        if i[0] == "N":
            coords[1] += i[1]
        elif i[0] == "S":
            coords[1] -= i[1]
        elif i[0] == "E":
            coords[0] += i[1]
        elif i[0] == "W":
            coords[0] -= i[1]
        elif i[0] == "F":
            coords[x_or_y] += i[1] * facing
        elif i[0] == "L":
            deg -= i[1]
        elif i[0] == "R":
            deg += i[1]
        if deg < 0 or deg >= 360:
            deg = deg % 360
    return abs(coords[0]) + abs(coords[1])


def find_manhattan_distance_waypoint():
    waypoint_coords = [10, 1]  # Waypont starts 10 east, 1 north.
    coords = [0, 0]
    instructions = process_instructions(content)
    for i in instructions:
        if i[0] == "N":
            waypoint_coords[1] += i[1]
        elif i[0] == "S":
            waypoint_coords[1] -= i[1]
        elif i[0] == "E":
            waypoint_coords[0] += i[1]
        elif i[0] == "W":
            waypoint_coords[0] -= i[1]
        elif i[0] == "F":
            coords[0] += waypoint_coords[0] * i[1]
            coords[1] += waypoint_coords[1] * i[1]
        elif i[0] == "L" or i[0] == "R":
            facing = 1 if i[0] == "R" else -1
            new_x, new_y = waypoint_coords
            if i[1] == 90:
                new_x = waypoint_coords[1] * facing  # -y * facing
                new_y = -waypoint_coords[0] * facing
            if i[1] == 180:
                new_x = -waypoint_coords[0]
                new_y = -waypoint_coords[1]
            if i[1] == 270:
                new_x = -waypoint_coords[1] * facing
                new_y = waypoint_coords[0] * facing
            waypoint_coords = [new_x, new_y]
    return abs(coords[0]) + abs(coords[1])


print(find_manhattan_distance())
print(find_manhattan_distance_waypoint())