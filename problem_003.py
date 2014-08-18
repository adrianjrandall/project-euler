__author__ = 'adrian'

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

input_number = 600851475143

trial_factor = 2
factors = []
while input_number > 1:
	if (input_number % trial_factor) == 0:
		factors.append(trial_factor)
		input_number /= trial_factor
		print input_number
		print factors
	else:
		trial_factor += 1

print max(factors)