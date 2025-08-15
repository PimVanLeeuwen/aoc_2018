from xmlrpc.client import MAXINT

# Solve this using a doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def solve_part1(input_data):
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
            if current.prev is not None: current.prev.next = current.next.next
            if current.next.next is not None: current.next.next.prev = current.prev

            # move one back to check if there are more reactions (if possible)
            if current.prev is not None:
                current = current.prev
            else:
                # we have to adjust the root since this is actually not the start any more and we do
                # want to keep track of the start for counting later
                root = current.next.next
                current = current.next.next
        else:
            current = current.next

    # reset node to count
    part_1 = 1
    current = root

    while current.next is not None:
        part_1 += 1
        current = current.next

    return part_1

def solve_part2(input_data):

    # part 2 easy just going over every char and doing part 1 without that char (and its upper case variant)
    part_2 = MAXINT
    for c in range(ord('a'), ord('z') + 1):
        new_input = input_data.replace(chr(c).lower(), "").replace(chr(c).upper(), "")
        part_2 = min(part_2, solve_part1(new_input))

    return part_2
