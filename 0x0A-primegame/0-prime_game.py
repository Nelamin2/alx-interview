#!/usr/bin/python3
"""Module for Prime Game""

def isWinner(x, nums):
    max_n = max(nums)
    
    # Precompute primes up to max_n using a sieve
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i]:
            for multiple in range(i * i, max_n + 1, i):
                sieve[multiple] = False

    # Precompute the number of primes up to each number <= max_n
    prime_count = [0] * (max_n + 1)
    count = 0
    
    for i in range(2, max_n + 1):
        if sieve[i]:
            count += 1
        prime_count[i] = count

    # Determine the winner for each round
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if prime_count[n] % 2 == 1:  # Odd number of primes: Maria wins
            maria_wins += 1
        else:  # Even number of primes: Ben wins
            ben_wins += 1
    
    # Return the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
"
