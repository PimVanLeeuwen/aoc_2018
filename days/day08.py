"""Module for day 8 of Advent of Code (by Pim van Leeuwen)"""
from utils import read_lines, extract_letters
from dataclasses import dataclass, field

@dataclass
class Node:
    header: list = field(default_factory=list)
    metadata: list = field(default_factory=list)
    children: list = field(default_factory=list)
    parent: 'Node' = None

def compute_node_value(node):
    """Compute recursively the value of a node based on its metadata and children"""
    if not node.children:
        return sum(node.metadata)
    else:
        return sum(compute_node_value(node.children[i-1]) if 1 <= i <= len(node.children) else 0 for i in node.metadata)


def solve(input_data):
    """Solve both parts of the Advent of Code Day"""
    parts = [0,0]

    nums = list(map(int, read_lines(input_data)[0].split(" ")))
    index = 0
    header_node = Node()
    current_node = header_node

    while index < len(nums):
        if not current_node.header:
            current_node.header = nums[index:index+2]
            index += 2

        elif len(current_node.children) < current_node.header[0]:
            new_node = Node(parent=current_node, header=nums[index:index+2])
            index += 2
            current_node.children.append(new_node)
            current_node = new_node

        elif len(current_node.metadata) < current_node.header[1]:
            current_node.metadata.append(nums[index])
            parts[0] += nums[index]
            index += 1

        else:
            current_node = current_node.parent


    parts[1] = compute_node_value(header_node)

    return parts

