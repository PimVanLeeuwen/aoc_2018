def solve_part1(input_data):
    exactly_two = 0
    exactly_three = 0

    for id in input_data.split("\n"):
        two, three = False, False

        # Check the requirements for the IDs
        # Added requirements for the counting only once per id
        for c in set(id):
            if id.count(c) == 2 and two == False:
                two = True
                exactly_two += 1
            if id.count(c) == 3 and three == False:
                three = True
                exactly_three += 1

    # return checksum
    return exactly_two * exactly_three

# Function to check if two ids are similar, returns the id of the one dissimilarity if that is present
def similar_inputs(a, b):
    one_off = -1
    for i, c in enumerate(a):
        if c != b[i] and one_off == -1:
            one_off = i
        elif c != b[i]:
            return -1
    return one_off

def solve_part2(input_data):
    for id1 in input_data.split("\n"):
        for id2 in input_data.split("\n"):
            if id1 == id2:
                continue

            #  remove similar without additional char
            if similar_inputs(id1, id2) != -1:
                i = similar_inputs(id1, id2)
                return f"{id1[:i] + id1[i+1:]}"

    return None