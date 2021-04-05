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
    """Calculate the number of eaten chocolates.
    
    N -- the number of chocolates in the circle
    M -- the number of steps between each eaten chocolate
    
    N and M 'meet' at their lcm; it is the total number of steps taken.
    """
    return lcm(N, M) // M
