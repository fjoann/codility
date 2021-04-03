def prefix_sum(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P

def solution(A):
    pref = prefix_sum(A)
    min_mean = 10000
    min_i = 0
    for i in range(len(A)):
        for j in range(i + 1, min(i + 3,len(A))):
            mean = (pref[j + 1] - pref[i]) / (j - i + 1)
            if mean < min_mean:
                min_mean = mean
                min_i = i
    return min_i
