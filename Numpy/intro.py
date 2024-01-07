#importing numpy module
import numpy as np

#Creating rom a list 
my_list = [1,2,3] #first creating a list
my_arrays = np.array(my_list) # And converting into numpy arrays and also storing into variable my_arrays.
print(my_arrays)

#Creating  a Tuple 
my_tuple = (4,5,6) #first creating a tuple 
my_array_from_tuple = np.array(my_tuple)
print(my_array_from_tuple)

#Creating Zeros and Ones Arrays:
zero_array = np.zeros(4) # it will make 4 zero matrix
one_array = np.ones((3,4)) # it will make 3 dimension and 4 ones' value in each arrays 
print(one_array)
print(zero_array)

#Creating Range Arrays:
range_array = np.arange(0,10,) #it will work like a range in loop
print(range_array)

#creating Linspace Arrays
linspace_array = np.linspace(1,20,5)
print(linspace_array)

#Shape and Dimension
new_array = np.array([1,2,3,4,5])
print(new_array.shape)
print(new_array.ndim)  

