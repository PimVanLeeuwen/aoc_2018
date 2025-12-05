"""Module for day 2 of Advent of Code (by Pim van Leeuwen)"""
def solve(input_data):
    """Solve both parts of the Advent of Code Day"""
    part1 = solve_part1(input_data)
    part2 = solve_part2(input_data)
    return part1, part2

def solve_part1(input_data):
    """Solve part 1 of the Advent of Code Day"""
    exactly_two = 0
    exactly_three = 0

    for i in input_data.split("\n"):
        two, three = False, False

        # Check the requirements for the IDs
        # Added requirements for the counting only once per id
        for c in set(i):
            if i.count(c) == 2 and not two:
                two = True
                exactly_two += 1
            if i.count(c) == 3 and not three:
                three = True
                exactly_three += 1

    # return checksum
    return exactly_two * exactly_three

def similar_inputs(a, b):
    """Function to check if two ids are similar,
    returns the id of the one dissimilarity if that is present"""
    one_off = -1
    for i, c in enumerate(a):
        if c != b[i] and one_off == -1:
            one_off = i
        elif c != b[i]:
            return -1
    return one_off

def solve_part2(input_data):
    """Solve part 2 of the Advent of Code Day"""
    for id1 in input_data.split("\n"):
        for id2 in input_data.split("\n"):
            if id1 == id2:
                continue

            #  remove similar without additional char
            if similar_inputs(id1, id2) != -1:
                i = similar_inputs(id1, id2)
                return f"{id1[:i] + id1[i+1:]}"

    return None
