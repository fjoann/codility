def valid_size(K, A, mid):
    sum = 0
    blocks = 0
 
    for element in A:
        if sum + element > mid:
            sum = element
            blocks += 1
        else:
            sum += element
        if blocks >= K:
            return False
 
    return True
 
def solution(K, M, A):
    """Perform a binary search."""
    start = max(A)
    end = sum(A)
 
    if K == 1:
        return end
    if K >= len(A):
        return start
 
    while start <= end:
        mid = (start + end) // 2
        if valid_size(K, A, mid):
            end = mid - 1
        else:
            start = mid + 1
 
    return start
