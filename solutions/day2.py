
SHAPE_POINTS = {"A": 1, "B": 2, "C": 3, "X": 1, "Y":2, "Z":3}
SHAPE_DEFEATS = {"A": "Z", "B":"X", "C": "Y"}

SOLUTION_DATA = 'data/day2'

def get_data():

    data_rows = open(SOLUTION_DATA).read().split("\n")

    return [x.replace(" ", "") for x in data_rows]

def day_2_1():

    score = 0
    for x in get_data():
        # Win
        if SHAPE_DEFEATS[x[0]] == x[1]:
            score += SHAPE_POINTS[x[1]] 
        # Draw
        elif SHAPE_POINTS[x[0]] == SHAPE_POINTS[x[1]]:
            score += SHAPE_POINTS[x[1]] + 3
        # Lose
        else:
            score += SHAPE_POINTS[x[1]] + 6 

    return score


print(f"Solution 1 Answer: {day_2_1()}.")