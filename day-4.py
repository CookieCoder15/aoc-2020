import re

file = open("input.txt", "r")
content = file.read()
content = content.split("\n\n")


def count_valid(to_check, to_ignore):
    checks = [x for x in to_check if x not in to_ignore]
    amount = len(content)
    for i in content:
        user = i.replace("\n", " ")
        fields = user.split(" ")
        x = 0
        while x < len(fields):
            fields[x] = fields[x][0:3]
            x += 1
        for check in checks:
            if check not in fields:
                amount -= 1
                break
    return amount


def count_valid_2(to_check, to_ignore):
    checks = [x for x in to_check if x not in to_ignore]
    amount = len(content)
    for i in content:
        fields_string = i.replace("\n", " ").split(" ")
        fields = {}
        for field in fields_string:
            fields[field.split(":")[0]] = field.split(":")[1]
        valid = True
        for check in checks:
            if check not in fields.keys():
                valid = False
                break
        if valid == True:
            if int(fields["byr"]) < 1920 or int(fields["byr"]) > 2002:
                valid = False
            elif int(fields["iyr"]) < 2010 or int(fields["iyr"]) > 2020:
                valid = False
            elif int(fields["eyr"]) < 2020 or int(fields["eyr"]) > 2030:
                valid = False
            elif fields["hgt"][-2:] != "cm" and fields["hgt"][-2:] != "in":
                valid = False
            elif fields["hgt"][-2:] == "cm" and (int(fields["hgt"][:-2]) < 150 or int(fields["hgt"][:-2]) > 193):
                valid = False
            elif fields["hgt"][-2:] == "in" and (int(fields["hgt"][:-2]) < 59 or int(fields["hgt"][:-2]) > 76):
                valid = False
            elif not re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', fields["hcl"]):
                valid = False
            elif fields["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                valid = False
            elif len(fields["pid"]) != 9:
                valid = False
        if valid == False:
            amount -= 1
    return amount


to_check = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
to_ignore = ["cid"]
print(count_valid(to_check, to_ignore))
print(count_valid_2(to_check, to_ignore))
