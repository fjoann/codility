def solution(A):
    if len(A) == 0:
        return -1
    if len(A) == 1:
        return 0
    
    # Boyer-Moore majority vote algorithm
    count = 0
    for i in A:
        if count == 0:
            candidate = i
            count += 1
        elif i == candidate:
            count += 1
        else:
            count -= 1
    if A.count(candidate) > len(A) // 2:
        return A.index(candidate)
    else:
        return -1
