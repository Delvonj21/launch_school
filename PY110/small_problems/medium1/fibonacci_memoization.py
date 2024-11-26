# For this exercise, your objective is to refactor the recursive fibonacci function to use memoization.


mem = {}


def fibonacci(n):
    if n <= 2:
        return 1
    elif n in mem:
        return mem[n]
    else:
        mem[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return mem[n]
