#POSITIONAL ARGUMENTS
#default values
def func(a, b= 1, c=2):
    print("a={0}, b={1}, c={2}".format(a, b, c))
func(10, 11, 12)
func(10,11)
func(10)

#UNPACKING ITERABLES
#tuples cannot have a single element - the comma makes the tuple. (1,2) = TUPLE (1) = NOT a TUPLE (1,) = TUPLE

def check_tuple(a):
    print(type(a))

check_tuple((1, 2, 3))
check_tuple([1, 2, 3])
check_tuple(1,)
check_tuple('')

l = [1,2,3,4]
def unpacking(l):
    a, b, c, d = l
    print(a, b, c, d)
    x, y, z = 'XYZ'
    print(x,y,z)

def unpacking2(a,b):
    print("a={0}, b={1}".format(a, b))
    a, b = b, a
    print("a={0}, b={1}".format(a, b))

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
for i in dict1:
    print(i)

#EXTENDED UNPACKING

def extend_unpack(l):
    a, b = l[0], l[1:]
    print(a, b)

def extend_unpack2(s):
    x, *y = s
    print(x,y)
    y = ''.join(y)
    print(y)

extend_unpack2('python')

def slicing(l):
    a, b, c, d, e = l[0], l[1:-1], l[-1][0], l[-1][1], list(l[-1][2:])
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

slicing([1,2,3,4,'python'])

d1 = {'key1': 1, 'key2': 2}
d2 = {'key2': 3, 'key3': 3}
print([*d1, *d2])
print({**d1, **d2})

def func1(a, b, *args):
    print(a)
    print(b)
    print(args)

func1(1, 2, 'a', 'b')

def average(a, *args):
    count = len(args) + 1
    total = a + sum(args)
    print(count, total)

average(2, 2, 4, 4)

#KEYWORD ARGUMENTS
def func2(a, b=20, *args, d=0, e='n/a'):
    print(a, b, args, d, e)
func2(0, 600, d=200, e='python')

def func3(*args, **kwargs):
    print(args)
    print(kwargs)
func3(1, 2, a=3, b=4)

def func4(*, d, **kwargs):
    print(d)
    print(kwargs)
func4(d=1, x=2, y=3)

def func5(a, b=2, *args, c=3, d):
    print(a, b, args, c, d)
func5(1, 2, 'a', 'b', 'c', c=3, d=4)

def calc(*args, log_to_console=False):
    high = int(bool(args)) and max(args)
    low = int(bool(args)) and min(args)
    average = (high + low)/2
    if log_to_console:
        print("high={0}, low={1}, avg={2}".format(high, low, average))
    return average
print(calc(1,2,3,4,5))

#FUNCTION TIMER
import time
def time_it(fn, *args, r=5, **kwargs):
    print(args, r, kwargs)
time_it(print, 1, 2, 3, sep='-')

def time_it2(fn, *args, r=5, **kwargs):
    start = time.perf_counter()
    for i in range(r):
        fn(*args, **kwargs)
    end = time.perf_counter()

def compute1(n, *, start=1, end):
    results = []
    for i in range(start, end):
        results.append(n**i)
    return results

def compute2(n, *, start=1, end):
    return (n**i for i in range(start, end))

time_it2(compute1, n=2, end=20000, r=4)
time_it2(compute2, n=2, end=20000, r=4)

from datetime import datetime
def log(message, *, date=datetime.utcnow()):
    print('{0}: {1}'.format(date, message))
log('Message one')

def log2(msg, *, date=None):
    date = date or datetime.utcnow()
    print('{0}: {1}'.format(date, msg))   
log2('message 3', date='2001-01-01 00:00:00')

store1 = []
store2 = []
def item(name, quantity, unit, grocery_list=None):
    if not grocery_list:
        grocery_list = []
    item_fmt = "{0} ({1} {2})".format(name, quantity, unit)
    grocery_list.append(item_fmt)
    return grocery_list

item('grapes', 1, 'bunch', store1)
item('Apples',5,'bunch',store2)

def factorial(n, cache={}):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print('{0}!'.format(n))
        result = n * factorial(n-1)
        cache[n] = result
        return result

print(factorial(3))





