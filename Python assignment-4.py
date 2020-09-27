#Q1.1)Problem_1.1-: Write a Python Program(with class concepts) to find the area of the triangle using the below formula.
#area = (s(s-a)(s-b)*(s-c)) ** 0.5
#Function to take the length of the sides of triangle from user should be defined in the parent class and function to calculate the area should be defined in subclass.

#Parent class
class Triangle:
    def __init__(self):
        ''' This method has been used as an self constructor for Traingle class'''
        number_of_sides=['a','b','c']
        self.TriangleSides=number_of_sides
        
    def sides_Of_Triangle(self):
        ''' This method will return sides of Traingle'''
        self.sides_Of_Traingle=[input("Enter the Side "+i+" :") for i in self.TriangleSides]
        
#Sub class       
class Traingle_Area(Triangle):
    def __init__(self):
        '''This method will inherit properties and attrivutes fro Parent class "Traingle" and it's class "TraingleArea"  '''
        Triangle.__init__(self)
        
    def area_Of_Triangle(self):
        '''This method will return an Area of Triangle'''
        
        # Iterator has been created to iterate sides of triangle from collection
        triangleSides=iter(self.sides_Of_Traingle)
        a=float(next(triangleSides))
        b=float(next(triangleSides))
        c=float(next(triangleSides))      
           
        # Half-perimeter (s) of Triangle         
        s= (a+b+c)*0.5        
        # Area of Triangle         
        Area = (s*(s-a)*(s-b)*(s-c))**0.5    
        print("The sides of triangle are a="+str(a)+", b="+str(b)+", c="+str(c))     
        Area = ('The Area of the triangle is %0.2f' %Area )
        #return Area
        print(Area)
        
# Create object of Sub class Traingle_Area()
Area_Of_Traingle = Traingle_Area()

#Ask User to Enter the sides of Triangle
Area_Of_Traingle.sides_Of_Triangle()

# Calculate the Area Of Triangle
Area_Of_Traingle.area_Of_Triangle()

#Q1.2)Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.

#Function to Filter words based on length
def filter_long_words(WordList,n):
    ''' This function returns list of words are longer than Argument n . 
    Note : n has been considerd has an integer'''
    
    #List Comprehensions
    Wordlist=[x.strip() for x in WordList if len(x.strip())>n]
    
    if(len(Wordlist)>0):
        print("\n Output:")
        print("\n The List of longest words , which  are longer than "+str(n)+" is :")
        return Wordlist
    else:
        return "No Words longer than specified number "+str(n)
    
#Ask user's Input
print("Input:")
string= input("Please enter your words: ")
number= int(input("Please enter your number: "))

# Split the words by "," comma and convert into list
list_Of_Words = list(string.split(","))
#Function Execution
filter_long_words(list_Of_Words,number)


#Q2.1)Write a Python program using function concept that maps list of words into a list of integers representing the lengths of the corresponding words . Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4] Here 2,3 and 4 are the lengths of the words in the list.

#Function to map length of words with words 
def map_Words_to_Length(List):
    ''' This function Map's the words with their corresponding length'''
    return list(map(len, List))

word_List=list(input("Input : Please enter Words : ").split(","))
#List Comprehension has been done to remove white trailing white spaces
List=[x.strip() for x in word_List]
#function Execution
Words_lengths=map_Words_to_Length(List)

print("Output: Length of Words are :",Words_lengths )


#Q2.2)Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.

# FUnction to check char is vowel and return True/False
def vowel_check(char):
 if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
  return True
 else:
  return False

# Take user input
char = input("Enter character: ");

# If Invalid input, exit
if (char.isalpha() == False):
 exit();

# Invoke function
if (vowel_check(char)):
 print(char, "is a vowel.");
else:
 print(char, "is not a vowel."); 






















