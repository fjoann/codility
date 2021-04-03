def prefix_sum(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P

def solution(A):
    pref = prefix_sum(A)
    n = len(pref)
    passing = 0
    for i in range(len(A)):
        if A[i] == 0:
            passing += pref[n - 1] - pref[i + 1]
    return passing
