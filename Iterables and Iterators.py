s = {'x', 'y', 'b', 'c', 'a'}
for item in s:
    print(item)

class Squares:
    def __init__(self, length):
        self.length = length
        self.i = 0
    
    def next_(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result           
        
    def __len__(self):
        return self.length

sq = Squares(5)
while True:
    try:
        print(sq.next_())
    except StopIteration:
        break   

print([item for item in sq if item%2==0])
print(list(enumerate(sq)))
print(sorted(sq, reverse=True))


import random  

class RandomNumbers:
    def __init__(self, length, *, range_min=0, range_max=10):
        self.length = length
        self.range_min = range_min
        self.range_max = range_max
        self.num_requested = 0
        
    def __len__(self):
        return self.length
    
    def __next__(self):
        if self.num_requested >= self.length:
            raise StopIteration
        else:
            self.num_requested += 1
            return random.randint(self.range_min, self.range_max)

numbers = RandomNumbers(10)
while True:
    try:
        print(next(numbers))
    except StopIteration:
        break

class Cities:
    def __init__(self):
        self._cities = ['New York', 'Newark', 'New Delhi', 'Newcastle']
        
    def __len__(self):
        return len(self._cities)
    
    def __iter__(self):
        print('Calling Cities instance __iter__')
        return self.CityIterator(self)
    
class CityIterator:
    def __init__(self, city_obj):
        print('Calling CityIterator __init__')
        self._city_obj = city_obj
        self._index = 0

    def __iter__(self):
        print('Calling CitiyIterator instance __iter__')
        return self

    def __next__(self):
        print('Calling __next__')
        if self._index >= len(self._city_obj):
            raise StopIteration
        else:
            item = self._city_obj._cities[self._index]
            self._index += 1
            return item
        
cities = Cities()
print(list(enumerate(cities)))
print([item.upper() for item in cities])
print(sorted(cities))

iter_1 = CityIterator(cities)
for city in iter_1:
    print(city)

import math
class Circle:
    def __init__(self, r):
        self.radius = r
        
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, r):
        self._radius = r
        self._area = None

    @property
    def area(self):
        if self._area is None:
            print('Calculating area...')
            self._area = math.pi * self.radius ** 2
        return self._area


c = Circle(1)
print(c.area, c.radius)

class Factorials:
    def __init__(self, length):
        self.length = length
    
    def __iter__(self):
        return self.FactIter(self.length)
    
    class FactIter:
        def __init__(self, length):
            self.length = length
            self.i = 0
            
        def __iter__(self):
            return self
        
        def __next__(self):
            if self.i >= self.length:
                raise StopIteration
            else:
                result = math.factorial(self.i)
                self.i += 1
                return result

factorials = Factorials()
fact_iter = iter(factorials)
for _ in range(10):
    print(next(fact_iter))

random.seed(0)
for i in range(10):
    print(random.randint(1, 10))

class RandomInts:
    def __init__(self, length, *, seed=0, lower=0, upper=10):
        self.length = length
        self.seed = seed
        self.lower = lower
        self.upper = upper
        
    def __len__(self):
        return self.length
    
    def __iter__(self):
        return self.RandomIterator(self.length, 
                                   seed = self.seed, 
                                   lower = self.lower,
                                   upper=self.upper)

class RandomIterator:
    def __init__(self, length, *, seed, lower, upper):
        self.length = length
        self.lower = lower
        self.upper = upper
        self.num_requests = 0
        random.seed(seed)
            
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.num_requests >= self.length:
            raise StopIteration
        else:
            result = random.randint(self.lower, self.upper)
            self.num_requests += 1
            return result

randoms = RandomInts(10)
for num in randoms:
    print(num)


