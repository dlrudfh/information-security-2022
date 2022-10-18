# BigNumber, mpmath package required
# run this before execute: pip install BigNumber mpmath

import random
from BigNumber import BigNumber
import math

# https://www.delftstack.com/howto/python/python-generate-prime-number/
def primesInRange(x, y):
    prime_list = []
    for n in range(x, y):
        isPrime = True

        for num in range(2, n):
            if n % num == 0:
                isPrime = False

        if isPrime:
            prime_list.append(n)
            
    return prime_list

def make_keys(p: BigNumber, q: BigNumber):
    # place your own implementation of make_keys
    # use e = 65537 as if FIPS standard
    n = p*q
    l = math.lcm(p-1, q-1)
    e = 65537
    d = 2
    '''
    for i in range(2, l):
        if math.gcd(i, l) == 1:
            e = i
            break
    '''
    for i in range(2, l):
        if e*i%l == 1:
            d = i
            break
    print(e)
    print(l)
    return [e, d, n]

def rsa_encrypt(plain: BigNumber, e: BigNumber, n: BigNumber):
    return (plain**e)%n

def rsa_decrypt(cipher: BigNumber, d: BigNumber, n: BigNumber):
    return (cipher**d)%n

primes = primesInRange(100, 1000)
P = primes[random.randrange(0, len(primes))]
Q = primes[random.randrange(0, len(primes))]

while P == Q:
    P = primes[random.randrange(0, len(primes))]
    Q = primes[random.randrange(0, len(primes))]

M = random.randrange(2, 20)
e, d, N = make_keys(P, Q)
C = rsa_encrypt(M, e, N)
M2 = rsa_decrypt(C, d, N)

print(f"P = {P}, Q = {Q}, N = {N}, M = {M}, e = {e}, d = {d}, C = {C}, M2 = {M2}")

if M == M2:
    print("RSA Success!!")
else:
    print("RSA Failed...")
