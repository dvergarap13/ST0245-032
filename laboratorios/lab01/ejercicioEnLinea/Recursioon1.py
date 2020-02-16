def factorial(n):
    if n<=1:
        return 1

    return n*factorial(n-1)

def bunnyears(n):
    if n==0:
        return 0
    return 2+bunnyears(n-1)

def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

def bunnyears2(n):
    if n==0:
        return 0
    if n%2==0:
        return 3 + bunnyears2(n-1)
    return 2+bunnyears2(n-1)

def triangle(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return n+triangle(n-1)

print(factorial(0))