import math

class Factorial_Iter:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        else:
            result = math.factorial(self.i)
            self.i += 1
            return result

fact_iter = Factorial_Iter(5)
for i in fact_iter:
    print(i)

def fact():
    i = 0
    def inner():
        nonlocal i
        result = math.factorial(i)
        i += 1
        return result
    return inner  

fact_iter = iter(fact(), math.factorial(5))
for i in fact_iter:
    print(i)

def function():
    print('line 1')
    yield 'Flying'
    print('line 2')
    yield 'Circus'   

get_function = function()
next(get_function)
next(get_function)
'__next__' in dir(get_function)

def squares(num):
    i = 0
    while True:
        if i < num:
            result = i**2
            i += 1
            yield result
        else:
            return 'all done!'

for i in squares(5):
    print(i)

def factorials(n):
    for i in range(n):
        yield math.factorial(i)    

for i in factorials(5):
    print(i)

list(factorials(5))

def squares_gen(n):
    for i in range(n):
        yield i ** 2

square = squares_gen(5)
for i in square:
    print(i)

class Squares:
    def __init__(self, n):
        self.n = n
        
    @staticmethod
    def squares_gen(n):
        for i in range(n):
            yield i ** 2
        
    def __iter__(self):
        return Squares.squares_gen(self.n)

for i in Squares(5):
    print(i)

print([i ** 2 for i in range(5)])

g = (i ** 2 for i in range(5))
for item in g:
    print(item)

import dis
dis.dis(compile('[i**2 for i in range(5)]', filename='<string>', mode='eval'))

start = 1
stop = 10

multiple_list = [ [i * j 
               for j in range(start, stop+1)]
             for i in range(start, stop+1)]
print(multiple_list)

from math import factorial

def combo(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

size = 10  # global variable
pascal = [ [combo(n, k) for k in range(n+1)] for n in range(size+1) ]
print(pascal)

from timeit import timeit
size = 600
timeit('[[combo(n, k) for k in range(n+1)] for n in range(size+1)]',
      globals=globals(), number=1)

size1 = 100_000
timeit('([combo(n, k) for k in range(n+1)] for n in range(size1+1))',
      globals=globals(), number=1)

import tracemalloc

def pascal_list(size):
    l = [[combo(n, k) for k in range(n+1)] for n in range(size+1)]
    for row in l:
        for item in row:
            pass
    stats = tracemalloc.take_snapshot().statistics('lineno')
    print(stats[0].size, 'bytes')

def pascal_gen(size):
    g = ((combo(n, k) for k in range(n+1)) for n in range(size+1))
    for row in g:
        for item in row:
            pass
    stats = tracemalloc.take_snapshot().statistics('lineno')
    print(stats[0].size, 'bytes')
    
tracemalloc.stop()
tracemalloc.clear_traces()
tracemalloc.start()
pascal_list(300)

tracemalloc.stop()
tracemalloc.clear_traces()
tracemalloc.start()
pascal_gen(300)

def matrix(n):
    gen = ( (i * j for j in range(1, n+1))
            for i in range(1, n+1)
          )
    return gen

print(list(matrix(5)))

def matrix_iterator(n):
    for row in matrix(n):
        for item in row:
            yield item

for i in matrix_iterator(3):
    print(i)


