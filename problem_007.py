__author__ = 'adrian'

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

def get_prime_factorization(n):
	# n must be integer >= 2
	factors = []
	k = 2 # test factor
	while n > 1:
		if n % k == 0:
			n /= k
			factors.append(k)
			k = 2 # reset to orig to get prime factorization
		else:
			k += 1
	return factors

num_primes = 0 # will find 2 is a prime and we'll call that the first one
n = 2
while num_primes < 10001:
	factors_list = get_prime_factorization(n)
	if len(factors_list) == 1: # prime
		num_primes += 1
		print num_primes
		print n
	n += 1