file = open("input.txt", "r")
content = file.read()
content = content.split("\n\n")


def count_yes():
    i = 0
    part_one = []
    while i < len(content):
        part_one.append(removeDup(content[i].replace("\n", "")))
        i += 1
    amount = 0
    for i in part_one:
        amount += len(i)
    return amount


def count_everyone_yes():
    amount = 0
    for i in content:
        group = i.split("\n")
        amount += len(commonChars(group))
    return amount


def removeDup(str):
    return "".join(set(str))


def commonChars(list):
    from collections import Counter

    counts = Counter(list[0])
    for str in list:
        counts &= Counter(str)

    res = []
    for letter, count in counts.items():
        res += [letter] * count
    return res


print(count_yes())
print(count_everyone_yes())
