file = open("input.txt", "r")
content = file.read()
content = content.split("\n")


def count_trees(right, down):
    line_length = len(content[0])
    amount = 0
    x = 0
    y = 0
    while y < len(content):
        if content[y][x] == "#":
            amount += 1
        x += right
        y += down
        if x >= line_length:
            x -= line_length
    return amount


print(count_trees(3, 1))
print(
    count_trees(1, 1)
    * count_trees(3, 1)
    * count_trees(5, 1)
    * count_trees(7, 1)
    * count_trees(1, 2)
)
