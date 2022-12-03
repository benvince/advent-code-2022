from typing import List

SOLUTION_DATA = 'data/day1'

def get_cals() -> List[int]:

    data_groups = open(SOLUTION_DATA).read().split("\n\n")

    output = []
    for grp in data_groups:
        output.append([int(x) for x in grp.split("\n") if not x == ""])

    return output

def day_1_1():

    group_sums = sorted([sum(x) for x in get_cals()],reverse=True)
    return group_sums[0]

def day_1_2():

    group_sums = sorted([sum(x) for x in get_cals()],reverse=True)
    return sum(group_sums[0:3])

print(f"Solution 1 Answer: {day_1_1()}.")
print(f"Solution 2 Answer: {day_1_2()}.")