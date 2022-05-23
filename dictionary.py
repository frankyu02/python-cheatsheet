#Collection of Items unordered, changeable and indexed. No duplicates. It's an object-key pair is what this means.

#Declaration
numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'Name': 'john'
}

numbers2 = dict(one=1, two=2, three=3, four=4, five=5, Name="john") #constructor

#getting value
print(numbers['one']) #reference by key **common practice**
print(numbers.get('one'))#using .get()

#adding new entry to dict
numbers['six'] = 6

#get all dict Keys
print(numbers.keys()) #returns array of keys

#get all dict items
print(numbers.items())

#dictionary copy
numbers_copy = numbers.copy() #copys values not reference

#remove item
del(numbers['one']) 
numbers.pop('two')

#clear dict
numbers2.clear()

#length
print(len(numbers_copy))

#list(array) of dictionaries
dictionaries = [
    {
        'thesaurus':'theo'
    },
    {
        'encyclopedia': 'Wikipedia'
    },
    numbers,
]
print(dictionaries)

#select from array of dicts
print(dictionaries[0]['thesaurus'])
print(dictionaries[1].get('encyclopedia'))

