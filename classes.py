#ooo OOP fun stuff 

#Declaration
from pkgutil import extend_path


class Book:
    #constructor always follows format def __init__(self, ...params):
    def __init__(self, title="book", author="sam", pages=0):
        self.__title = title #adding __ before a variable makes it private
        self.__author = author
        self.__pages = pages

    def info(self):
        return f'Title: {self.__title}, Author: {self.__author}, Has: {self.__pages} page(s)'
    def greet(self):
        print('Hello!')

MTS = Book()
print(MTS.info())
MTS.greet()

#extending classes
class Comic(Book):
    def __init__(self, title="book", author="sam", pages=0, characters=[]):
        self.title = title #this title variable is public because of no __
        self.author = author 
        self.pages = pages
        self.characters=characters
    def info(self): #Comic's info function
        return f'Characters: {", ".join(self.characters)}'

chars = ["superman", "iron man", "black Widow"]
marvel = Comic("Marvel", "Mr Marvel", 30, chars)
print(marvel.info())
marvel.greet() #classes that extends another also have access to the original class's methods
