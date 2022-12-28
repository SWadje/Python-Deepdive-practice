#LAMBDA EXPRESSIONS
function = lambda x: x**2
function(2)
func = lambda x, *args, y, **kwargs: (x, *args, y, {**kwargs})
func(1, 'a', 'b', y=2, a=3, b=4)

def apply_function(x, fn):
    return fn(x)
apply_function(4, lambda x: x**2)

def apply_function2(fn, *args, **kwargs):
    return fn(*args, **kwargs)
apply_function2(lambda x, y: x+y, 1, 2)
apply_function2(lambda x, y: x*y, 'a', 4)

#LAMBDAS AND SORTING
list = ['A','c','d','B']
sorted(list, key=str.upper)
dict = {'def': 2, 'abc': 1, 'ghi': 3}
sorted(dict)
sorted(dict, key=lambda k: dict[k])

import random
random.random()
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sorted(list2, key=lambda x: random.random())
sorted('python', key=lambda x: random.random())

#FUNCTION INTROSPECTION
def factorial(n):
    if n < 0:
        return 0
    elif n <= 1:
        return 1
    else:
        return n * factorial(n-1)

factorial.short_description = "Calculating factorial "
factorial(3)

def my_function(a, b=1, *args, **kwargs):
    i = 10
    b = min(i, b)
    return a * b
my_function('s', 100)

import inspect
inspect.isfunction(my_function)
inspect.ismethod(my_function)

class Class:
    def f_instance(self):
        pass
    
    #classmethod
    def f_class(cl_ass):
        pass
    
    #staticmethod
    def f_static():
        pass

inspect.isfunction(Class.f_instance), inspect.ismethod(Class.f_instance)
inspect.isfunction(Class.f_class), inspect.ismethod(Class.f_class)
inspect.isfunction(Class.f_static), inspect.ismethod(Class.f_static)

object = Class()
inspect.isfunction(object.f_instance), inspect.ismethod(object.f_instance)
inspect.isfunction(object.f_class), inspect.ismethod(object.f_class)
inspect.isfunction(object.f_static), inspect.ismethod(object.f_static)


def information(f: "callable") -> None:
    print(f.__name__)
    print('=' * len(f.__name__), end='\n\n')
    
    print('{0}\n{1}\n'.format(inspect.getcomments(f), 
                              inspect.cleandoc(f.__doc__)))
    
    print('{0}\n{1}'.format('Inputs', '-'*len('Inputs')))
    
    sig = inspect.signature(f)
    for param in sig.parameters.values():
        print('Name:', param.name)
        print('Default:', param.default)
        print('Annotation:', param.annotation)
        print('Kind:', param.kind)
        print('--------------------------\n')
        
    print('{0}\n{1}'.format('\n\nOutput', '-'*len('Output')))
    print(sig.return_annotation)

information(my_function)
