def solution(A):
    sum_array = sum(A)
    sum_full = sum(range(1, len(A) + 2))
    missing = sum_full - sum_array
    return missing
