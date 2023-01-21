def squares(n):
    for i in range(n):
        yield i**2
    
list(squares(5))
print(min(squares(5)),max(squares(5)))

class Person:
    pass

p = Person()
bool(p)

class MySeq:
    def __init__(self, n):
        self.n = n
        
    def __len__(self):
        return self.n
    
    def __getitem__(self, s):
        pass

bool(MySeq(0))
bool(MySeq(10))

all([1, 'abc', [1, 2], range(5)])
all([1, 'abc', [1, 2], range(5), ''])

from numbers import Number
print(isinstance(10, Number), isinstance(10.5, Number))
print(isinstance(2+3j, Number))

from decimal import Decimal
print(isinstance(Decimal('10.3'), Number))

l = [10, 20, 30, 40]

is_all_numbers = True
for item in l:
    if not isinstance(item, Number):
        is_all_numbers = False
        break
print(is_all_numbers)

g = [10, 20, 30, 40, 'hello']
is_all_numbers = False
for item in g:
    if not isinstance(item, Number):
        break
else: 
    is_all_numbers = True
print(is_all_numbers)
all(map(lambda x: isinstance(x, Number), g))

map(str, [0, 1, 2, 3, 4])
list(map(str, [0, 1, 2, 3, 4]))
list(map(lambda x: isinstance(x, Number), l))

s = slice(0, 2)
l[s]

import math
def factorials(n):
    for i in range(n):
        yield math.factorial(i)
facts = factorials(100)
facts[0:2]

def slice_(iterable, start, stop):
    for _ in range(0, start):
        next(iterable)
        
    for _ in range(start, stop):
        yield(next(iterable))

list(slice_(factorials(100), 1, 5))
list(factorials(10))

from itertools import islice
islice(factorials(10), 0, 3)
list(islice(factorials(10), 0, 3))
list(islice(factorials(10), 0, 10, 2))
list(islice(factorials(10), None, None, 2))

for _ in range(5):
    print(next(facts))

def factorials_1():
    index = 0
    while True:
        print(f'yielding factorial({index})...')
        yield math.factorial(index)
        index += 1

list(islice(factorials_1(), 9))
list(islice(factorials_1(), None, 10, 2))

facts = factorials_1()
next(facts), next(facts), next(facts), next(facts)

def gen_cubes(n):
    for i in range(n):
        print(f'yielding {i}')
        yield i**3

def is_odd(x):
    return x % 2 == 1

is_odd(4)
is_odd(81)

filtered = filter(is_odd, gen_cubes(10))
list(filtered)

def is_even(x):
    return x % 2 == 0
list(filter(is_even, gen_cubes(10)))

from itertools import filterfalse
evens = filterfalse(is_odd, gen_cubes(10))
list(evens)

from math import sin, pi

def sine_wave(n):
    start = 0
    max_ = 2 * pi
    step = (max_ - start) / (n-1)
    for _ in range(n):
        yield round(sin(start), 2)
        start += step    

print(list(sine_wave(15)))

from itertools import takewhile
list(takewhile(lambda x: 0 <= x <= 0.9, sine_wave(15)))

from itertools import dropwhile
list(dropwhile(lambda x: x < 5, l))

data = ['a', 'b', 'c', 'd', 'e']
selectors = [True, False, 1, 0]
list(zip(data, selectors))
[item for item, truth_value in zip(data, selectors) if truth_value]

from itertools import compress
list(compress(data, selectors))

from itertools import (
    count,
    cycle,
    repeat, 
    islice)

list(islice(count(10, step=2), 5))
list(islice(count(1+1j, 1+2j), 5))

from decimal import Decimal
list(islice(count(Decimal('0.0'), Decimal('0.1')), 5))
list(islice(cycle(('red', 'green', 'blue')), 8))

def colors():
    yield 'red'
    yield 'green'
    yield 'blue'

cols = colors()
list(cols)
list(islice(cycle(cols), 10))

from collections import namedtuple
Card = namedtuple('Card', 'rank suit')
def card_deck():
    ranks = tuple(str(num) for num in range(2, 11)) + tuple('JQKA')
    suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
    for suit in suits:
        for rank in ranks:
            yield Card(rank, suit)

hands = [list() for _ in range(4)]
index = 0
for card in card_deck():
    index = index % 4
    hands[index].append(card)
    index += 1

print(hands)

hands_1 = [list() for _ in range(4)]
index_cycle = cycle([0, 1, 2, 3])
for card in card_deck():
    hands[next(index_cycle)].append(card)

print(hands_1)

hands = [list() for _ in range(4)]
hands_cycle = cycle(hands)
for card in card_deck():
    next(hands_cycle).append(card)
    print(hands_1)

for _ in range(5):
    print(next(repeat('Python')))

list(repeat('Python', 4))

l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4, 8))
l3 = (i**2 for i in range(8, 12))

for gen in (l1, l2, l3):
    for item in gen:
        print(item)

def chain_iterables(*iterables):
    for iterable in iterables:
        yield from iterable

l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4, 8))
l3 = (i**2 for i in range(8, 12))

for item in chain_iterables(l1, l2, l3):
    print(item)

from itertools import chain
for item in chain(l1, l2, l3):
    print(item)

lists = [l1, l2, l3]
for item in chain(*lists):
    print(item)

def squares():
    yield (i**2 for i in range(4))
    yield (i**2 for i in range(4, 8))
    yield (i**2 for i in range(8, 12))

for item in chain(*squares()):
    print(item)

for item in chain.from_iterable(squares()):
    print(item)

def chain_iter(iterable):
    for item in iterable:
        yield from item

maps = map(lambda x: x**2, range(5))
list(maps)
def add(t):
    return t[0] + t[1]

list(map(add, [(0,0), [1,1], range(2,4)]))
def add(x, y):
    return x + y
t = (2, 3)
add(*t)

list(map(add, [(0,0), (1,1), (2,2)]))

from itertools import starmap
list(starmap(add, [(0,0), (1,1), (2,2)]))
sum([10, 20, 30])

from functools import reduce
reduce(lambda x, y: x*y, [1, 2, 3, 4])

def sum_(iterable):
    it = iter(iterable)
    acc = next(it)
    yield acc
    for item in it:
        acc += item
        yield acc

for item in sum_([10, 20, 30]):
    print(item)

def running_reduce(fn, iterable, start=None):
    it = iter(iterable)
    if start is None:
        accumulator = next(it)
    else:
        accumulator = start
    yield accumulator
    
    for item in it:
        accumulator = fn(accumulator, item)
        yield accumulator

import operator
list(running_reduce(operator.add, [10, 20, 30]))

from itertools import accumulate
list(accumulate([10, 20, 30]))

def integers(n):
    for i in range(n):
        yield i
        
def cubes(n):
    for i in range(n):
        yield i**3

iter1 = integers(6)
iter3 = cubes(4)
list(zip(iter1,iter3))

from itertools import zip_longest
help(zip_longest)
list(zip_longest(l1, l2, l3, fillvalue='N/A'))
 
import itertools

def matrix(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            yield f'{i} x {j} = {i*j}'

list(itertools.islice(matrix(10), 10, 20))
list1 = ['x1', 'x2', 'x3', 'x4']
list2 = ['y1', 'y2', 'y3']
for x in l1:
    for y in l2:
        print((x, y), end=' ')
    print('')

list(itertools.product(list1, list2))
list(matrix(4))

def matrix2(n):
    for i, j in itertools.product(range(1, n+1), range(1, n+1)):
        yield (i, j, i*j)

list(matrix2(4))

from itertools import tee

def matrix3(n):
    return ((i, j, i*j) 
            for i, j in itertools.product(*itertools.tee(range(1, n+1), 2)))

list(matrix3(4))

def grid(min_val, max_val, step, *, num_dimensions=2):
    axis = itertools.takewhile(lambda x: x <= max_val,
                               itertools.count(min_val, step))
    
    # to handle multiple dimensions, we just need to repeat the axis that
    # many times - tee is perfect for that
    axes = itertools.tee(axis, num_dimensions)

    # and now we just need the product of all these iterables
    return itertools.product(*axes)

list(grid(-1, 1, 0.5))
list(grid(-1, 1, 0.5, num_dimensions=3))

sample = list(itertools.product(range(1, 7), range(1, 7)))
print(sample)

outcomes = list(filter(lambda x: x[0] + x[1] == 8, sample))
print(outcomes)

from fractions import Fraction
odds = Fraction(len(outcomes), len(sample))
print(odds)

list(itertools.permutations('abc'))

list(itertools.permutations('abc', 2))

list(itertools.combinations([1, 2, 3, 4], 2))

SUITS = 'SHDC'
RANKS = tuple(map(str, range(2, 11))) + tuple('JQKA')

from collections import namedtuple
Card = namedtuple('Card', 'rank suit')

deck = (Card(rank, suit) for suit, rank in itertools.product(SUITS, RANKS))
space = itertools.combinations(deck, 4)
total = 0
acceptable = 0
for outcome in space:
    total += 1
    for card in outcome:
        if card.rank != 'A':
            break
    else:
        # else block is executed if loop terminated without a break
        acceptable += 1
print(f'total={total}, acceptable={acceptable}')
print('odds={}'.format(Fraction(acceptable, total)))
print('odds={:.10f}'.format(acceptable/total))

print(all(['A', 'A', '10', 'J']))

