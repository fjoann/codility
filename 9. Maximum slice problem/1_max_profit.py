# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import math

def max_subarray(A):
    """Kadane's algorithm for the maximum subarray problem."""
    best_sum = -math.inf
    current_sum = 0
    for a in A:
        current_sum = max(a, current_sum + a)
        best_sum = max(best_sum, current_sum)
    return best_sum

def solution(A):
    if len(A) in [0, 1]:
        return 0
    P = [0] * len(A)
    for i in range(1, len(A)):
        P[i] = A[i] - A[i - 1]
    return max_subarray(P)
