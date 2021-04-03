def solution(S):
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    stack = []
    for s in S:
        if s in brackets:
            stack.append(s)
        else:
            if len(stack) == 0:
                return 0
            if not ((stack.pop(), s) in brackets.items()):
                return 0
    if len(stack) != 0:
        return 0
    return 1
