#SEQUENCE TYPES
a = [1, 3, 2]
print(min(a), max(a))

s = 'python'
print(min(s), max(s))

print([1, 2, 3] * 5)
print(''.join(tuple('abc') + ('d', 'e', 'f')))

try:
    idx = s.index('n', 13)
except ValueError:
    print('not found')

print(s.index('n'))
print(s[0:3], s[4:6])

r = range(15)
print(r)
print(list(r))

hash(r)
hash(a)
hash(s)

from decimal import Decimal
hash(Decimal(10.5))

#MUTABLE SEQUENCES
list = [1, 2, 3, 4, 5]
print(id(list))
list[0] = 'a'
print(id(list), list)

list[0:2] = ['a', 'b', 'c', 'd', 'e']
print(id(list), list)

list.clear()
print(list)

list.extend(('a', 'b', 'c'))
print(list)

popped = list.pop()
print(id(list), popped, list)

list.insert(1, 'a')
print(id(list), list)

list.reverse()
print(id(list), list)

#LISTS VS TUPLES
from dis import dis

print(dis(compile('(1,2,3, "a")', 'string', 'eval')))
print(dis(compile('[1,2,3, "a"]', 'string', 'eval')))

from timeit import timeit
timeit("(1,2,3,4,5)", number=10_000_000)
timeit("[1,2,3,4,5]", number=10_000_000)

def function():
    pass
print(dis(compile('(function, 1, 2)', 'string', 'eval')))
print(dis(compile('[function, 1, 2]', 'string', 'eval')))

import sys
prev = 0
for i in range(10):
    c = tuple(range(i+1))
    size = sys.getsizeof(c)
    delta, prev = size - prev, size
    print(f'{i+1} items: {size}, delta={delta}')

c = []
prev = sys.getsizeof(c)
print(f'0 items: {sys.getsizeof(c)}')
for i in range(255):
    c.append(i)
    size = sys.getsizeof(c)
    delta, prev = size - prev, size
    print(f'{i+1} items: {size}, delta={delta}')

tuple1 = tuple(range(100_000))
timeit('tuple1[99_999]', globals=globals(), number=10_000_000) #same for lists

#COPYING SEQUENCES
l1 = [1, 2, 3]

l1_copy = []
for item in l1:
    l1_copy.append(item)

print(l1_copy)
print(id(l1),id(l1_copy)) #not the same

l2 = [1, 2, 3]
l2_copy = [item for item in l2]
print(l2_copy)
print(id(l2),id(l2_copy))

l3 = [1, 2, 3]
l3_copy = l3.copy()
print(l3_copy)
print(id(l3),id(l3_copy))

t1 = (1, 2, 3)
t1_copy = tuple(t1)
print(t1_copy)
print(id(t1),id(t1_copy)) #the same

s1 = 'python'
s1_copy = str(s1)
print(s1_copy)
print(s1 is s1_copy)

p1 = [0, 0]
p2 = [0, 0]

line1 = [p1, p2]
print(line1)
print(id(line1[0]), id(line1[1]))

line2 = line1.copy()
print(line1 is line2)
print(id(line1[0]), id(line1[1]))
print(id(line2[0]), id(line2[1]))

line2[0][0] = 100
print(line2)
print(line1)

line3 = [item[:] for item in line1]
print(id(line1[0]), id(line1[1]))
print(id(line3[0]), id(line3[1]))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'Point({self.x}, {self.y})'
    
class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
    def __repr__(self):
        return f'Line({self.p1.__repr__()}, {self.p2.__repr__()})'

point1 = Point(0, 0)
point2 = Point(10, 10)
line_1 = Line(p1, p2)
line_2 = line_1.copy()

print(line_1.point1, id(line_1.point1))
print(line_2.point1, id(line_2.point1))

#SLICING
slice1 = slice(0, 2)
type(slice1)
slice1.start
slice1.stop

data = []  # a collection of rows, read from a file maybe
for row in data:
    first_name = row[0:51]
    last_name = row[51:101]
    ssn = row[101:111]

range_first_name = slice(0, 51)
range_last_name = slice(51, 101)
range_ssn = slice(101, 111)

for row in data:
    first_name = row[range_first_name]
    last_name = row[range_last_name]
    ssn = row[range_ssn]

print(slice(1, 5).indices(10))
print(list(range(*slice(None, None, -1).indices(10))))

#CUSTOM SEQUENCES
my_list = [0, 1, 2, 3, 4, 5]
my_list.__getitem__(5)
my_list.__getitem__(-1)
my_list.__getitem__(slice(0,6,2))
my_list.__getitem__(slice(None, None, -1))

for item in my_list:
    print(item ** 2)

class MySequence:
    def __getitem__(self, index):
        print(type(index), index)
    
my_seq = MySequence()
my_seq[0]

from functools import lru_cache

class Fibonacci:
    def __init__(self, n):
        self._n = n
    
    def __getitem__(self, s):
        if isinstance(s, int):
            # single item requested
            print(f'requesting [{s}]')
        else:
            # slice being requested
            print(f'requesting [{s.start}:{s.stop}:{s.step}]')
            idx = s.indices(self._n)
            rng = range(idx[0], idx[1], idx[2])
            print(f'\trange({idx[0]}, {idx[1]}, {idx[2]}) --> {list(rng)}')
    
f = Fibonacci(10)
f[3:5]
f[::-1]

class MyClass:
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return f'MyClass(name={self.name})'
    
    def __add__(self, other):
        return MyClass(self.name + ' ' + other.name)
        
    def __iadd__(self, other):
        self.name += ' ' + other.name
        return self
    
    def __mul__(self, n):
        return MyClass(self.name * n)
        
    def __imul__(self, n):
        self.name *= n
        return self
    
    def __rmul__(self, n):
        self.name *= n
        return self

c1 = MyClass('Sid')
c2 = MyClass('Sand')

c3 = c1 + c2
print(c3)
print(2*c1)

