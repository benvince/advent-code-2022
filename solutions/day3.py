import string
SOLUTION_DATA = 'data/day3'

LETTERS = string.ascii_lowercase + string.ascii_uppercase

def get_data():

    data_rows = open(SOLUTION_DATA).read().split("\n")

    return data_rows

def day_3_1():

    score = 0 
    for row in get_data():
        first_half = row[:len(row)//2]
        second_half = row[len(row)//2:]

        for c in first_half:
            if c in second_half:
                score += LETTERS.find(c)+1
                break

    return score

def day_3_2():

    data = get_data()

    score = 0
    for i in range(0,len(data),3): 
        common = set.intersection(*map(set,data[i:i+3]))
        score += LETTERS.find(common.pop()) + 1

    return score 

print(f"Solution 1 Answer: {day_3_1()}.")
print(f"Solution 2 Answer: {day_3_2()}.")
