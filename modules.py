#A Module is a file containing a set of functions to include in your application. Theyre basically libraries
#there are code python modules, modules you can install using pip package manager
#you can also make custom modules


#default modules
import datetime #import entire module
today = datetime.date.today()

from datetime import date #import specific functions from a module
today2 = date.today()

import time
Time = time.time()

from time import time
time2 = time()

#you can do the same by installing modules using pip

#custom Modules
from customModule import add1 #from customModule.py, take specific functions
print(add1(3))

from classes import Book
wiki = Book('wikipedia', 'bobby', 333)
print(wiki.info())