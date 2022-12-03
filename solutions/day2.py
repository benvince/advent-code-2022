
SHAPE_POINTS = {"A": 1, "B": 2, "C": 3, "X": 1, "Y":2, "Z":3}
SHAPE_DEFEATS = {"A": "Z", "B":"X", "C": "Y"}
SHAPE_LOSES = {"A": "B", "B":"C", "C": "A"}
SHAPE_WINS =  {v: k for k, v in SHAPE_LOSES.items()}

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

def day_2_2():

    score = 0
    for x in get_data():
        if x[1] == "X":
            # Lose
            score += SHAPE_POINTS[SHAPE_WINS[x[0]]]
        elif x[1] == "Y":
            # Draw:
            score += SHAPE_POINTS[x[0]] + 3
        else:
            # Win
            score += SHAPE_POINTS[SHAPE_LOSES[x[0]]] + 6

    return score


print(f"Solution 1 Answer: {day_2_1()}.")
print(f"Solution 2 Answer: {day_2_2()}.")
