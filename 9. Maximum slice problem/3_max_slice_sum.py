import math

def solution(A):
    """Kadane's algorithm for the maximum subarray problem."""
    best_sum = -math.inf
    current_sum = 0
    for a in A:
        current_sum = max(a, current_sum + a)
        best_sum = max(best_sum, current_sum)
    return best_sum
