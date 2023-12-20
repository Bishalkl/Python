#Built-in Data structures

#creating in list
list1 = [1,2,3,"bishal","Animation",2, 4, 5, 6,]
print(list)

#add = append(), extend(), and insert()

b = [1,2,3,4,5,6]
b.append("Bishal") #append is use to data in list and will be store in last index
print(b)

c = [1,2,3,5,6,7,3,5,]
c.extend(("ANimation",8)) #it i will split if we put string single and also put double bracket to store it multiple data 
print(c)

d = [1,2,3,4,5]
d.insert(2,"bishal") #need index and also value where value should be put and will capture a other index value and push it next beyond it.
print(d)




#delete = del, pop(), remove()

del list1[0] # it is use to delete the data targeting the index of l
print(list1)

a = list1.pop(5) # it is use to pop the element and print it out in targeting the index of list
print(a)

list2 = [1,2,3,4,5,6,7,"komal", "Animation"] # it remove the data targeting the exact the value 
list2.remove("komal")
print(list2)


#sort: 
e = [1,2,3,12,9,17,45,25]
print(sorted(a))





