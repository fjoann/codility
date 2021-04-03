# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from statistics import mean

def solution(A):
    min_avg = mean(A[0:1])
    min_idx = 0
    for i in range(len(A) - 2):
        avg_2 = mean(A[i:i+1])
        avg_3 = mean(A[i:i+2])
        if avg_2 < min_avg:
            min_avg = avg_2
            min_idx = i
        if avg_3 <
