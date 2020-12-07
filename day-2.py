file = open("input.txt", "r")
content = file.read()
content = content.split("\n")


def check_valid_1():
    valid = 0
    for pword in content:
        temp = pword.split("-")
        charMin = int(temp[0])
        temp = temp[1].split(" ")
        charMax = int(temp[0])
        char = temp[1][0]
        toCheck = temp[2]
        amount = 0
        for i in toCheck:
            if i == char:
                amount += 1
        if charMin <= amount and amount <= charMax:
            valid += 1
    return valid


def check_valid_2():
    valid = 0
    for pword in content:
        temp = pword.split("-")
        pos1 = int(temp[0])
        temp = temp[1].split(" ")
        pos2 = int(temp[0])
        char = temp[1][0]
        toCheck = temp[2]
        amount = 0
        if toCheck[pos1 - 1] == char:
            amount += 1
        if toCheck[pos2 - 1] == char:
            amount += 1
        if amount == 1:
            valid += 1
    return valid


print(check_valid_1())
print(check_valid_2())
