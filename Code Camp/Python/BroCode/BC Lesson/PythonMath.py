# FILE CONTAINS INPUT AND MATHEMATICAL FUNCTIONS.

# INPUT must be float or int because volume is a number, not a string
length = float(input('Length of the course: ')) # 13
width = float(input('Width of the course: ')) # 15
height = float(input('Height of the course: ')) # 4.99

volume = length * width * height # Formula for volume

# Indentations for results
print('\nRESULTS:')
# Since the result has many decimal places, we will ROUND it OFF by 2
print(f'The volume of the course is {round(volume, 2)}cm^3')

# Built-in Math Functions:
print(abs(-15)) # ABSOLUTE
print(pow(volume,2)) # POWER
print(max(length, width, height)) # MAX (Highest number)
print(min(length, width, height)) # MIN (Lowest number)


print('\nAugmented Operators:')
Pizza = 0
Pizza += 5 # Pizza = (Pizza + 5) can be: ADDITION
Pizza -= 2 # Pizza = (Pizza - 2) can be: SUBTRACTION
Pizza **= 2 # Pizza = (Pizza ^4) can be: EXPONENTS
Pizza %= 6 # Pizza = (Pizza % 6) can be: REMAINDER
# The same method works for multiplication and division

print(f'The pizza is: {Pizza}cm')

print('\nMath Modules:')
import math
print(math.pi) # Pie
print(math.e) # E value
print(math.sqrt(9)) # Square root
print(math.ceil(9.1)) # Round UP
print(math.floor(9.5)) # Round DOWN

# SAMPLE for Math Modules:
# Circumference of a circle
radius = float(input('Enter the radius of a circle: '))
circumference = 2 * math.pi * radius
print(f'The circumference of the circle is: {round(circumference, 2)}cm')

# Area of a circle
radiuss = float(input('Enter the radius of circle: '))
area = math.pi * pow(radiuss, 2)
print(f'The area of the circle is: {round(area, 2)}cm^2')

# Hypotenuse of a triangle
a = float(input('Enter side A: '))
b = float(input('Enter side B: '))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f'The Hypotenuse (C) of the triangle is: {round(c, 2)}cm^2')