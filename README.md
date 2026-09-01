# CS-2-Sampaguita-Eguilos
This program calculates the distance between two points (x1, y1) and (x2, y2) on a 2D plane  using input values and a math library.

import math

# Ask the user to enter the coordinates of the first point
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
# Ask the user to enter the coordinates of the second point
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Compute the distance using the distance formula
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# Compute the distance using the distance formula
print(f"\nThe distance between the two points is: {distance:.2f}")
