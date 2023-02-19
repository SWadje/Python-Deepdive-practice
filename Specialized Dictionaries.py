from collections import defaultdict
counts = {}
sentence = "Hello World"

for c in sentence:
    if c in counts:
        counts[c] += 1
    else:
        counts[c] = 1

persons = {
    'john': {'age': 20, 'eye_color': 'blue'},
    'jack': {'age': 25, 'eye_color': 'brown'},
    'jill': {'age': 22, 'eye_color': 'blue'},
    'eric': {'age': 35},
    'michael': {'age': 27}
}

eye_colors = {}
for person, details in persons.items():
    if 'eye_color' in details:
        color = details['eye_color']
    else:
        color = 'unknown'
    if color in eye_colors:
        eye_colors[color].append(person)
    else:
        eye_colors[color] = [person]

print(eye_colors)

eye_colors2 = defaultdict(list)
for person, details in persons.items():
    color = details.get('eye_color', 'Unknown')
    eye_colors[color].append(person)

print(eye_colors2)

persons2 = {
    'john': defaultdict(lambda: 'unknown', 
                        age=20, eye_color='blue'),
    'jack': defaultdict(lambda: 'unknown',
                        age=20, eye_color='brown'),
    'jill': defaultdict(lambda: 'unknown',
                        age=22, eye_color='blue'),
    'eric': defaultdict(lambda: 'unknown', age=35),
    'michael': defaultdict(lambda: 'unknown', age=27)
}

print(persons2)

from collections import defaultdict, namedtuple
from datetime import datetime
from functools import wraps

def function_stats():
    d = defaultdict(lambda: {"count": 0, "first_called": datetime.utcnow()})
    Stats = namedtuple('Stats', 'decorator data')
    
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            d[fn.__name__]['count'] += 1
            return fn(*args, **kwargs)
        return wrapper
    
    return Stats(decorator, d)       

stats = function_stats()
dict(stats.data)
@stats.decorator
def func_1():
    pass

@stats.decorator
def func_2(x, y):
    pass

from collections import OrderedDict
d = OrderedDict()

for key in d:
    print(key)

d1 = OrderedDict()
d1['a'] = 10
d1['b'] = 20

d2 = OrderedDict()
d2['a'] = 10
d2['b'] = 20

d3 = OrderedDict()
d3['b'] = 20
d3['a'] = 10


print(d1)
print(d2)
print(d3)

from timeit import timeit
from collections import deque

def create_ordereddict(n=100):
    d = OrderedDict()
    for i in range(n):
        d[str(i)] = i
    return d

def create_deque(n=100):
    return deque(range(n))   


def pop_all_ordered_dict(n=1000, last=True):
    d = create_ordereddict(n)
    while True:
        try:
            d.popitem(last=last)
        except KeyError:
            break           

def pop_all_deque(n=1000, last=True):
    dq = create_deque(n)
    if last:
        pop = dq.pop
    else:
        pop = dq.popleft

    while True:
        try:
            pop()
        except IndexError:
            break

timeit('create_ordereddict(10_000)', 
       globals=globals(), 
       number=1_000)

n = 10_000
number = 1_000

results = dict()

results['dict_create'] = timeit('create_ordereddict(n)', 
                                globals=globals(), 
                                number=number)

results['deque_create'] = timeit('create_deque(n)', 
                                 globals=globals(), 
                                 number=number)

results['dict_create_pop_last'] = timeit(
    'pop_all_ordered_dict(n, last=True)',
    globals=globals(), number=number)

results['dict_create_pop_first'] = timeit(
    'pop_all_ordered_dict(n, last=False)',
    globals=globals(), number=number)

results['deque_create_pop_last'] = timeit(
    'pop_all_deque(n, last=True)',
    globals=globals(), number=number
)

results['deque_create_pop_first'] = timeit(
    'pop_all_deque(n, last=False)',
    globals=globals(), number=number
)

results['dict_pop_last'] = (
    results['dict_create_pop_last'] - results['dict_create'])

results['dict_pop_first'] = (
    results['dict_create_pop_first'] - results['dict_create'])

results['deque_pop_last'] = (
    results['deque_create_pop_last'] - results['deque_create'])

results['deque_pop_first'] = (
    results['deque_create_pop_first'] - results['deque_create'])

for key, result in results.items():
    print(f'{key}: {result}')

from collections import defaultdict, Counter

sentence = 'Hello World'
counter = defaultdict(int)
for c in sentence:
    counter[c] += 1
    print(counter)

import random
random.seed(0)
my_list = [random.randint(0, 10) for _ in range(1_000)]
c2 = Counter(my_list)
print(c2)

class RepeatIterable:
    def __init__(self, **kwargs):
        self.d = kwargs
        
    def __setitem__(self, key, value):
        self.d[key] = value
        
    def __getitem__(self, key):
        self.d[key] = self.d.get(key, 0)
        return self.d[key]
    
    def elements(self):
        for k, frequency in self.d.items():
            for i in range(frequency):
                yield k

r = RepeatIterable(x=10, y=20)

for e in r.elements():
    print(e, end=', ')
