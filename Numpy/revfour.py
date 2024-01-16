import numpy as np
#BroadCasting 

a = np.array([[1,2,3],[1,2,3]])
b = np.array([[1,2,3]])
print(a * b)

#Indexing
example_array = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33]])
print(example_array[1,1])

#Slicing
practice_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(practice_array[3:8])
print(practice_array[::-1])