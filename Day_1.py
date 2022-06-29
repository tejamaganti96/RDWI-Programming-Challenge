#Part 1 boils down to counting the number of times the input is higher then its predeccesor
#Part 2 is esentially the same as part one, but requires "3 depth windows"
#For part 2, all 3 values don't need to be summed,
    #To test if a window is larger than the previous one is to compare 
    #the first value of the previous with the last value of the new one.


with open('inputs/Day_1.txt', 'r') as readings:
    depths = [int(number.strip()) for number in readings.readlines()]
increased = sum([1 for i in range(1, len(depths)) if depths[i] > depths[i-1]])

#Answer to part 1
print("Depth increases:", increased)

increased = sum([1 for i in range(3, len(depths)) if depths[i] > depths[i-3]])
#Answer to part 2
print("Sliding increases:", increased)
