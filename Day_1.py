with open('inputs/Day_1.txt', 'r') as readings:
    depths = [int(number.strip()) for number in readings.readlines()]

increased = sum([1 for i in range(1, len(depths)) if depths[i] > depths[i-1]])
print("Depth increases:", increased)

increased = sum([1 for i in range(3, len(depths)) if depths[i] > depths[i-3]])
print("Sliding increases:", increased)
