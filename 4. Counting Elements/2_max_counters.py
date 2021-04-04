def solution(N, A):
    C = [0] * N
    for i in A:
        if i > N:
            C = [max(C)] * len(C)
        else:
            C[i - 1] += 1
    return C
