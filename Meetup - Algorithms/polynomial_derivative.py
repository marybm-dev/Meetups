'''
	polynomial_derivative.py

	Purpose: take in an array of Terms that represents a polynomial; e.g. 2x^2 + 3x + 4; and return it's derivative
	Notes: currently does not support negative exponent, square roots or logarithms
	Created: 09/03/2015 mlmartinez85@gmail.com
'''

from collections import namedtuple

# C-like struct for a Term Object
#	an array of Term objects = polynomial    (view main() for an example)
# 	e.g. 2x^3 is one term => coefficient is 2, variable is x, exponent is 3
Term = namedtuple("Term", "coefficient variable exponent")

def derivative(polynomial):
	# our derivative array = array of ddx terms
	result = []

	for term in polynomial:
		# case for a constant: i.e. if we have 4x^0 then this is really the constant 4
		#		the derivative of a constant is always 0 so continue
		if term[2] == 0:
			continue

		# take the derivative of valid term
		ddx = term[0] * term[2]

		# append the derivative of this term to our polynomial (aka result array)
		result.append(Term(ddx, 'x', term[2] - 1))
	
	# return the human friendly display of the derivate
	return display(result)


def display(polynomial):
	result = ""
	for term in polynomial:
		# add a + if we have terms
		if result != "":
			result += ' + '
		# cases for exponent = 0, 1, >1
		if term[2] == 0:					# this term is a constant
			result += ( str(term[0]) )
		elif term[2] == 1:							# this term has degree of one
			result += ( str(term[0]) + term[1] )	
		else:												# this term has higher degree
			result += ( str(term[0]) + term[1] + '^' + str(term[2]) )		
	# return the human friendly string display
	return result


def main():
	# first create the Terms of our polynomial
	degree2 = Term(2, 'x', 3)
	degree1 = Term(3, 'x', 1)
	constant = Term(4, 'x', 0)

	# create an array of terms => this is our polynomial
	polynomial = [degree2, degree1, constant]

	# print the polynomial and it's derivative
	print display(polynomial)
	print derivative(polynomial)



# run the main program
main()
