#VARIABLE MEMORY LOCATION
variable = 100
print('Memory location: {0} '.format(id(variable))) #base 10
print('Memory location: {0} '.format(hex(id(variable)))) #base 16

#REFERENCE COUNTING
import ctypes
from http.client import PROCESSING
import sys
from tkinter import Y

def reference_count(address):
    return ctypes.c_long.from_address(address).value

print(reference_count(id(variable)))
print(sys.getrefcount(id(variable)))

#GARBAGE COLLECTION
import gc
def specific_id(variable_id):
    for x in gc.get_objects():
        if id(x) == variable_id:
            return True
    return False

class one:
    def __init__(self):
        self.b = two(self)
        print(hex(id(self)))
        print(hex(id(self.b)))
    
class two:
    def __init__(self,a):
        self.a = a
        print(hex(id(self)))
        print(hex(id(self.a)))

gc.disable()

variable = one()

#DYNAMIC TYPING
y = lambda x: x*x
print(type(y))
print(type(10))
print(type('Hi'))

#OBJECT MUTABILITY
list = [1,2,3,4,5]
print(list)
print(id(list))
print(hex(id(list)))

list.append(7) #memory address does not change
print(list)
print(id(list))

list = list + [8] #memory address changes
print(list)
print(id(list))

#In dictionaries the memory address does not change
dictionary = dict(K1 = 'Key 1')
print(dictionary)
print(id(dictionary))

dictionary['K1'] = 'New Key 1'
print(dictionary)
print(id(dictionary))

dictionary['K2'] = 'Key 2'
print(dictionary)
print(id(dictionary))

t = (1,2,3,4,5) #this tuple will never change

#this tuple's memory address does not change
a = [1,2,3]
b = [4,5,6]
t = (a,b)
print(t)
print(id(t))
a.append(4)
b.append(7)
print(t)
print(id(t))

#FUNCTION ARGUMENTS AND MUTABILITY
def process(x):
    print('Unchanged memory address: {0}'.format(hex(id(x))))
    x = x + 's'
    print('Memory address after change: {0}'.format(hex(id(x))))

variable_one = 'World'
print('Initial memory address: {0}'.format(hex(id(variable_one))))
process(variable_one) #After altering the string the memory address changes.


new_list = [1,2,3,4,5] #mutable object
def modify_list(items):
    print('Initial list address: {0}'.format(id(items)))
    print(items)
    if len(items) > 0:
        items[0] = items[0] ** 2 
    items.pop()
    items.append(6)
    print(items)
    print('Final memory address: {0}'.format(id(items)))

modify_list(new_list) #after altering the list the memory address does not change. 

new_tuple = ([1,2],[4,5]) 
def modify_tuple(items):
    print(items)
    print('Initial memory address: {0}'.format(id(items)))
    items[0].append(3)
    print(items)
    print('Final memory address: {0}'.format(id(items)))

modify_tuple(new_tuple) #after altering the tuple the memory address doesn't change.

#SHARED REFERENCES AND MUTABILITY
my_var = 'Hello World'
my_var2 = 'Hello World'
print('Variable One Contents: {0} Memory Address: {1}'.format(my_var,id(my_var)))
print('Variable Two Contents: {0} Memory Address: {1}'.format(my_var2,id(my_var2)))
my_var2 = my_var2 + '!'
print('Variables and their memory address after change.')
print('Variable One Contents: {0} Memory Address: {1}'.format(my_var,id(my_var)))
print('Variable Two Contents: {0} Memory Address: {1}'.format(my_var2,id(my_var2))) #the memory address of variable two has been changed.

my_list = [1,2,3,4,5]
my_list2 = my_list
print('List One: {0} Memory Address: {1}'.format(my_list,id(my_list)))
print('List Two: {0} Memory Address: {1}'.format(my_list2,id(my_list2)))
my_list2.append(6)
print('The lists and their memory address after change.')
print('List One: {0} Memory Address: {1}'.format(my_list,id(my_list)))
print('List Two: {0} Memory Address: {1}'.format(my_list2,id(my_list2))) #the memory address' of the list don't change

#VARIABLE EQUITY
var1 = 100
var2 = 100
print('var1 is var2: ', var1 is var2) #this returns true if the memory addresses are the same
print('var1 == var2: ',var1==var2) #this returns true if the contents of the variables are the same 

l1 = [1,2,3]
l2 = [1,2,3]
print(l1 is l2)
print(l1 == l2)

t1 = (1,2,3)
t2 = (1,2,3)
print(t1 is t2)
print(t1 == t2)

# the contents of the variables are all the same but the data types are different so the memory address' are different.
v1 = 10
v2 = 10.0
v3 = 10 + 0j
print('v1 is v2: ',v1 is v2)
print('v2 is v3: ', v2 is v3)
print(v1 == v2 == v3)

#PYTHON OPTIMIZATION  - INTERNING
x = 1000
y = 1000
print('x: {0}, y: {1}'.format(id(x),id(y)))

#PYTHON OPTIMIZATION - STRING INTERNING
sentence = 'Hello World !'
sentence2 = 'Hello World !'
print('sentence: {0}, sentence2: {1}'.format(id(sentence),id(sentence2)))
