"""Module for day 7 of Advent of Code (by Pim van Leeuwen)"""
from utils import read_lines, extract_letters

def solve(input_data):
    """Solve both parts of the Advent of Code Day"""
    part1 = solve_part1(input_data)
    part2 = solve_part2(input_data)
    return part1, part2

def solve_part1(input_data):
    """Solve part 1 of the Advent of Code Day"""

    constraints = [extract_letters(l) for l in read_lines(input_data)]

    letters = list(set([a for a, b in constraints] + [b for a, b in constraints]))
    completed = []

    while len(letters) > 0:
        available = sorted([l for l in letters if all(pre in completed for pre, post in constraints if post == l)])
        next_letter = available[0]
        completed.append(next_letter)
        letters.remove(next_letter)

    return ''.join(completed)

def step_duration(l):
    return 60 + ord(l) - ord('A') + 1

def solve_part2(input_data):
    """Solve part 2 of the Advent of Code Day"""
    constraints = [extract_letters(l) for l in read_lines(input_data)]
    letters = list(set([a for a, b in constraints] + [b for a, b in constraints]))
    prerequisites = {l: set() for l in letters}
    for pre, post in constraints:
        prerequisites[post].add(pre)


    workers = [None] * 5
    completed = []
    in_progress = []
    time = 0

    # iterate like time, every iteration is one second
    while len(completed) < len(letters):
        # All available steps
        # all preconditions met, not completed yet, not in progress
        available = sorted([l for l in letters if
                            all(pre in completed for pre, post in constraints if post == l)
                            and l not in completed
                            and l not in in_progress])

        # check we can assign some workers
        for i in range(5):
            if workers[i] is None and available:
                next_step = available[0]
                available.remove(next_step)
                in_progress.append(next_step)
                workers[i] = [next_step, step_duration(next_step)]

        # Advance time by 1 second, if workers are done mark steps as completed and free up worker
        for i in range(5):
            if workers[i]:
                workers[i][1] -= 1
                if workers[i][1] == 0:
                    completed.append(workers[i][0])
                    in_progress.remove(workers[i][0])
                    workers[i] = None
        time += 1

    return time