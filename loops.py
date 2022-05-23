#Python Loop notation is weird, stupid, and annoying

#For Loops is an Iterator

#simple for loop
for i in range(5):
    print('bruh') #this loops 5 times

print()
#looping through a string
x = "hello world"
for str in x:
    print(str) #this prints every char in "hello world"

print()
#looping through lists/typles/dicts/sets
numbers = [1,2,3,4,5]
for num in numbers:
    print(num)

print()
#break exists. It does what break does in every other language break exists in
for i in range(5):
    if(i == 3):
        break #Loop terminates at i = 3
    print(i)
print()
#continue exists. It does what continue does in every other language continue exists in
for i in range(5):
    if(i == 3):
        continue #loop skips printing i when i = 3 but loop does not terminate
    print(i)
print()

#While Loops do what while loops do
counter = 0
while(counter < 10):
    print(counter)
    counter += 1 