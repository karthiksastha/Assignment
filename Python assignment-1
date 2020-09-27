#Q1)Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.

#Using for loop

for i in range(2000,3201):
    if i%7 == 0 and i%5!=0:
        print(i,end=',')
print("\b")

#Using generators and list comprehension

print(*(i for i in range(2000, 3201) if i%7 == 0 and i%5 != 0), sep=",")


#Q2)Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name github
fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)

#Q3)Write a Python program to find the volume of a sphere with diameter 12 cm.
#Formula: V=4/3 * π * r3

import math

pi = math.pi

#Converting Diameter into radius
r = float(12/2)
V = (float(4/3)*(pi)*(r)**3)

print(V)

