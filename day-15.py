file = open("input.txt", "r")
content = file.read()
content = content.split(",")

for i, j in enumerate(content):
    content[i] = int(j)


def play_game(turns):
    rounds = {}
    rounds[0] = []  # Setup for first mention of numbers.
    turn = 0
    # Have turns for starting numbers.
    for i in content:
        turn += 1
        rounds[i] = [turn]
    last_spoken = content[-1]
    while turn < turns:
        turn += 1
        if len(rounds[last_spoken]) == 1:
            rounds[0].append(turn)
            last_spoken = 0
        else:
            last_spoken = rounds[last_spoken][-1] - rounds[last_spoken][-2]
            if last_spoken in rounds:
                rounds[last_spoken].append(turn)
            else:
                rounds[last_spoken] = [turn]
    return last_spoken


print(play_game(2020))
print(play_game(30000000))