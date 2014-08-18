__author__ = 'adrian'
'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

# c = 1000 - b - a
# c = sqrt(a^2 + b^2)

from math import sqrt
# need to find where 1000 - b - a = sqrt(a^2 + b^2)

for a in range(1000):
	for b in range(1000):
		c2 = sqrt(a**2 + b**2)
		c = 1000 - b - a
		if c2 == c:
			print a*b*c
			break
