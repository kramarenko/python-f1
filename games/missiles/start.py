import random
from random import randint
from math import *

print(randint(1, 110))
print(factorial(5))
print(random.random())

print(type("test"))
print(type(12))
print(type(1.3))

exList = [1, 5, 8, 9]


def list_modifier(li):
    return li[2] / 0.5


print(list_modifier(exList))

inList = ["jump", "leap", "hop"]


def one_li(list_val):
    print(list_val[1])
    print(list_val[2] + "frog")
    list_val.remove(list_val[0])
    print(list_val)


one_li(inList)

var3 = range(1, 20, 3)
for x in var3:
    print(x, end='\n')

ex3 = [num3 for num3 in range(1, 21, 4) if num3 > 7]
print(ex3)

exList2 = [1, 2, 3, 4, 5, 6, 7]
reversedList = exList2[::-2]
print(reversedList)

stringText = "Create fun social quizzes"
print(stringText[42::-1])

print(bytearray([1, 4, 5]))
print(800//10)
