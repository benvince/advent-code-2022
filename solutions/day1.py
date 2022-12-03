SOLUTION_DATA = 'data/day1'

def get_cals():

    data_groups = open(SOLUTION_DATA).read().split("\n\n")

    return [[int(x) for x in grp.split("\n")] for grp in data_groups]

def day_1_1():

    group_sums = sorted([sum(x) for x in get_cals()],reverse=True)
    return group_sums[0]

def day_1_2():

    group_sums = sorted([sum(x) for x in get_cals()],reverse=True)
    return sum(group_sums[0:3])

print(f"Solution 1 Answer: {day_1_1()}.")
print(f"Solution 2 Answer: {day_1_2()}.")