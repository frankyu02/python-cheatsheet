name = "Tommy"
age = 37

#concatination
print('name: ' + name)

#print('age' + age) will return an error

print('age: ' + str(age))

#position arguments
print('Name: {n}, Age: {a}'.format(n=name, a=age))

#f-Strings version 3.6+
print(f'Fstring Name: {name}. Age: {age}') #variables here must be defined

#string methods
s = "hello world"

#capitalization
print(s.capitalize())

#uppercase
print(s.upper())

#lowercase
print(s.lower())

#swapcase: A -> a, a -> A
print(s.swapcase())

#length
print(len(s))

#place
print(s.replace('world', 'everyone'))

#------Boolean Functions---------------

#startswith
print(s.startswith('hello'))

#endswith

print(s.endswith('d'))

#split returns a list
#default splits on space, specifics can be passed as parameters
print(s.split())

#find position returns index of first found case or -1 if not found
print(s.find('r'))

#----The following functions splits Strings by space for return value----

noSpace = 'helloworld'

#check if all elements of string are alphaneumeric
print(s.isalnum()) #false
print(noSpace.isalnum()) #true

#check if all letters are alphabetic
print(s.isalpha()) #false
print(noSpace.isalpha())#true

#check if value is neumeric
num = "1234"
print(s.isnumeric()) #false
print(num.isnumeric()) #true

