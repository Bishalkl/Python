#zeros: 

import numpy as np 
#q1
matrix_zero = np.zeros((3,3))
print(matrix_zero)

#q2
arr_zeros_8 = np.zeros(8)
print(arr_zeros_8)


#One

#q1
matrix_one = np.ones((2,4))
print(matrix_one)

#q2
arr_ones_6 = np.ones(6)
print(arr_ones_6)

#Empty

#q1
matrix_empty = np.empty((2,2))
print(matrix_empty)

#q2
arr_empty = np.empty(1)
print(arr_empty)


#Arrange:
#q1
arr_even = np.arange(2,10,2)
print(arr_even)

#q2
arr_1d = np.arange(1,10) #first make numpy list
arr_2d = arr_1d.reshape((3,3)) #and reshape the matrix 
print(arr_2d)
