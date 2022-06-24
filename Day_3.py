with open('inputs/day_3.txt', 'r') as input:
    input_lines = [line.strip() for line in input.readlines()]


column_conversion = []
for row_num in range(len(input_lines[0])):
        column_conversion.append('')
        for col_num in range(len(input_lines)):
            column_conversion[-1] += input_lines[col_num][row_num]

gamma = ''
for column in column_conversion:
    if column.count('0') > len(column) / 2:
        gamma += '0'
    else:
        gamma += '1'

epsilon = ''.join(map(lambda bit: '1' if bit == '0' else '0', gamma))

print("Submarine power consumption:", int(gamma, 2) * int(epsilon, 2))

