"""import math

def degree_to_radian(degree):
    return round(degree * (math.pi / 180), 6)

degree = float(input("Degree: "))
print("Radian:", degree_to_radian(degree))



def trapezoid_area(height, base1, base2):
    return (1/2) * (base1 + base2) * height
height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))
print(" Output:", trapezoid_area(height, base1, base2))


import math

def polygon_area(sides, length):
    area = (sides * length ** 2) / (4 * math.tan(math.pi / sides))
    return area

sides = int(input("Number of sides: "))
length = int(input("The length of a side: "))
area = polygon_area(sides, length)
print(f"The area of the polygon is: {area}")"""



def parallelogram_area(base, height):
    return base * height

base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
area = parallelogram_area(base, height)
print(area)  
