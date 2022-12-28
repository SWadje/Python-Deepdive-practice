#DATA TYPES
import sys
print(sys.getsizeof(0)) #the number of bytes needed to store the value of 0
print(sys.getsizeof(2*10))
print(sys.getsizeof(2**100))

import time
def func(x):
    x*2

def func2(y):
    y**100

start = time.perf_counter()
func(10)
end = time.perf_counter()
print(end - start)

start = time.perf_counter()
func2(2)
end = time.perf_counter()
print(end - start)

#OPERATIONS
print(type(10/2)) #always returns the value as a float
print(type(10/3))

import math
#for non-negatives math.floor will always return the integer part of the number
print(math.floor(3.1415))
print(math.floor(3.9999))
#for negatives math.floor will return the nearest smallest number
print(math.floor(-3.89))
print(math.floor(-3.0001))
#a//b is the same as math.floor(a/b) becuase floor rounds the answer
print(10/3)
print(10//3)
print(math.floor(10/3))

print(-10/3)
print(-10//3)
print(math.floor(-10/3))

#the modulo operator and floor division operator both follow this rule: a = b * (a//b) + a%b
def mod_operator(a,b):
    print('{0}/{1} = {2}'.format(a,b,a/b))
    print('{0}//{1} = {2}'.format(a,b,a//b))
    print('{0}%{1} = {2}'.format(a,b,a%b))
    print(a == b * (a//b) + a%b)

mod_operator(10,2)
mod_operator(12,-4)
mod_operator(-20,-10)

#CONSTRUCTORS AND BASES
from fractions import Fraction
print(int(Fraction(15/2)))
print(int('1010',2))#using binary
print(int('F1A',16))#using hexadecimal
print(0b1010)#using binary
print(0xf1a)#using hexadecimal
# 0x for hexadecimal, 0b for binary and 0o for octal

def base10(a, b):
    if b < 2:
        raise ValueError('Base b must be >= 2')#this displays syntax
    if a < 0:
        print('Number n must be >= 0')
    if a == 0:
        return [0]
    list = []
    while a > 0:
        a, m = divmod(a,b)
        list.insert(0, m)
    return list

print(base10(10, 2))
print(base10(-10,2))


def encode(x, y):
    if max(x) >= len(y):
        raise ValueError("digit_map is not long enough to encode digits")
    encoding = ''.join([y[d] for d in x])
    return encoding

print(encode([1, 0, 1], 'FT'))

def rebase10(n, b):
    digit_map = '0123456789ABCDEFG'
    if b < 2 or b > 16:
        raise ValueError('Invalid base: 2 <= base <= 16')
    if n < 0:
        sign = -1
    else:
        sign = 1
    n *= sign
    digits = base10(n, b)
    encoding = encode(digits, digit_map)
    if sign == -1:
        encoding = '-' + encoding
    return encoding

print(rebase10(10,2))

#INTERNAL REPRESENTATION - FLOATS
print(float(Fraction(15/2)))
print(format(0.1, '.25f')) # to 25 decimal figures
print(format(0.125, '.25f'))

#EQUALITY TESTING - FLOATS
#0.1 does not equal to a complete fraction.
x = 0.1 + 0.1 + 0.1
y = 0.3
if x == y:
    print(True)
if round(x, 5) == round(y, 5):
    print(True)

from math import isclose
print(isclose(x,y))

#FLOATS - ROUNDING
a = round(4.5)
print(a, type(a))
print(round(2.8888, 3))#number to round and decimal places
print(round(-2.8888, 2))
print(round(3.45, 1))

def Round(x):
    from math import copysign
    return int(x + 0.5 * copysign(1, x))
Round(3.45)

import decimal
from decimal import Decimal

global_context  = decimal.getcontext()
print(global_context.prec) #precision
print(global_context.rounding)
#change by assigning values to the variable
global_context.prec = 7
#local
with decimal.localcontext() as context:
    print(context.prec)
    print(context.rounding)

decimal.getcontext().rounding = decimal.ROUND_HALF_EVEN
num1 = Decimal('3.75')
num2 = Decimal('8.65')
print(round(num1, 1))
print(round(num2, 1))

decimal.getcontext().rounding = decimal.ROUND_HALF_UP
num_1 = Decimal('3.75')
num_2 = Decimal('8.65')
print(round(num_1, 1))
print(round(num_2, 1))

#CONSTRUCTORS AND CONTEXTS
decimal.getcontext().prec = 2
print(Decimal('1.2345')+Decimal('1.2345'))

#MATH OPERATIONS
def ops(a, b):
    print(a//b, a%b)
    print(divmod(a, b))
    print( a == b * (a//b) + a % b)

ops(11, 4)
ops(Decimal(11),Decimal(4))
ops(-11,4)
ops(Decimal(-11),Decimal(4))

def more_ops(a):
    print(a.log10())# base 10 logarithm
    print(a.ln())# natural logarithm 
    print(a.exp())# e**a
    print(a.sqrt())# square root

more_ops(Decimal(1.5))

print(format(math.sqrt(0.01), '1.27f'))
print(format(math.sqrt(Decimal('0.01')), '1.27f'))
print(Decimal('0.01').sqrt())

#DECIMALS - PERFORMANCE
print(sys.getsizeof(1.2345))
print(sys.getsizeof(Decimal('1.2345')))

import time
def float(n=1):
    for i in range(n):
        a = 1.2345

start = time.perf_counter()
float(10000000)
end = time.perf_counter()
print('float: ', end-start)

def _decimal(n=1):
    for i in range(n):
        a = Decimal('1.2345')

start = time.perf_counter()
_decimal(10000000)
end = time.perf_counter()
print('Decimal: ', end-start)

def float2(n=1):
    a = 1.2345
    for i in range(n):
        a + a

start = time.perf_counter()
float2(10000000)
end = time.perf_counter()
print('float: ', end-start)

def _decimal2(n=1):
    a = Decimal('1.2345')
    for i in range(n):
        a + a

start = time.perf_counter()
_decimal2(10000000)
end = time.perf_counter()
print('Decimal: ', end-start)

def float3(n=1):
    a = 1.2345
    for i in range(n):
        math.sqrt(a)

start = time.perf_counter()
float3(10000000)
end = time.perf_counter()
print('float: ', end-start)

def _decimal3(n=1):
    a = Decimal('1.2345')
    for i in range(n):
        math.sqrt(a)

start = time.perf_counter()
_decimal3(10000000)
end = time.perf_counter()
print('Decimal: ', end-start)

#COMPLEX NUMBERS
import cmath
print(complex(1, 2) -- 1 + 2j)

def complex_maths():
    a = 1 + 2j
    b = 3 - 4j
    c = 5j
    d = 6
    print(a+b)
    print(b*c)
    print(c/d)
    print(d-a)
    print(cmath.sqrt(a))
    #div and mod don't work for complex numbers
    print('{0} = ({1},{2})'.format(a, abs(a), cmath.phase(a))) #abs returns the magnitude of the complex number 
    print(cmath.rect(math.sqrt(2), cmath.pi/4)) # rect turns the number back into complex
    print(cmath.exp(cmath.pi * 1j) + 1)

complex_maths()
#comparisons such as >,<etc don't work for complex numbers

#BOOLEANS
print(issubclass(bool, int))

print('0: ' ,bool(0))
print('1: ' ,bool(1))
print('-1: ' ,bool(-1))
#booleans are subclassed as integers so can behave as integers
print('True  > False: ',True > False)
print('True + 2: ',True + 2)
print('False // 2: ',False // 2)
print('True + True + True: ',True + True + True)

#BOOLEANS - TRUTH VALUES
#any non-zero numeric values are true. Any versions of 0 are false
#empty objects are false non-empty are true
#None is always false

def booleans(a):
    if a:
        print(a[0])
    else:
        print('a is false, or a is empty')

booleans('abc')
booleans([])
booleans([1,2,3])
booleans('')

#PRECEDENCE AND SHORT-CUTTING
import string
help(string)
print('Digits: ', string.digits)
print('ASCII: ', string.ascii_letters)

def check(name):
    if name and name[0] in string.digits:
        print('Name cant start with digit')

check('')
check('Bob')
check('1Steve')

#BOOLEAN OPERATORS
def And(s):
    print(s and s[0])
    print((s and s[0]) or '')
    print((s and s[0]) or 'n/a')

And(None)
And('')
And('abc')

#COMPARISON OPERATORS
print(1 in [1, 2, 3])
print([1, 2] in [1, 2, 3])
print(Decimal('0.1') == Fraction(1, 10))
#in chaain comparisons such as a<b<c python makes changes itself tp a<b and b<c
