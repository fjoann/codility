import math

def fib(n):
    a = b = 1
    yield 1
    while a + b <= n:
        yield a + b
        a, b = b, a + b

def solution(A):
    n = len(A) + 1
    pos = [math.inf] * (n + 1)
    pos[0] = 0
    
    for i in range(1, n + 1):
        if (i < n and A[i - 1] == 1) or (i == n):
            pos[i] = min([pos[i - x] + 1 for x in fib(i)])

    if pos[-1] < math.inf:
        return pos[-1]
    else:
        return -1
