try:
    10 / 2
except ZeroDivisionError:
    print('Error')
finally:
    print('finally ran!')  

try:
    1 / 0
except ZeroDivisionError:
    print('Error')
finally:
    print('finally ran!')


class MyContext:
    def __init__(self):
        self.obj = None
        
    def __enter__(self):
        print('entering context...')
        self.obj = 'the Return Object'
        return self.obj

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exiting context...')
        if exc_type:
            print(f'*** Error occurred: {exc_type}, {exc_value}')
        return True 


with MyContext() as obj:
    print('running inside with block...')
    print(obj)
print(obj)

class Resource:
    def __init__(self, name):
        self.name = name
        self.state = None

class ResourceManager:
    def __init__(self, name):
        self.name = name
        self.resource = None
        
    def __enter__(self):
        print('entering context')
        self.resource = Resource(self.name)
        self.resource.state = 'created'
        return self.resource
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exiting context')
        self.resource.state = 'destroyed'
        if exc_type:
            print('error occurred')
        return False

with ResourceManager('spam') as res:
    print(f'{res.name} = {res.state}')
print(f'{res.name} = {res.state}')


class DataIterator:
    def __init__(self, fname):
        self._fname = fname
        self._f = None
    
    def __iter__(self):
        return self
    
    def __next__(self):
        row = next(self._f)
        return row.strip('\n').split(',')
    
    def __enter__(self):
        self._f = open(self._fname)
        return self
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        if not self._f.closed:
            self._f.close()
        return False

with DataIterator('Level1_Coins.csv') as data:
    for row in data:
        print(row)

import decimal

decimal.getcontext()


class prec:
    def __init__(self, prec):
        self.prec = prec
        self.current_prec = decimal.getcontext().prec
        
    def __enter__(self):
        decimal.getcontext().prec = self.prec
        
    def __exit__(self, exc_type, exc_value, exc_traceback):
        decimal.getcontext().prec = self.current_prec
        return False      
        
with prec(3):
    print(decimal.Decimal(1) / decimal.Decimal(3))
print(decimal.Decimal(1) / decimal.Decimal(3))   

from time import perf_counter, sleep

class Timer:
    def __init__(self):
        self.elapsed = 0
        
    def __enter__(self):
        self.start = perf_counter()
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.stop = perf_counter()
        self.elapsed = self.stop - self.start
        return False
    
with Timer() as timer:
    sleep(1)
print(timer.elapsed)

import sys

class OutToFile:
    def __init__(self, fname):
        self._fname = fname
        self._current_stdout = sys.stdout
        
    def __enter__(self):
        self._file = open(self._fname, 'w')
        sys.stdout = self._file
        
    def __exit__(self, exc_type, exc_value, exc_tb):
        sys.stdout = self._current_stdout
        if self._file:
            self._file.close()
        return False

with OutToFile('Essay.txt'):
    print('Line 1')
    print('Line 2')

