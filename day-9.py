file = open("input.txt", "r")
content = file.read()
content = content.split("\n")
i = 0
while i < len(content):
    content[i] = int(content[i])
    i += 1


def find_invalid():
    i = 25
    while i < len(content):
        num = content[i]
        valid = False
        for x in content[i - 25 : i]:
            for y in content[i - 25 : i]:
                if x + y == num:
                    valid = True
        if not valid:
            return num
        i += 1


def find_set(invalid):
    x = 0
    while x < len(content):
        y = 0
        num_set = []
        set_sum = 0
        while x + y < len(content):
            set_sum += content[x + y]
            num_set.append(content[x + y])
            if len(num_set) > 1 and set_sum == invalid:
                num_set.sort()
                return num_set[0] + num_set[-1]
            y += 1
        x += 1


invalid = find_invalid()
print(invalid)
print(find_set(invalid))