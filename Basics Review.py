#Multi-line statements and strings

x = """The answer is \n
yes"""
y = """The answer is \n
no"""

def func(a,
        b, c):
    if a > b \
        and a > c:
        print(x)
    else:
        print(y)

func(6,
    5,
    4)


#Conditionals

num1 = int(input('Enter num1: '))
num2 = int(input('Enter num2: '))

def right():
    print('YES')

def wrong():
    print('NO')   

right() if num1 > num2 else wrong()


#functions
from cmath import sqrt
import math

s = [1,2,3,4,5,6,7,8,9]

def multiply(r, t):
    print(r*t)
    divide()

def divide():
    print(len(s)/sqrt(len(s)))

multiply(5,4)
