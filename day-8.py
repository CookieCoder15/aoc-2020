file = open("input.txt", "r")
content = file.read()
content = content.split("\n")


def run_instructions(instructions):
    i = 0
    run_actions = []
    accumulator = 0
    will_loop = False  # Loop variable used in part 2.
    while i < len(instructions) and not will_loop:
        run_actions.append(i)
        if instructions[i][0:3] == "nop":
            i += 1
        elif instructions[i][0:3] == "acc":
            accumulator += int(instructions[i][4:])
            i += 1
        elif instructions[i][0:3] == "jmp":
            i += int(instructions[i][4:])
        if i in run_actions:
            will_loop = True
    return accumulator, will_loop


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
