import functools as ft
import random
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def f(cal, a, b):
    return cal(a, b)

def newf(a,b):
    return a*b+b


if __name__=='__main__':
    add=lambda x,y:1 if x>y else 'a'
    lst=range(10)
    b=map(lambda x:x+1,filter(lambda x:x>5,lst))
    print(list(b))
    randintx=random.randint(-50,50)
    print(c)


