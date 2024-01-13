#Arithmetic Function

import numpy as np 
# Q1
var = np.array([1,8,5,3,7])
print(np.mean(var))

#q2
var1 = np.array([[2,1,3],[9,5,6]])
print(np.add(var1[0],var1[1]))

#Square Root and Trigonometric Function:
# angles = np.array([0,np.pi/2,np.p1])
# tangent_value = np.tan(angles) #tanget mean tan 
# print(tangent_value)

var3 = np.array([4,16,25])
print(np.sqrt(var3))


#Cumulative Sum:

# q1
nums = np.array([1,2,3,4,5])
print(np.cumsum(nums))

# q2
var5 = np.array([2,4,1,7,3])
result = np.cumsum(var5)
print(result)
for i  ,value in enumerate(result):
    if(value >= 10):
        print(f"Index is {i} here the value exceeds 10 and value is {value}.")
        break

#Shape and Reshape

#Q1
arr = np.array([[5,8,2],[3,1,7]])
print(np.size(arr))

#Q2
arrs = np.array([1,2,3,4])
result_reshape = arrs.reshape(2,2)
print(result_reshape)








