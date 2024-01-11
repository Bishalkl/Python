import numpy as np
# Data Type of NumPy

#question one 

#create 
int_arr = np.array([1,2,3,4,5], dtype='f') #changing the data type with character value function
float_arr = np.array([1.2,3.4,34.3],dtype=int) #chaning the datatype with the keyword of datatype
complex_arr= np.array([1+2j,3-4j,5+6j])

# display datatype
print(int_arr.dtype) #int 64
print(float_arr.dtype) #float 64
print(complex_arr.dtype) #complex128


#changing the value with astype
int1_arr = np.arange(10)
float1_arr = int1_arr.astype(float)
print(int1_arr)
print(float1_arr)


#Arthimetic Operation in numpy

#numpy arthimetic operation in only 1d arrays with only one value

add_arr = np.array([1,2,3,4,4])
resutl_arr = 23 + add_arr
print(resutl_arr)

#numpy arthimetic operation in  only 1d arrrays with another 1d arrays
mulitply_arr = np.arange(1,9)
mulitply2_arr = np.arange(11,19)
result2_arr = mulitply_arr * mulitply2_arr
print(result2_arr)

#numpy arthimetic operation in 2d arrays with another 2d array
first_arr = np.arange(1,10)
first_main_arr = first_arr.reshape(3,3)

second_arr = np.arange(1,10)
second_main_arr = second_arr.reshape(3,3)

resutl_Main = np.mod(first_arr,second_arr)
print(resutl_Main)
