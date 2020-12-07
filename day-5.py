file = open("input.txt", "r")
content = file.read()
content = content.split("\n")


def get_ids(rows, columns):
    ids = []
    for x in content:
        max_row = rows - 1
        min_row = 0
        max_column = columns - 1
        min_column = 0
        row = 0
        column = 0
        for y in x[0:6]:
            if y == "F":
                max_row -= round((max_row - min_row) / 2)
            else:
                min_row += round((max_row - min_row) / 2)
        if x[6] == "F":
            row = min_row
        else:
            row = max_row
        for y in x[7:9]:
            if y == "L":
                max_column -= round((max_column - min_column) / 2)
            else:
                min_column += round((max_column - min_column) / 2)
        if x[9] == "L":
            column = min_column
        else:
            column = max_column
        ids.append(row * 8 + column)
    ids.sort()
    return ids


def find_highest_id(rows, columns):
    ids = get_ids(rows, columns)
    id = 0
    for i in ids:
        if i > id:
            id = i
    return id


def find_missing_id(rows, columns):
    ids = get_ids(rows, columns)
    id = 0
    i = 0
    while i < len(ids) - 1:
        if ids[i + 1] - ids[i] != 2:
            ids.remove(ids[i])
        else:
            i += 1
    id = ids[0] + 1
    return id


print(find_highest_id(128, 8))
print(find_missing_id(128, 8))
