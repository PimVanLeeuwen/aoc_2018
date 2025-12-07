"""Module for day 9 of Advent of Code (by Pim van Leeuwen)"""
from utils import read_lines, extract_letters
from dataclasses import dataclass, field

@dataclass
class Marble:
    score: int = 0
    next: 'Marble' = None
    prev: 'Marble' = None

def play_game(players, marbles):
    p = 0
    current_marble = Marble(0)
    current_marble.next = current_marble
    current_marble.prev = current_marble
    scores = [0] * players

    for m in range(1, marbles + 1):
        if m % 23 == 0:
            # add score of marble to be added
            scores[p] += m

            # Go back 7 marbles
            for _ in range(7):
                current_marble = current_marble.prev

            # Add score of marble to be removed
            scores[p] += current_marble.score

            # Remove marble
            current_marble.prev.next = current_marble.next
            current_marble.next.prev = current_marble.prev
            current_marble = current_marble.next

        else:
            new_marble = Marble(m)
            one_clockwise = current_marble.next
            two_clockwise = one_clockwise.next

            one_clockwise.next = new_marble
            new_marble.prev = one_clockwise
            new_marble.next = two_clockwise
            two_clockwise.prev = new_marble

            current_marble = new_marble

        p = (p + 1) % players

    return max(scores)

def solve(input_data):
    """Solve both parts of the Advent of Code Day"""
    parts = [play_game(411, 71170), play_game(411, 7117000)]

    return parts

