#Q1.1)Write a Python Program to implement your own myreduce() function which works exactly like Python's built-in function reduce()

# Reduce will produce a single result
def myreduce(anyfunc, sequence):

 # Get first item in sequence and assign to result
  result = sequence[0]
 # iterate over remaining items in sequence and apply reduction function 
  for item in sequence[1:]:
   result = anyfunc(result, item)

  return result

#Q1.2)Write a Python program to implement your own myfilter() function which works exactly like Python's built-in function filter()

# Custom filter function 
def myfilter(anyfunc, sequence):

 # Initialize empty list
 result = []
 # iterate over sequence of items in sequence and apply filter function
 for item in sequence:
  if anyfunc(item):
   result.append(item)

 # return funal output
 return result


# test myreduce function
def sum(x,y): return x + y

# test myfilter function
def ispositive(x):
 if (x <= 0): 
  return False 
 else: 
  return True


print ("Sum on list [1,2,3] using custom reduce function "   + str(myreduce(sum, [1,2,3])) )
print ("Filter only positive Integers on list [0,1,-2,3,4,5] using custom filter function"  + str(myfilter(ispositive, [0,1,-2,3,4,5])))


#Q2)Implement List comprehensions to produce the following lists. Write List comprehensions to produce the following Lists ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’] ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz'] ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz'] [[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]] [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

#Section 1
word="AcadGild"
#list Comprehension
output_list=[w.upper() for w in list(word)]
print("Output:")
print(output_list)

#Section 2
word_1=list('xyz')
word_2=[x*n for x in word_1 for n in range(1,5) ]
print(word_2)

#Section 3
word_3=[x*n for n in range(1,5) for x in word_1 ]
print(word_3)

#Section 4
number=[2,3,4]
number_1=[[x+n] for x in number for n in range(0,3)]
print(number_1)

#Section 5
number_2=[2,3,4,5]
number_3=[[x+n for n in range(0,4)] for x in number_2 ]
print(number_3)

#Section 6
number_4=[1,2,3]
number_5= [(b,a) for a in number_4 for b in number_4]
print(number_5)

