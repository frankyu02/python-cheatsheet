#god if ur here looking at how conditionals work, you better have gotten permanent brain damage or something
x = 4
y = 1
#if/else statements do what if/else statements do

#comparitors
if(x == y):
    print('yee')
else:
    print('haw')

if(x > y):
    print('gee')
elif(x == y):
    print('gaw')
else:
    print('g')

#now in python, you have connectors in the form of 'and', 'or', 'not'. very cool
if x > y and x % 2:
    print('thee')
elif x > y and not(x % y):
    print('thaw')
else:
    print('th')

#not(x==y) is the same as (x != y) however !(x == y) does not work. (thanks Python)


#Membership Operators
#usually for lists

#in
numbers = [1,2,3,4,5]
if x in numbers:
    print('awdad')
else: 
    print('joe')

#not in
if x not in numbers:
    print('awofhaoeifh')
else:
    print('joe')

#Identity Operators compare two values to see if they are exactly equal

z = str(x)
#is
if x is z:
    print('hehe')
elif(x is y):
    print('gagaga')
elif(x is x):
    print('zaza')
else:
    print('zozozozoasf')

#is not
if x is not z:
    print('death is inevitable')
else:
    print('jk')