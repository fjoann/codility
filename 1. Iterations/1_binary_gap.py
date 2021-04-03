def solution(N):
    bin = format(N, 'b')
    strip = bin.strip('0')
    split = strip.split('1')
    longest = len(max(split))
    return longest
