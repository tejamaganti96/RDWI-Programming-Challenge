with open('inputs/day_2.txt', 'r') as input:
    input_lines = [line.strip().split(' ') for line in input.readlines()]
    input_lines = [(x, int(y)) for [x, y] in input_lines]

horizontal_position = 0
depth = 0

for direction, distance in input_lines:
    if direction == 'forward':
        horizontal_position +=distance
    elif direction == 'up':
        depth -= distance
    elif direction == 'down':
        depth += distance
print("Product of horizontal position and depth: ", (horizontal_position * depth) )

horizontal_position = 0
depth = 0
aim = 0

for direction, distance in input_lines:
    if direction == 'forward':
        horizontal_position +=distance
        depth += aim * distance
    elif direction == 'up':
        aim -= distance
    elif direction == 'down':
        aim += distance

print("Adjusted product of horizontal position and depth: ", (horizontal_position * depth))

