#Q1) Create the below pattern using nested for loop in Python

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*


n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')
    
#Q2) Write a Python program to reverse a word after accepting the input from the user?

word = input("Input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")


