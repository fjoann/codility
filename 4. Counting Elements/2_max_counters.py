def solution(N, A):
    C = [0] * N
    max_val = 0
    last_max = False
    for i in A:
        if i == N + 1 and not last_max:
            C = [max_val] * N
            last_max = True
            continue
        if i <= N:
            C[i - 1] += 1
            max_val = max(max_val, C[i - 1])
            last_max = False
    return C
