import numpy as np

# Sheet object to gather all data from the input
class Sheet:
    def __init__(self, id, x, y, w, h):
        self.id = id
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    # Returns true if (x,y) is within the range of this sheet
    def is_inside(self, x, y):
        if self.x <= x < self.x + self.w and self.y <= y < self.y + self.h:
            return True
        else:
            return False

    # Returns true if s2 overlaps with s1
    def overlaps_with(self, s2):
        return not (self.x + self.w <= s2.x or s2.x + s2.w <= self.x or
            self.y + self.h <= s2.y or s2.y + s2.h <= self.y)

def process_data(input_data):
    sheets = []

    # process every line
    for line in input_data.split("\n"):
        element = line.split(" ")
        sheets.append(Sheet(int(element[0][1:]), int(element[2].split(',')[0]), int(element[2].split(',')[1][:-1]),
                            int(element[3].split('x')[0]), int(element[3].split('x')[1])))

    return sheets

def solve_part1(input_data):
    # grid of 1000x1000 inches
    grid = np.zeros((1100, 1100), dtype=int)
    sheets = process_data(input_data)

    # add the claim to the grid
    for s in sheets:
        for x in range(s.x, s.x + s.w):
            for y in range(s.y, s.y + s.h):
                grid[y][x] += 1

    # return all places with more than 1 claim
    return np.sum(grid > 1)

def solve_part2(input_data):
    sheets = process_data(input_data)

    # Check if there is a single sheet that does not overlap with any
    for s1 in sheets:
        if all(not s1.overlaps_with(s2) or s1.id == s2.id for s2 in sheets):
            return s1.id

    return None
