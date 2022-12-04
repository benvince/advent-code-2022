import utils
SOLUTION_DATA = 'data/day4'

def day_4_1():

    data = utils.get_data(SOLUTION_DATA)

    score = 0 
    for row in data:

        rng1 = [int(x) for x in row.split(",")[0].split("-")]
        rng2 = [int(x) for x in row.split(",")[1].split("-")]

        if (rng1[0] >= rng2[0] and rng1[1] <= rng2[1]) or rng2[0] >= rng1[0] and rng2[1] <= rng1[1]:
            score += 1

    return score

print(f"Solution 1 Answer: {day_4_1()}.")
