
s = {'a', 100, (1,2)}
s1 = set(range(10))
print(s)
print(s1)

d = {'a': 1, 'b': 2}
s2 = set(d)

for e in d:
    print(e)

def my_func(a, b, c):
    print(a, b, c)
a = {20, 10, 30}
my_func(a)

def averager(*args):
    total = 0
    for arg in args:
        total += arg
    return total / len(args)
averager(10,20,30)

s3 = 'abcdefghijklmnopqrstuvwxyz'
distinct = set(s)
score = len(s) / 26
print(score)

def scorer(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    s = s.lower()
    distinct = set(s)
    effective = distinct & alphabet
    return len(effective) / len(alphabet)

scorer('hello world')


s4 = {1, 2, 3}
len(s4)

print(1 in s4)
print(10 in s4)

from timeit import timeit

n = 100_000
s5 = {i for i in range(n)}
l = [i for i in range(n)]
d = {i:None for i in range(n)}

number = 3_000
search = 99_999
t_list = timeit(f'{search} in l', globals=globals(), number=number)
t_set = timeit(f'{search} in s5', globals=globals(), number=number)
t_dict = timeit(f'{search} in d', globals=globals(), number=number)
print('list:', t_list)
print('set:', t_set)
print('dict:', t_dict)

number = 3_000
search = -1
t_list = timeit(f'{search} not in l', globals=globals(), number=number)
t_set = timeit(f'{search} not in s5', globals=globals(), number=number)
t_dict = timeit(f'{search} not in d', globals=globals(), number=number)
print('list:', t_list)
print('set:', t_set)
print('dict:', t_dict)

s5.add(10)
d[10] =None
l.append(10)

print(d.__sizeof__())
print(s5.__sizeof__())
print(l.__sizeof__())

list = list()
set = set()
dict = dict()

print('#', 'dict', 'set', 'list')
for i in range(50):
    print(i, dict.__sizeof__(), set.__sizeof__(), list.__sizeof__())
    list.append(i)
    set.add(i)
    dict[i] = None


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    def __repr__(self):
        return f'Person(name={self._name}, age={self._age})'
    
    @property
    def name(self):
        return self._name
        
    @property
    def age(self):
        return self._age
    
    def key(self):
        return frozenset({self.name, self.age})

p1 = Person('John', 78)
p2 = Person('Eric', 75)

dict1 = {p1.key(): p1, p2.key(): p2}
print(dict1)

from functools import lru_cache
@lru_cache()
def my_func(*, a, b):
    print('calculating a+b...')
    return a + b

my_func(a=1, b=2)

def memoizer(fn):
    cache = {}
    def inner(*args, **kwargs):
        key = (*args, frozenset(kwargs.items()))
        if key in cache:
            return cache[key]
        else:
            result = fn(*args, **kwargs)
            cache[key] = result
            return result
    return inner

@memoizer
def my_func(*, a, b):
    print('calculating a+b...')
    print(a + b)

@memoizer
def adder(*args):
    print('calculating...')
    print(sum(args))


my_func(a=1, b=2)
adder(1, 2, 3)

from timeit import timeit
from random import randint

d1 = {k: randint(0, 100) for k in range(10_000)}
keys = d1.keys()

def iter_direct(d1):
    for k in d1:
        pass
    
def iter_view(d1):
    for k in d1.keys():
        pass

def iter_view_direct(view):
    for k in view:
        pass
    
print(timeit('iter_direct(d)', globals=globals(), number=20_000))
print(timeit('iter_view(d)', globals=globals(), number=20_000))
print(timeit('iter_view_direct(keys)', globals=globals(), number=20_000))

d2 = {k: randint(0, 100) for k in range(10_000)}
items = d2.items()

def iterate_view(view):
    for k, v in view:
        pass
    
def iterate_clunky(d2):
    for k in d2:
        d2[k]
        
print(timeit('iterate_view(items)', globals=globals(), number=5_000))
print(timeit('iterate_clunky(d)', globals=globals(), number=5_000))