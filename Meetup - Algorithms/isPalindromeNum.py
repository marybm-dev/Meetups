import math

# first reverse the number
def reverseNum(number):
	if number < 10:				# check if we are already at the ones term
		return number
	else:
		ones = number % 10		# grab the one's digit
		rest = number // 10 	# determine the rest by doing integer division

	# log10(num) + 1 = the # of digits in a number. e.g. log10(678) + 1 = 3.83 => cast to (int) = 3 digits
	# place the ones digit in the highest term by => ones * (10 to power of digits length)
	# then recursive call to continue with the rest of the numbers
	return ones * 10 ** int(math.log10(rest) +1) + reverseNum(rest)

# then check if the reverse equals the original number => True if yes
def isPalindromeNum(number):
	return number == reverseNum(number)

print isPalindromeNum(785)
print isPalindromeNum(353)

## SAMPLE OUTPUT 
# False
# True
