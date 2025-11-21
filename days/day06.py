"""Module for day 6 of Advent of Code (by Pim van Leeuwen)"""
from utils import read_lines


def solve_part1(input_data):
    """Solve part 1 of the Advent of Code Day"""

    # coordinates that are dangerous
    coordinates = [tuple(map(int, line.split(','))) for line in read_lines(input_data)]

    # Domain of the field, everything outside extends to infinity
    min_x = min(x for x, y in coordinates)
    max_x = max(x for x, y in coordinates)
    min_y = min(y for x, y in coordinates)
    max_y = max(y for x, y in coordinates)

    area = {coord: 0 for coord in coordinates}
    infinite = set()

    part_2 = 0

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            # get distance to all coordinates
            distances = [(abs(x - coord[0]) + abs(y - coord[1]), coord) for coord in coordinates]
            distances.sort()

            total_distance = sum(d for d, coord in distances)

            if total_distance < 10000:
                part_2 += 1

            # If it is the closest to multiple coordinates, skip it
            if len(distances) > 1 and distances[0][0] == distances[1][0]:
                continue

            # Add the area to the closest coordinate
            area[distances[0][1]] += 1
            if x == min_x or x == max_x or y == min_y or y == max_y:
                infinite.add(distances[0][1])

    finite_areas = [size for coord, size in area.items() if coord not in infinite]


    return max(finite_areas), part_2

def solve_part2(input_data):
    """Solve part 2 of the Advent of Code Day"""

    return "Included in part 1"