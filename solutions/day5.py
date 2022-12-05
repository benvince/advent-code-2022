import utils
SOLUTION_DATA = 'data/day5'
class Stack():

    def __init__(self, start_state=[]):
        self.state = start_state

    def move_to_stack(self, no_items, stack, solution2=False):

        stack.add_items(self.state[:no_items], solution2)
        self.state = self.state[no_items:]

    def add_items(self, items, solution_2):
        
        if solution_2:
            direction = -1
        else:
            direction = 1

        for i in items[::direction]:
            self.state.insert(0, i)

def define_stack():
    return {"1": Stack(["T","R","D","H","Q","N","P","B"]),
            "2": Stack(["V","T","J","B","G","W"]),
            "3": Stack(["Q","M","V","S","D","H","R","N"]),
            "4": Stack(["C","M","N","Z","P"]),
            "5": Stack(["B","Z","D"]),
            "6": Stack(["Z","W","C","V"]),
            "7": Stack(["S","L","Q","V","C","N","Z","G"]),
            "8": Stack(["V","N","D","M","J","G","L"]),
            "9": Stack(["G","C","Z","F","M","P","T"])}

def day_5(solution_2=False):

    data = utils.get_data(SOLUTION_DATA)

    for row in data:
        if row.startswith("move"):
            words = row.split(" ")
            stacks[words[3]].move_to_stack(int(words[1]), stacks[words[5]], solution_2)

    output = ""
    for stack in stacks:
        output += stacks[stack].state[0]

    return output

stacks = define_stack()
print(f"Solution 1 Answer: {day_5(False)}.")
stacks = define_stack()
print(f"Solution 2 Answer: {day_5(True)}.")