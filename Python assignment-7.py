#Q1)Write a function so that the columns of the output matrix are powers of the input vector. The order of the powers is determined by the increasing boolean argument. Specifically, when increasing is False, the i-th output column is the input vector raised element-wise to the power of N - i - 1.

# Import libraries

import numpy as num_py

# Function
def matrix_Vandermonde(input_vector,n,bool_arg):
    '''This function Will return Matrix in which 
    the columns of the output matrix are powers of the input vector.'''
    
    output_matrix=num_py.vander(x=input_vector,N=n,increasing=bool_arg)
    return output_matrix

# input paramater
input_vector = num_py.arange(5,13,2)   # input vector ( 1-D array)
n = 5                                  # no. of column in matrix 
bool_arg_T = True                      # boolean argument
bool_arg_F = False                     # boolean argument

# function execution
out_matrix_True=matrix_Vandermonde(input_vector,n,bool_arg_T)

out_matrix_False=matrix_Vandermonde(input_vector,n,bool_arg_F)

#output
print("Input vector \n",input_vector,"\n")
print("Output Matrix , when boolean argument is True: \n",out_matrix_True,"\n")
print("Output Matrix , when boolean argument is False: \n",out_matrix_False)


#Q2)Write a function to find moving average in an array over a window: Test it over [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150] and window of 3.

# Moving average sequence
# formula for Moving average sequence is n-k+1  ; 
# where n -:is no. of elements  , k is window for which moving average sequence has to be create
    

# function
def moving_average_seq(input_array,k):
    ''' This function will return moving average in an array.'''
    val_array=num_py.cumsum(input_array,dtype=float)    
    val_array[3:]=val_array[3:]-val_array[:-3]
    return val_array[3-1:]/3

#input values 
lst =[3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
input_array = num_py.array(lst)
    
# output 
# Thus, total movieng average sequence are 13-3+1 = 11 values  ; where n=13 , k=3
output_array=moving_average_seq(input_array,k=3)
print("Input: Moving average of values ",lst," are :\n")
print("Output:\n",output_array)





