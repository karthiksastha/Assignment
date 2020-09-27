#Q1)Write a function to compute 5/0 and use try/except to catch the exceptions.

def DivideByZero(x,y):
    ''' This Function is intended to return an Exception,if an integer has been tried to get divisible by Zero '''
    try:
        x/y
    except ZeroDivisionError as e:
        print("An interger/number can't be divisible by Zero")
        print("An execption has been occured as, ",e, " action has been attempted")

# apply values on variable x & y
x,y=5,0

#Function Execute
DivideByZero(x,y)

#Q2)Implement a Python program to generate all sentences where subject is in ["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in ["Baseball","cricket"].

subject=["Americans","Indians"]
verb=["play","watch"]
objects=["Baseball","Cricket"]

# List Comprehension
Syntax = [(Sub+' '+vrb+' '+Objct+".") for Sub in subject for vrb in verb for Objct in objects]

#for Loop for Iteration
print("Output:")

for syn in Syntax:  
    print(syn)