import numpy as np 

#q1
a = np.array([[1,2,3],[4,7,8]])
for i in a:
    for j in i:
        print(j)

#q2
b = np.array([[[1,3,4,7],[8,10,6,2]],[[1,2,3,9],[8,4,2,10]]])
for i in np.nditer(b):
    if(i % 2 == 0):
        print(i)

#q3
c = np.arange(1,21)
d = c.reshape(4,5)
for i, j in np.ndenumerate(d):
    p = j*2
    print(i,p)

#q4
e = np.array([1,2,3,4,5])
f = np.copy(e)
e = np.array([i*2 for i in e]) 
print(f,e)

#q5
h = np.array([[1,2,3],[2,3,4]])
j = h[0,0:3].view()
h [0,0] = 34

print(j,h)