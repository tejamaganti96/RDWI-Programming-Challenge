with open('inputs/day_7.txt', 'r') as aoc_input:
    crabs = [int(x) for x in aoc_input.read().strip().split(',')]

least_fuel = None
for position in range(max(crabs)):
    fuel_cost = sum([abs(x - position) for x in crabs])
    if not least_fuel or fuel_cost < least_fuel:
        least_fuel = fuel_cost

print("Fuel cost to align to least expensive position:", least_fuel)

least_fuel = None
for position in range(max(crabs)):

    fuel_cost = 0
    for crab in crabs:
        movement = abs(crab - position)
        fuel_cost += movement * (movement + 1) // 2

    if not least_fuel or fuel_cost < least_fuel:
        least_fuel = fuel_cost

print("Actual fuel cost to align to least expensive position:", least_fuel)