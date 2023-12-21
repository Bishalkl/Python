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
print(sorted(e)) # sorted use to sort a list in acending order

f = [1,2,3,4,5,9,7,10,12,11]
f.sort(reverse=True) # to sort it in reversed form we have to use reverse function
print(f)


#Set 
s1 = {1,2,3,4}
s2 = {1,2,3,5,6,8}

#add ,  Union(), intersection(), difference(), symmertic_difference()

print(s1.union(s2)) #it will combine like union but remove the repeated data

print(s1.intersection(s2)) #it will filter and give a data which already in to list 

print(s1.difference(s2)) #it will give only the value which is on the list 

print(s1.symmetric_difference(s2)) #it will remove common data and give output of all unique data of both list



#List comprehension

list_evenNumber =[ x for x in range(1,10) if x%2 == 0] 
print(list_evenNumber)

list_squarenumber =[x**2 for x in range(1,10)]
print(list_squarenumber)

#






