#collection of items which are unordered and unindexed. No Duplicates allowed.

#Declaration
numbers = {1,2,3,4,5}
print(numbers) #{1, 2, 3, 4, 5}

#check if element exists in a set
print(2 in numbers)

#Add to a set
#if a duplicate is added, set will not update
numbers.add(6)

#remove from a set
numbers.remove(2)

#clear set
numbers.clear()

#deletion
del numbers