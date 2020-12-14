import re


file = open("input.txt", "r")
content = file.read()
content = content.split("\n")


def initalize():
    memory = {}
    mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    for instruction in content:
        if instruction.startswith("mask"):
            mask = instruction[7:]
        else:
            # Store first matching string.
            index = int(re.findall("\[(.*?)\]", instruction)[0])
            mem_val = "{0:036b}".format(int(instruction.split(" = ")[1]))
            for i, j in enumerate(mask):
                if j == "0":
                    mem_val = mem_val[:i] + "0" + mem_val[i + 1 :]
                elif j == "1":
                    mem_val = mem_val[:i] + "1" + mem_val[i + 1 :]
            memory[index] = mem_val
    return memory


def initalize_2():
    memory = {}
    mask = "000000000000000000000000000000000000"
    for instruction in content:
        if instruction.startswith("mask"):
            mask = instruction[7:]
        else:
            # Store first matching string.
            index = "{0:036b}".format(int(re.findall("\[(.*?)\]", instruction)[0]))
            for i, j in enumerate(mask):
                if j == "X":
                    index = index[:i] + "X" + index[i + 1 :]
                elif j == "1":
                    index = index[:i] + "1" + index[i + 1 :]
            addresses = get_addresses(index.split("X"))
            mem_val = "{0:036b}".format(int(instruction.split(" = ")[1]))
            for address in addresses:
                index = int(address, 2)
                memory[index] = mem_val
    return memory


def get_addresses(addr_parts):
    addresses = []
    address = addr_parts[0]
    if len(addr_parts) == 1:
        return addr_parts
    elif len(addr_parts) == 2:
        addresses.append(address + "0" + addr_parts[1])
        addresses.append(address + "1" + addr_parts[1])
    else:
        sub = get_addresses(addr_parts[1:])
        for i in sub:
            addresses.append(address + "0" + i)
            addresses.append(address + "1" + i)
    return addresses


def sum_all_values(memory):
    amount = 0
    for i in memory.values():
        amount += int(i, 2)
    return amount


print(sum_all_values(initalize()))
print(sum_all_values(initalize_2()))
