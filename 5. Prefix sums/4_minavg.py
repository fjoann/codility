from statistics import mean

def solution(A):
    min_i = 0
    min_avg = 10001
 
    for i in range(len(A) - 1):
        avg_2 = mean(A[i:i+2])
        if avg_2 < min_avg:
            min_i = i
            min_avg = avg_2
        avg_3 = mean(A[i:i+3])
        if i < len(A) - 2 and avg_3 < min_avg:
            min_i = i
            min_avg = avg_3
 
    return min_i
