from math import sqrt

def solution(N):
    d = {1, N}
    for i in range(2, int(sqrt(N)) + 1):
        if N % i == 0:
            d.update((i, N // i))
    return len(d)
