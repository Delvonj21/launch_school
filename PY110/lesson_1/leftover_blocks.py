# You have a number of building blocks that can be used to build a valid structure. There are certain rules about what determines a valid structure:

## P: Understand the Problem
# Input:
# Integer representing the Number of available blocks
# Output:
# Integer representing the number of blocks left over after building the tallest possible valid structure

# Explicit:
# Structures are built with blocks
# Blocks are cubes
# Cubes are six-sided, have square faces, and have equal lengths on all sides
# The top layer in the structure has a single block
# The Upper layer blocks must be supported by four lower layer blocks
# The Lower layer blocks can support more than one upper layer blocks
# Layers are solid structures, There are no gaps between blocks

# Implicit:
# Layer number correlates with blocks in a layer
# The number of blocks in a layer is layer number * layer number

# Questions:
# Is a lower layer valid if it has more blocks than it needs?
# Will there always be left-over blocks?

## E: Examples and Test Cases
# print(calculate_leftover_blocks(0) == 0)   True
# print(calculate_leftover_blocks(1) == 0)   True
# print(calculate_leftover_blocks(2) == 1)   True
# print(calculate_leftover_blocks(4) == 3)   True
# print(calculate_leftover_blocks(5) == 0)   True
# print(calculate_leftover_blocks(6) == 1)   True
# print(calculate_leftover_blocks(14) == 0)  True

# No, a lower level isn't valid if it has more blocks than it needs
# No, there won't always be leftover blocks


## D: Data Structures
#  nested list to represent the structure, each sublist could represent a layer.

# [
#     ['x'],
#     ['x','x', 'x', 'x'],
#     ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x',],
#     ....
# ]

## A: Algorithms
# 1. Start with:
#      - The "number of blocks remaining" is equal to the input.
#      - The "current layer number" is layer 0.

# 2. Calculate the "current layer number" for the next layer by
#    adding 1 to the "current layer number".

# 3.  Using the new "current layer number", calculate the "number of
#    blocks required in this layer" by multiplying the "current
#    layer number" by itself.

# 4. Determine whether the "number of blocks remaining" is greater
#    than or equal to the "number of blocks required in this layer".
#      - If there are enough blocks:
#          - Subtract the "number of blocks required in this layer"
#            from the "number of blocks remaining".
#          - Go to step 3.
#      - If there aren't enough blocks:
#          - Return the "number of blocks remaining".

# C: Implementing a Solution in Code


def calculate_leftover_blocks(n):
    current_layer = 0
    remaining_blocks = n

    required_blocks = (current_layer + 1) ** 2

    while remaining_blocks >= required_blocks:
        remaining_blocks -= required_blocks
        current_layer += 1
        required_blocks = (current_layer + 1) ** 2

    return remaining_blocks


print(calculate_leftover_blocks(0) == 0)
print(calculate_leftover_blocks(1) == 0)
print(calculate_leftover_blocks(2) == 1)
print(calculate_leftover_blocks(4) == 3)
print(calculate_leftover_blocks(5) == 0)
print(calculate_leftover_blocks(6) == 1)
print(calculate_leftover_blocks(14) == 0)
