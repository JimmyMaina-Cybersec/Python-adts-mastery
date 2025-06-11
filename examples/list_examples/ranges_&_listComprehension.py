# Counting to twenty
for number in range(1, 21):
    print(number)

# Using range(), make a list of odd numbers from 1 to 20
for number in range(1, 21, 2):
    print(f"\n{number}")

# Make a list of multiples of 3 from 3 to 30
for multiple_of_3 in range(3, 31, 3):
    print(multiple_of_3)

# Make a list of number from one to one million
oneMillion_numbers = [number for number in range(1, 1000001)]

# Find the min, max and sum of the one million numbers
print(f"\nMinimum: {min(oneMillion_numbers)}")
print(f"Maximum: {max(oneMillion_numbers)}")
print(f"Sum: {sum(oneMillion_numbers)}\n")

# Loop throught he one million numbers while printing each one of them
for number in oneMillion_numbers:
    print(number)

# First 10 cubes
cubes = []
for cube in range(1, 11):
    cubes.append(cube**3)

print(cubes)

# Cube comprehension
cubes = [value**3 for value in range(1, 11)]
print(cubes)
