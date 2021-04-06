import numpy as np

def sieve(n):
  flags = np.ones(n, dtype = bool)
  flags[0] = flags[1] = False
  for i in range(2, n):
    if flags[i]:
      flags[i*i::i] = False
  return np.flatnonzero(flags)

def exponents(n):
  P = sieve(n)
  factors = []
  for p in P:
    k = n
    i = 0
    while k % p == 0:
      i += 1
      k = k // p
    factors.append(i)
  return [i for i in factors if i != 0]

def divisors(n):
  A = exponents(n)
  return np.prod([i + 1 for i in A])
