__author__ = 'adrian'

'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

# get LCM
# find factors of each number 2...20

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

list_of_factors = []
for k in range(2,20):
	list_of_factors.append(get_prime_factorization(k))

print list_of_factors
factors_dict = {}

for factor_list in list_of_factors:
	for factor in factor_list:
		if factor not in factors_dict.keys(): # new factor
			factors_dict[factor] = factor_list.count(factor)
		else:
			# already in factors_dict
			tmp_factor_count = factor_list.count(factor)
			if tmp_factor_count > factors_dict[factor]:
				factors_dict[factor] = tmp_factor_count

print factors_dict

LCM = 1
for factor in factors_dict:
	LCM *= (factor**factors_dict[factor])

print LCM