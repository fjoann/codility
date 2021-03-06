import numpy as np

def sieve(n):
    flags = np.ones(n, dtype = bool)
    flags[0] = False
    if n > 1:
        flags[1] = False
    for i in range(2, n):
      if flags[i]:
        flags[i*i::i] = False
    return np.flatnonzero(flags)
