#!/usr/bin/python3
"""A module to solve the problem of the prime game winner"""


def SieveOfEratosthenes(n):
    """Find the prime numbers from number n down to zero"""
    prime = [True for i in range(n+1)]
    primes_list = [0 for i in range(n+1)]
    pr = 2
    prime_nums = 0
    for pr in range(2, n + 1):
        if (prime[pr]):
            prime_nums += 1
            for i in range(pr * pr, n+1, pr):
                prime[i] = False
            primes_list[pr] = prime_nums
        return (primes_list)

def isWinner(x, nums):
    """choose the winner of the prime game either Maria or Ben"""
    if not x or not numbers or x < 0:
        return None
    Maria_wins = 0
    Ben_wins = 0
    the_max = max(numbers[0:x])
    primes_lists = SieveOfEratosthenes(the_max)

    for i in range(x):
        prime_nums = primes_lists[numbers[i]]
        if (prime_nums % 2):
            Maria_wins += 1
        else:
            Ben_wins += 1

        if (Maria_wins > Ben_wins):
            return 'Maria'
        if (Ben_wins > Maria_wins):
            return 'Ben'
