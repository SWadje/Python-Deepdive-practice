a = {('a', 100): ['a', 'b', 'c'], 'key2': {'a': 100, 'b': 200}}
hash((1, 2, 3))

def function(a, b, c):
    print(a, b, c)

hash(function)

def fn_add(a, b):
    return a + b

def fn_inv(a):
    return 1/a

def fn_mult(a, b):
    return a * b

functions = {fn_add: (10, 20), fn_inv: (2,), fn_mult: (2, 8)}
for f in functions:
    print(f)

for f in functions:
    result = f(*functions[f])
    print(result)

d = {'a': 100, 'b': 200, 'c': {'d': 1, 'e': 2}}
print(d)
print(id(d))

keys = ['a', 'b', 'c']
values = (1, 2, 3)

dict = {}  
for k, v in zip(keys, values):
    dict[k] = v

x_coords = (-2, -1, 0, 1, 2)
y_coords = (-2, -1, 0, 1, 2)

grid = [(x, y) 
         for x in x_coords 
         for y in y_coords]
print(grid)

import math
math.hypot(1, 1)
grid_extended = [(x, y, math.hypot(x, y)) for x, y in grid]
print(grid_extended)

counters = dict.fromkeys(['a', 'b', 'c'], 0)
print(counters)

dict2 = dict(zip('abc', range(1, 4)))
len(dict2)

result = d.get('python')
print(result)

text = 'Historical objects have the potential to portray critical narratives.'
counts = dict()
for c in text:
    counts[c] = counts.get(c, 0) + 1
print(counts)

counts = dict()
for c in text:
    key = c.lower().strip()
    if key:
        counts[key] = counts.get(key, 0) + 1
print(counts)

result1 = d.pop('z', 'Not found!')
print(result1)

def insert_if_not_present(d, key, value):
    if key not in d:
        d[key] = value
        return value
    else:
        return d[key]

result2 = insert_if_not_present(d, 'a', 0)
print(result2, d)

d1 = {'a': 1, 'b': 2, 'c': 3}
result = d1.setdefault('a', 0)
print(result)
print(d1)

import string
print(string.ascii_lowercase)
print(string.ascii_uppercase)

categories = {}
for c in text:
    if c != ' ':
        if c in string.ascii_lowercase:
            key = 'lower'
        elif c in string.ascii_uppercase:
            key = 'upper'
        else:
            key = 'other'
        if key not in categories:
            categories[key] = set()  
        
        categories[key].add(c)
for cat in categories:
    print(f'{cat}:', ''.join(categories[cat]))


def cat_key(c):
    categories = {' ': None,
                 string.ascii_lowercase: 'lower',
                 string.ascii_uppercase: 'upper'}
    for key in categories:
        if c in key:
            return categories[key]
    else:
        return 'other'

cat_key('a'), cat_key('A'), cat_key('!'), cat_key(' ')

categories = {}
for c in text:
    key = cat_key(c)
    if key:
        categories.setdefault(key, set()).add(c)

for cat in categories:
    print(f'{cat}:', ''.join(categories[cat]))

    

