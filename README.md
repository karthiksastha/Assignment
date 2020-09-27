# Python Assignment-1

Q1)Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). the numbers obtained should be printed in a comma-separated sequence on a single line.

Q2)Write a python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.

Q3)write a python program to find the volume of a sphere with diameter 12 cm.Formula: V=4/3 * π * r3

# Python Assignment-2

Q1)Create the below pattern using nested for loop in Python

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

Q2)Write a Python program to reverse a word after accepting the input from the user?

# Python Assignment-3

Q1.1)Write a Python Program to implement your own myreduce() function which works exactly like Python's built-in function reduce()

Q1.2)Write a Python program to implement your own myfilter() function which works exactly like Python's built-in function filter()

Q2)Implement List comprehensions to produce the following lists. Write List comprehensions to produce the following Lists ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’] ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz'] ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz'] [[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]] [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]


# Python Assignment-4

Q1.1)Problem_1.1-: Write a Python Program(with class concepts) to find the area of the triangle using the below formula.
area = (s(s-a)(s-b)*(s-c)) ** 0.5
Function to take the length of the sides of triangle from user should be defined in the parent class and function to calculate the area should be defined in subclass.

Q1.2)Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.

Q2.1)Write a Python program using function concept that maps list of words into a list of integers representing the lengths of the corresponding words . Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4] Here 2,3 and 4 are the lengths of the words in the list.

2.2)Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.

# Python Assignment-5

Q1) Write a function to compute 5/0 and use try/except to catch the exceptions.

Q2)Implement a Python program to generate all sentences where subject is in ["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in ["Baseball","cricket"].

        Hint: Subject,Verb and Object should be declared in the program as shown below.                
        subjects=["Americans ","Indians"]
        verbs=["play","watch"]
        objects=["Baseball","Cricket"]

Exptected Output  :                       
                   Americans play Baseball.
                   Americans play Cricket.
                   Americans watch Baseball.
                   Americans watch Cricket.
                   Indians play Baseball.
                   Indians play Cricket.
                   Indians watch Baseball.
                   Indians watch Cricket.
                   
                  
 # Python Assignment-6
 
Q1)It happens all the time: someone gives you data containing malformed strings, Python, lists and missing data. How do you tidy it up so you can get on with the analysis? Take this monstrosity as the DataFrame to use in the following puzzles:

df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm', 'Budapest_PaRis', 'Brussels_londOn'], 'FlightNumber': [10045, np.nan, 10065, np.nan, 10085], 'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]], 'Airline': ['KLM(!)', ' (12)', '(British Airways. )','12. Air France', '"Swiss Air"']})

Some values in the the FlightNumber column are missing. These numbers are meant to increase by 10 with each row so 10055 and 10075 need to be put in place. Fill in these missing numbers and make the column an integer column (instead of a float column).

The From_To column would be better as two separate columns! Split each string on the underscore delimiter _ to give a new temporary DataFrame with the correct values. Assign the correct column names to this temporary DataFrame.

Notice how the capitalisation of the city names is all mixed up in this temporary DataFrame. Standardise the strings so that only the first letter is uppercase (e.g. "londON" should become "London".)

Delete the From_To column from df and attach the temporary DataFrame from the previous questions.

In the RecentDelays column, the values have been entered into the DataFrame as a list. We would like each first value in its own column, each second value in its own column, and so on. If there isn't an Nth value, the value should be NaN. Expand the Series of lists into a DataFrame named delays, rename the columns delay_1, delay_2, etc. and replace the unwanted RecentDelays column in df with delays.


