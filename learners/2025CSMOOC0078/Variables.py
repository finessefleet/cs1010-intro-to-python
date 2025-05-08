#Here we will know the variables in python, How to write a variable or identifiers.
#Using some prebuilt functions like print(),input(),type() etc.
#Use of f-strings
#Will know some operators in python.
#Intro to new functions like ceil , floor
#using comparison operator >
a = 10
b = 20
c = "MOOC foundation"
a > c
a > b

#assigning same value to multiple variables.
x = y = z = q = 9
print(x)
print(y)
print(z)
print(q)

#Using input() function -> tells about the type of class e.g. <int>, <float> etc.
a = 10
b = 'Yam hai hum'
c = 70.6
d = True
''' type(a)
type(b)
type(c)
type(d) ''' #It will take the current last statement as output e.g. <bool> as it took d statement

print(type(a))
print(type(b))
print(type(d))
print(type(c)) #It will show all the classes

#Using input() function along with datatypes, 
#we need a datatype to be written before the input() to bypass the default assignment i.e. input() takes string by default.
name = input("Enter your name: ")
mark1 = int(input("Enter the marks of sub1: "))
mark2 = int(input("Enter the marks of sub2: "))
mark3 = int(input("Enter the marks of sub3: "))

total_marks = mark1 + mark2 + mark3
print(f"The Total marks of {name} are : ", total_marks)

#Using id() function -> tells about the unique identity for variable's lifespan, it is constant for the lifespan of a variable.
#It also tells about where the variable is stored.
x = 89
y = 'String'
print(id(y)) #for string
print(id(a)) #for int

#declaring multiple variables in a single line
a, b, p, q = 2,4,'Empire', 6  #here the sequence of assignment is followed
print(p)
print(a)
print(b)
print(q)
import math
x = math.sqrt(int(input("Enter a number:")))
print(x)

#Using floor(), ceil() functions
#floor() -> the lowest value e.g. if 4.5 then floor() will give 4.
#ceil() -> the highest next e.g. if 8.7 then ceil() will give 9.
x = float(input("Enter a float value: "))
print(math.floor(x))
print("\t")

y = float(input("Enter another float value: "))
print(math.ceil(y))

#Using the del keyword
#It delets a variable
del x
print(x)
