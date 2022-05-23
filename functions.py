#functions run when called. This is similar across almost every single language...

#Declaration
def foo(params):
    print('Hello World' + str(params))

def fooWithDefault(param=""):
    print(param)

def add(a):
    a += 1
    return a

foo('yes') #prints('yes');
fooWithDefault() #prints("")
fooWithDefault('hello') #prints('hello')

num = 2
print(add(num)) #prints(3)

#lambda functions can only have one expression
addd = lambda a : a + 1

print(addd(5))