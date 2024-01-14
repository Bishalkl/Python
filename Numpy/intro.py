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

#zero
ar_zero = np.zeros(4)
print(ar_zero)

ar_zero1 = np.zeros((4,3))
print(ar_zero1)

#Ones
ar_one = np.ones(5)
print(ar_one)

#Empty
ar_em = np.empty(5)
print(ar_em)

#Arrange
ar_rn = np.arange(4)
print(ar_rn)

#Diagonal
ar_dia = np.eye(5) #Diagonal
print(ar_dia)

#Linspace
ar_lin = np.linspace(0,20,num=5) 
print(ar_lin)

#Random Number

#rand()
rand_number = np.random.rand(2,4) #Generate a random number between 0 and 1 
print(rand_number)

#randn() #Generate a random number between close to zero and it could be both positive and negative 
randn_number= np.random.randn(4,3)
print(randn_number)

#ranf
ranf_number = np.random.ranf(3)
print(ranf_number)

#randint

#we should pust first min value and max and total value will generate a random value according to that range.
randint_number = np.random.randint(5,20,10)
print(randint_number)



#Arthimetic Function

var = np.array([1,2,3])

print(np.min(var)) #to get min value of arrays
print(np.max(var)) #to get max value of arrays
print(np.argmin(var)) #to get a index postion of min value 
print(np.argmax(var)) #to get a index postion of max value 

#axis = 0 for col
#axis = 1 for row

#using 2d arrays
var1 = np.array([[2,1,3],[9,5,6]])
print(np.min(var1,axis=0))
print(np.max(var1,axis=1))

#Squre root function
print(np.sqrt(var))

#sin  and cos function
print(np.sin(var))
print(np.cos(var))

#cumsum function
print(np.cumsum(var)) #adding the value of each after each and it is use in statitisc in median 

#Shape and reshape of numpy arrays

#shape check
shape_arr = np.array([[1,2,3],[1,3,4]])
print(shape_arr.shape)

#ndim function 
shape_arr1 = np.array([1,2,3,4], ndmin=4) #customize the dimension
print(shape_arr1)
print(shape_arr1.ndim) #check the dimension of arrrays
print(shape_arr1.shape)

#Reshape
shape_arr2= np.array([1,2,3,4,5,6,7,8,9,2,3,4,2,3,4,4,4,4])
reshape_arr = shape_arr2.reshape(3,2,3)

print(reshape_arr)
print(reshape_arr.ndim) 
print(reshape_arr.shape)

print(reshape_arr.reshape(-1)) #to reshape the arrays


#Boardcasting
#to avoid Broadcasting
# -same Dimension
#-should be one in minimum data array

a = np.array([1,2,3])
print(a.shape)
b = np.array([[1],[2],[3]])
c = a + b
print(c)

#Indexing Numpy Arrays

#1D index
var_1d = np.array([1,2,3,4,5])
print(var_1d[-1])

#2D index
var_2d = np.array([[2,3],[3,7]])
print(var_2d[1,0])

#3d index
var_3d = np.array([[[1,2],[3,6]],[[1,2],[4,5]]])
print(var_3d[1,0,0])

#Slicing NumPy Arrays

#1d dimension
var_a = np.array([1,2,3,4,5,6,7,8,9,10])
print(var_a[1:3]) #give starting point to given end point
print(var_a[:4]) #starting point to given point
print(var_a[::]) #strting point to ending point
print(var_a[::2]) # gap fo 2 from starting point to ending point
print(var_a[::-1]) #reversed array

#multiple dimension
var_b = np.array([[1,2,3,4],[1,2,4,5]])
print(var_b[1,::-1])




