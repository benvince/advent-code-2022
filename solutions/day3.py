import string
SOLUTION_DATA = 'data/day3'

def get_data():

    data_rows = open(SOLUTION_DATA).read().split("\n")

    return data_rows

def day_3_1():

    letters = string.ascii_lowercase + string.ascii_uppercase

    score = 0 
    for row in get_data():
        first_half = row[:len(row)//2]
        second_half = row[len(row)//2:]

        for c in first_half:
            if c in second_half:
                score += letters.find(c)+1
                break

    return score

print(f"Solution 1 Answer: {day_3_1()}.")
