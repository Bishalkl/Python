#Practise one 
my_list = [10, 20, 30, 40, 50]
print(my_list[1:4:1])
#The value at index 2 is 30.

#practise two
fav_fruits = ["Apple", "Orange", "Pineapple", "Mango"]
fav_fruits.append("Grapes")
print(fav_fruits)
#The pop() method are those method which are use to pop out the value from list according to the index value and return.

#practise three
my_squarelist = [x**2 for x in range(1,6)]
print(my_squarelist) 

#practise four
#If we modifiy any element at a specific index then it will change the value of specific index for example:
a = [1,2,3,4,5,6]
a[2] = 4 # it will change the value 
a.insert(3,"Bishal") # but from insert it will push the before value beside and value in that index.
print(a)

#practise five
nested_list = [[1,2,3], [4,5,6]]
print(nested_list[0])
print(nested_list[1][1])

#practise six
favorite_book = {"title": "Ai and Human", "author": "Jeffery himston", "publication_year" : 2001}
print(favorite_book)

#practise seven
for i in favorite_book.items():
    print(i)

a = [x for x in favorite_book.keys()]
b = [ x for x in favorite_book.values()]
print(a)
print(b)


#practise eight
c = { x: x**2 for x in range(1,6)}
print(c)

#practise nine
favorite_book['author'] = "Bishal koirala" # updating 
del favorite_book['title'] #deleting  the value
favorite_book['publication_year'] = 2005
print(favorite_book)

#practise 10
evenNumber = {2,4,6,8}
primeNumber = {2,3,5,7}
union = evenNumber.union(primeNumber) #union
print(union)

#practise 11
A = {1,2,3}
B = {3,4,5}

intersection_number = A.intersection(B) #intersection

difference_number = A.difference(B) #difference_number
print(intersection_number, difference_number)

#practise 12
fav_color = ("Red", "Blue", "Green", "purple")
print(fav_color)
#tuple = tuple are also the data structure but they are immutable.
print(fav_color)
#tuple does not support item assignment

#practise 13
squares_set = {x**2 for x in range(1,6)}
print(squares_set)

print("Hello world hi hello hello hello")