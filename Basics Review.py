#MULTI-LINE STATEMENTS AND STRINGS
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


#CONDITIONALS
num1 = int(input('Enter num1: '))
num2 = int(input('Enter num2: '))

def right():
    print('YES')

def wrong():
    print('NO')   

right() if num1 > num2 else wrong()


#FUNCTIONS
from cmath import sqrt
import math

s = [1,2,3,4,5,6,7,8,9]

def multiply(r, t):
    print(r*t)
    divide()

def divide():
    print(len(s)/sqrt(len(s)))

multiply(5,4)

#WHILE LOOPS
i = 0
while i <= 5:
    print(i)
    i += 1

length = 8

password = input('Enter a password: ')
while len(password) < length and password.capitalize() != password:
    password = input('Enter a password: ')

print('Accepted')

#fOR LOOPS
for i  in range(1,10):
    if i % 2 == 0:
        print(i)
        break
else:
       print('No multiples of 2')

#CLASSES
class Square:
    def __init__(self, side_length):
        self.side_length = side_length
    
    def area(self):
        print(self.side_length ** 2)
    
    def perimeter(self):
        print(self.side_length * 4)

square = Square(10)
square.area()
square.perimeter()


