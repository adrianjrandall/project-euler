__author__ = 'adrian'

'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

number_1 = 999
number_2 = 999

def check_palindrome(number_str):
	result = False
	if len(number_str) > 1:
		if number_str[0] == number_str[-1]:
			result = check_palindrome(number_str[1:-1])
	else: #len is 0 or 1
		result = True
	return result

found_palindrome = False
max_palindrome = 0

for j in range(100,999):
	for k in range(100,999):
		product = j*k
		if check_palindrome(str(product)):
			print j, k, product
			if product > max_palindrome:
				max_palindrome = product


print max_palindrome