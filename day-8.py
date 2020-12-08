file = open("input.txt", "r")
content = file.read()
content = content.split("\n")


def run_instructions(instructions):
    i = 0
    run_actions = []
    accumulator = 0
    loop = False
    while i < len(instructions) and i not in run_actions:
        run_actions.append(i)
        if instructions[i][0:3] == "nop":
            i += 1
        elif instructions[i][0:3] == "acc":
            if instructions[i][4] == "+":
                accumulator += int(instructions[i][5:])
            else:
                accumulator -= int(instructions[i][5:])
            i += 1
        elif instructions[i][0:3] == "jmp":
            if instructions[i][4] == "+":
                i += int(instructions[i][5:])
            else:
                i -= int(instructions[i][5:])
        if i in run_actions:
            loop = True
    return accumulator, loop


def find_fix():
    i = 0
    # Brute force by replacing each instance and then checking if loop is false.
    while i < len(content):
        if content[i][0:3] == "nop" or content[i][0:3] == "jmp":
            new_instructions = content.copy()
            # Swap around jmp and nop using tmp as a temporary string while replacing.
            new_instructions[i] = (
                new_instructions[i]
                .replace("nop", "tmp")
                .replace("jmp", "nop")
                .replace("tmp", "jmp")
            )
            results = run_instructions(new_instructions)
            if results[1] == False:
                return results
        i += 1


print(run_instructions(content))
print(find_fix())
