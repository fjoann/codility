def solution(S):
    s = []
    if not S:
        return 0
    if S[0] == ')':
        return 1
    for p in S:
        if p == '(':
            s.append(p)
        elif s:
            s.pop()
        else: return 0
    if not s:
        return 1
    return 0
