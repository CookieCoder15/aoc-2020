from sympy.ntheory.modular import crt


file = open("input.txt", "r")
content = file.read()
content = content.split("\n")


def process_data(data):
    earliest = int(data[0])
    ids = []
    for i in data[1].split(","):
        if i != "x":
            ids.append(int(i))
        else:
            ids.append(0)
    return earliest, ids


def find_earliest_bus(data):
    bus_id = 0
    wait = data[0]
    for i in data[1]:
        if i != 0:
            timestamp = 0
            while timestamp < data[0]:
                timestamp += i
            if wait > timestamp - data[0]:
                wait = timestamp - data[0]
                bus_id = i
    return bus_id, wait


def find_earliest_timestamp(data):
    m = []
    v = []
    for i, j in enumerate(data[1]):  # i is index and j is the value.
        if j != 0:
            m.append(j)
            # For example if bus with id 47 is at index 2, it will come 45 mins before timestamp.
            v.append(j - i)
        i += 1
    timestamp = crt(m, v)  # Returns the desired timestamp and the lcm(?)
    return timestamp[0]  # TODO: Read more documentation on sympy.ntheory.modular.crt


data = process_data(content)
earliest_bus = find_earliest_bus(data)
print(earliest_bus[0] * earliest_bus[1])
print(find_earliest_timestamp(data))
