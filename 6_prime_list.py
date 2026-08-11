# Implement prime_list(n). 
# Return a list of all prime numbers from 2 to n inclusive. 
# A prime number has exactly two positive divisors. 
# Students may need to research a simple primality test or the Sieve of Eratosthenes.

def prime_list(n):
    primes = []

    for i in range(2, n+1):
        if i == 2:
            primes.append(i)
            continue
        # Set prime to True at the start of every outer iteration, so a False from a previous i (like 4) --
        # -- does not incorrectly carry over and block later primes (like 5) that never had a reason to fail.
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
        if prime:
            primes.append(i)
    
    return primes