"""Module for day 10 of Advent of Code (by Pim van Leeuwen)"""
import sys
from xmlrpc.client import MAXINT

from utils import *
from dataclasses import dataclass

@dataclass
class Star:
    x: int = 0
    y: int = 0
    vx: int = 0
    vy: int = 0

def print_stars(stars):
    min_x = min(star.x for star in stars)
    max_x = max(star.x for star in stars)
    min_y = min(star.y for star in stars)
    max_y = max(star.y for star in stars)

    grid = [['.' for _ in range(min_x, max_x + 1)] for _ in range(min_y, max_y + 1)]

    for star in stars:
        grid[star.y - min_y][star.x - min_x] = '#'

    for row in grid:
        print(''.join(row))

def bounding_box(stars):
    min_x = min(star.x for star in stars)
    max_x = max(star.x for star in stars)
    min_y = min(star.y for star in stars)
    max_y = max(star.y for star in stars)

    return (max_x - min_x) * (max_y - min_y)

def do_step(stars):
    for star in stars:
        star.x += star.vx
        star.y += star.vy

def solve(input_data):
    """Solve both parts of the Advent of Code Day"""
    lines = read_lines(input_data)
    parts = ["Read message visually", 0]
    stars = []

    for line in lines:
        stars.append(Star(*extract_ints(line)))

    min_i = 0
    min_bounding = sys.maxsize
    for i in range(20000):
        do_step(stars)
        if (bb := bounding_box(stars)) < min_bounding:
            min_bounding = bb
            min_i = i + 1
            print(i + 1, bb)
            if min_bounding < 1000:
                print_stars(stars)

    parts[1] = min_i

    return parts

