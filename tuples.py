#tuples are collections of items that are unchangeable. Allows for duplicates

#declaration
numbers = (1,2,3,4,5)
numbers2 = tuple((1,2,3,4,5)) #using contructor
numbers3 = (4) #this is an integer declaration
numbers4 = (4,) #this is now a tuple declaration
print(numbers) #(1, 2, 3, 4, 5)
print(len(numbers)) #5