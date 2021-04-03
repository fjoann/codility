def solution(A):
    A.sort()
    last_three = A[-3] * A[-2] * A[-1]
    negative = A[0] * A[1] * A[-1]
    return max(last_three, negative)
