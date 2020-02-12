#!/usr/bin/pytho

import random
from time import time
import sys

sys.setrecursionlimit(1000000000)


def array_generator(len):
    """List generator"""
    A = []
    for i in range(len):
        A.append(random.randrange(100000))
    return A


def arrayMax(arr, indice, max):
    if indice == len(arr):
        return max
    elif arr[indice] > max:
        return arrayMax(arr, indice + 1, arr[indice])
    else:
        return arrayMax(arr, indice + 1, max)



def array_sum(array, start , target):
    """Add the elements in the list"""
    if start>=len(array):
        return target==0
    for i in range(len(array)):
        return array_sum(array,start +1, target-array[start]) or array_sum(array,start +1, target)




def fib_r(n):      
    if n==0:
        return 0
    if n==1:
        return 1
    return fib_r(n-1)+fib_r(n-2)



for i in range(100, 2000,100):
    tiempoinicial = time()
    arrayMax(array_generator(i), 0, 0)
    tiempofinal = time()
    print(tiempofinal - tiempoinicial)

for i in range(5,25):
    tiempoinicial = time()
    array_sum(array_generator(i), 0, 10000000)
    tiempofinal = time()
    print(tiempofinal - tiempoinicial)

