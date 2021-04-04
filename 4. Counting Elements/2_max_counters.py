def solution(N, A):
    C = [0] * N
    max_val = 0
    for i in A:
        if i == N + 1:
            max_val = max(C)
        else:
            C[i - 1] = max(C[i - 1] + 1, max_val + 1)
    for i in range(len(C)):
        C[i] = max(C[i], max_val)
    return C
