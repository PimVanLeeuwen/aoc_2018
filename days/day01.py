"""Module for day 1 of Advent of Code (by Pim van Leeuwen)"""
def solve(input_data):
    """Solve both parts of the Advent of Code Day"""
    part1 = solve_part1(input_data)
    part2 = solve_part2(input_data)
    return part1, part2

def solve_part1(input_data):
    """Solve part 1 of the Advent of Code Day"""
    frequency = 0

    # add or subtract all numbers in the list
    for l in input_data.split("\n"):
        if l[0] == '-':
            frequency -= int(l[1:])
        else:
            frequency += int(l[1:])
    return frequency

def solve_part2(input_data):
    """Solve part 2 of the Advent of Code Day"""
    frequencies = [0]

    # Keep adding the frequencies until we find a duplicate
    while True:
        for l in input_data.split("\n"):
            if l[0] == '-':
                frequencies.append(frequencies[-1] - int(l[1:]))
            else:
                frequencies.append(frequencies[-1] + int(l[1:]))
            if frequencies[-1] in frequencies[:len(frequencies)-1]:
                return frequencies[-1]
