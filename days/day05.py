"""Module for day 5 of Advent of Code (by Pim van Leeuwen)"""
from xmlrpc.client import MAXINT

class Node:
    """We will solve this using a doubly linked list"""
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def has_next(self):
        """Check if this node has a successor"""
        return self.next is not None

    def length(self):
        """Return the length of the node and all the nodes following it"""
        if self.has_next():
            return self.next.length() + 1
        return 1

def solve_part1(input_data):
    """Solve part 1 of the Advent of Code Day"""
    root = Node(input_data[0])
    current = root

    # create the doubly linked list from the input
    for c in input_data[1:]:
        new_node = Node(c)

        # set pointers
        current.next = new_node
        new_node.prev = current

        current = new_node

    # reset current node
    current = root

    # whilst the next is still present (so not at the end)
    while current.next is not None:
        if current.data.lower() == current.next.data.lower() and current.data != current.next.data:
            # reaction takes place
            # A-current-current.next-D becomes AD
            if current.prev is not None:
                current.prev.next = current.next.next
            if current.next.next is not None:
                current.next.next.prev = current.prev

            # move one back to check if there are more reactions (if possible)
            if current.prev is not None:
                current = current.prev
            else:
                # we have to adjust the root since this is actually not the start anymore, and we do
                # want to keep track of the start for counting later
                root = current.next.next
                current = current.next.next
        else:
            current = current.next

    return root.length()

def solve_part2(input_data):
    """Solve part 2 of the Advent of Code Day
    just going over every char and doing part 1 without that char (and its upper case variant) """
    part_2 = MAXINT
    for c in range(ord('a'), ord('z') + 1):
        new_input = input_data.replace(chr(c).lower(), "").replace(chr(c).upper(), "")
        part_2 = min(part_2, solve_part1(new_input))

    return part_2
