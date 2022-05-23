#Lists: pretty much Arrays

#declaration
empty = []
numbers = [1,2,3,4,5]
strings = ["hello", 'world', 'it', 'is me']

#lists are 0 based i.e 
print(f'number: {numbers[0]}') #prints 1
print(f'String: {strings[0]}') #prints 1

#length of a list
print(f'length of numbers[]: {len(numbers)}') #5
print(f'length of strings[]: {len(strings)}') #4
print(f"length of empty[] {len(empty)}") #0

#appending aka push to back of list
numbers.append(6) #legal
numbers.append("yo") #also legal

#removing
numbers.remove('yo')

#popping: removed from index

numbers.pop(2) #value must be in range of array

#insert: add to specific index
strings.insert(2, 'jo mama') #now 3rd item of the strings list is 'jo mama' everything else pushed back

#Reverse List reverts the position of the list contents

#sort list (default = alphaneumeric)
# you can also sort in reverse by passing (reverse=True) as a parameter
numbers.sort()

#replace: no function but just set the value manually
numbers[0] = 909