__author__ = 'adrian'
'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

primes = [2]
n = 3
while primes[-1] < 2000000:
	loop_broke = False
	for prime in primes:
		if n % prime == 0:
			loop_broke = True
			break
	if not loop_broke:
		primes.append(n)
	print n
	print len(primes)
	n += 2
print sum(primes[:-1])