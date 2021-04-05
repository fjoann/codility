def gcd(a, b):
    """Calculate the greatest common divisor."""
    if (a % b == 0):
        return b
    else:
        return gcd(b, a % b)

def lcm(a, b):
    """Calculate the least common multiple."""
    return (a * b) // gcd(a, b)

def solution(N, M):
    return lcm(N, M) // M
