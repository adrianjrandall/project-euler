__author__ = 'adrian'

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

primes = [2]
n = 2
while len(primes) < 10001:
	loop_broke = False
	n += 1
	for prime in primes:
		if n % prime == 0:
			loop_broke = True
			break
	if not loop_broke:
		primes.append(n)


print primes[-1]