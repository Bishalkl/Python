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