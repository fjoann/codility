def solution(A):
    min_diff = abs(sum(A[:1]) - sum(A[1:]))
    for i in range(1, len(A) - 1):
        diff = abs(sum(A[:i + 1]) - sum(A[i + 1:]))
        if diff < min_diff:
            min_diff = diff
    return min_diff
