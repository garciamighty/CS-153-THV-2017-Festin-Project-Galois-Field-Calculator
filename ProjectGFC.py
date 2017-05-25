# MICHAEL TYRONE GARCIA
# CS 153 THV (SUSAN PANCHO-FESTIN): PROJECT - GALOIS FIELD CALCULATOR [GF(2^m)]
# May 25, 2017

# Generally assume correct input.
import sys
import numpy as np
from numpy.polynomial import polynomial as P


# operationChooser is a function that prints options for the user to choose from, saves user input, and returns it as an integer.
def operationChooser():
	print "\nChoose an operation: "
	print "1. [Addition] A(x) + B(x) "
	print "2. [Subtraction] A(x) - B(x) "
	print "3. [Multiplication] A(x) x B(x) "
	print "4. [Division] A(x) / B(x) "
	operation = raw_input()
	
	return int(operation)
	
# polyPrinter is a function that prints a polynomial in a 'pretty format' as an output in the console using a numpy array as an input argument.
def polyPrinter(list):
	first = 1
	for x in range(len(list)-1, -1, -1):
		if list[len(list)-1 - x] != 0:
			if first != 1: 
				print "+",
				
			if list[len(list)-1 - x] != 1 or x == 0:
				print '',
				sys.stdout.write(format(int(list[len(list)-1 - x])))
				
			if x == 1:
				print "x",
			elif x != 0:
				print "x^{}".format(x),

			first = 0
		elif first == 1 and x is 0:
			print "0",
			first = 0
	print ""


# Start of Program	
print "Welcome to Galois Field Calculator [GF(2^m)]!\n"

# Asks user to input coefficients of polynomials A(x), B(x), and P(x), and saves each of them as a numpy array.
A = raw_input("Please input the coefficients of the polynomial A(x): ")
a = A.split()
a = np.array([int(x) for x in a])

B = raw_input("Please input the coefficients of the polynomial B(x): ")
b = B.split()
b = np.array([int(x) for x in b])

C = raw_input("Please input the coefficients of the irreducible polynomial P(x): ")
c = C.split()
c = np.array([int(x) for x in c])


# Asks user to choose an operation for the calculator to use using the operationChooser function.
operation = operationChooser()
while operation < 1 or operation > 4:
	print "Invalid Input. Try again.\n"
	operation = operationChooser()

# Prints out A(x), B(x), and P(x) to the console.	
print '\nA(x) = ',
polyPrinter(a)
print 'B(x) = ',
polyPrinter(b)
print 'P(x) = ',
polyPrinter(c)


# Depending on the operation the user chose, do one of the following operations using the numpy library:
if operation == 1:
	# A(x) + B(x)
	answer = P.polyadd(a[::-1], b[::-1])[::-1]
elif operation == 2:
	# A(x) - B(x)
	answer = P.polysub(a[::-1], b[::-1])[::-1]
elif operation == 3:
	# A(x) * B(x)
	answer = P.polymul(a[::-1], b[::-1])[::-1]
	# 'product' modulo 2 since this is in GF(2^m)
	answer = [x % 2 for x in answer]
	# 'remainder' modulo P(x)
	answer = P.polydiv(answer[::-1], c[::-1])[1][::-1]
elif operation == 4:
	# A(x) / B(x)
	answer = P.polydiv(a[::-1], b[::-1])[1][::-1]
	# 'product' modulo 2 since this is in GF(2^m)
	answer = [x % 2 for x in answer]
	# 'remainder' modulo P(x)
	answer = P.polydiv(answer[::-1], c[::-1])[1][::-1]


# The result 'answer' is then further simplified to 'answer modulo 2' because we are operating inside the constraints of GF(2^m).	
answer = [x % 2 for x in answer]
# Prints out the final simplified result as a polynomial using the function polyPrinter.
print 'Output of Chosen Operation = ',
polyPrinter(answer)