from functools import lru_cache

file = open("input.txt", "r")
content = file.read()
content = content.split("\n")

i = 0
while i < len(content):
    content[i] = int(content[i])
    i += 1
content.sort()


def valid_jump(new, old):
    if new - old <= 3:
        return True
    else:
        return False


def count_jolt_diff(diff):
    joltage = 0
    max_joltage = content[-1] + 3
    amount = 0
    i = 0
    while i < len(content):
        actual_diff = content[i] - joltage
        if actual_diff == diff:
            amount += 1
        joltage = content[i]
        i += 1
    actual_diff = max_joltage - joltage
    if actual_diff == diff:
        amount += 1
    return amount


@lru_cache(maxsize=None)
def count_possibilities(data, max_joltage):
    amount = 0
    i = len(data) - 1
    while i >= 0:
        if max_joltage - data[i] <= 3:
            if 0 - data[i] >= -3:
                amount += 1
            amount += count_possibilities(tuple(data[:i]), data[i])
        i -= 1
    return amount


print(count_jolt_diff(1) * count_jolt_diff(3))
print(count_possibilities(tuple(content), content[-1] + 3))
