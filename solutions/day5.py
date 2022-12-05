import utils
SOLUTION_DATA = 'data/day5'

class Stack():

    def __init__(self, start_state=[]):
        self.state = start_state

    def move_to_stack(self, no_items, stack):

        stack.add_items(self.state[:no_items])
        self.state = self.state[no_items:]

    def add_items(self, items):
        
        for i in items:
            self.state.insert(0, i)

stacks = {"1": Stack(["T","R","D","H","Q","N","P","B"]),
          "2": Stack(["V","T","J","B","G","W"]),
          "3": Stack(["Q","M","V","S","D","H","R","N"]),
          "4": Stack(["C","M","N","Z","P"]),
          "5": Stack(["B","Z","D"]),
          "6": Stack(["Z","W","C","V"]),
          "7": Stack(["S","L","Q","V","C","N","Z","G"]),
          "8": Stack(["V","N","D","M","J","G","L"]),
          "9": Stack(["G","C","Z","F","M","P","T"])}

def day_5_1():

    data = utils.get_data(SOLUTION_DATA)

    for row in data:
        if row.startswith("move"):
            words = row.split(" ")
            stacks[words[3]].move_to_stack(int(words[1]), stacks[words[5]])

    for stack in stacks:
        output += stacks[stack].state[0]

    return output

print(f"Solution 1 Answer: {day_5_1()}.")
# print(f"Solution 2 Answer: {day_4_2()}.")