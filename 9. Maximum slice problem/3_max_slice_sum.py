# Kadane's algorithm for the maximum subarray problem

def solution(A):
    best_sum = current_sum = 0
    for a in A:
        current_sum = max(0, current_sum + a)
        best_sum = max(best_sum, current_sum)
    return best_sum
