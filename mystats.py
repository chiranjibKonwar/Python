
import string


import statistics 
import sys


def average(numbers):
	sum = 0
	for number in numbers:
#KMK  1 the following are unnecessary 
#       	   value = 0
#           try:
#              value = float(numberstring.strip()) # i don't understand this line
#       	   except ValueError:
#          	pass  
#          sum = sum + value
           sum = sum + number
        averageval=0 
        if sum!=0:
          averageval = sum/ len(numbers)
        else : 
           averageval = sum
        return averageval


def standardDeviation(numbers):
	for number in numbers:
#		value=0
		sumOfSquareOfDiff=0


#		try:
#			value=float(numberstring.strip())
#			sumOfSquareOfDiff=(value-average(numbers))**2 + sumOfSquareOfDiff
			
#		except ValueError:
#			pass
		sumOfSquareOfDiff=(number-average(numbers))**2 + sumOfSquareOfDiff
		standardDeviation=(sumOfSquareOfDiff/len(numbers))**0.5

		return standardDeviation


def median(numbers):

    return 1000

