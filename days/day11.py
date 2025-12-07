"""Module for day 11 of Advent of Code (by Pim van Leeuwen)"""
import sys
from itertools import product
from xmlrpc.client import MAXINT

from utils import *
from dataclasses import dataclass

def power_level(x,y, serial):
    rack_id = x + 10
    power = rack_id * y
    power += serial
    power *= rack_id
    power = (power // 100) % 10
    power -= 5
    return power

# Python
def find_max(power_map, size):
    max_sum = -sys.maxsize
    max_coord = (0, 0)
    for x,y in product(range(1, 301-(size-1)), range(1, 301-(size-1))):
        total = sum(
            power_map[(x + dx, y + dy)]
            for dx,dy in product(range(size), range(size))
        )
        if total > max_sum:
            max_sum = total
            max_coord = (x, y)  # 1-based indexing
    return max_coord, max_sum

def solve(input_data):
    """Solve both parts of the Advent of Code Day"""
    parts = [0, 0]
    serial = 2866
    power_level_map = {(0,0): 1}

    # power level tests
    assert(power_level(122, 79, 57) == -5)
    assert(power_level(217, 196, 39) == 0)
    assert(power_level(101, 153, 71) == 4)

    for x,y in product(range(1, 301), range(1, 301)):
        power_level_map[(x,y)] = power_level(x, y, serial)

    parts[0] = find_max(power_level_map, 3)[0]

    max_coord, max_power = (0,0,0),0
    for s in range(12):
        (c, p) = find_max(power_level_map, s)
        if p > max_power:
            max_power = p
            max_coord = (c[0], c[1], s)

    parts[1] = max_coord

    return parts

