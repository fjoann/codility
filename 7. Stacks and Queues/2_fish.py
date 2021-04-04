def solution(A, B):
    stack = []
    alive = len(A)
    for fish in zip(A, B):
        size, downstream = fish
        if not downstream:
            while stack and stack[-1] < size:
                alive -= 1
                stack.pop()
            if stack:
                alive -= 1
        else:
            stack.append(size)
    return alive
