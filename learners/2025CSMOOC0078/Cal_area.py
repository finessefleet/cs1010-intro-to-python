# Calculating Area of different shape
# Using Basic data type, print statement, input(), importing math module
# Calculating Area of Rectangle

length = int(input("Enter the length: "))
width = int(input("Enter the width: "))

Area_rec = length * width
print("The area is : ", Area_rec)


#Calculating Area of Circle
pi = 3.1459
radius = float(input("Enter the radius: "))

Area_circle = pi*radius**2
print("The area of Circle is : ", Area_circle)

#Calculating Area of sphere
# Area = 4*pi*r**2

import math
pi = math.pi
r = float(input("Enter the radius of Sphere: "))

sphere_area = 4*pi*r**2
print("The area of sphere is : %.3f" % sphere_area)
