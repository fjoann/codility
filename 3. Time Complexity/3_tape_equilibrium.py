def solution(A):
    total = sum(A)
    min_diff = float('inf')
    left = right = 0
    for i in A[:-1]:
        left += i
        right = total - left
        min_diff = min(
            abs(right - left), min_diff
        )
    return min_diff
