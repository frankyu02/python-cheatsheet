#this some API Shit
#JSON is quite literally just a Dictionary in Python

import json #JSON support

#sample data
data = '{"glossary": {  "title": "example glossary","GlossDiv": {"title": "S","GlossList": {"GlossEntry": {"ID": "SGML","SortAs": "SGML","GlossTerm": "Standard Generalized Markup Language","Acronym": "SGML","Abbrev": "ISO 8879:1986","GlossDef": {"para": "A meta-markup language, used to create markup languages such as DocBook.","GlossSeeAlso": ["GML", "XML"]},"GlossSee": "markup"}}}}}'

#parse json -> Dict

JSONdata = json.loads(data) 
print(JSONdata["glossary"])

print()

#dict -> JSON
car = {'make': 'Ford', 'model': 'X', 'year': 1994}
carJSON = json.dumps(car)
print(carJSON)