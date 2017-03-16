
import string
from mystats import average

def standardDeviation(numbers):
	for numberstring in numbers:
		value=0
		sumOfSquareOfDiff=0
		try:
			value=float(numberstring.strip())
			sumOfSquareOfDiff=(value-average(numbers))**2 + sumOfSquareOfDiff
			
		except ValueError:
			pass
		standardDeviation=(sumOfSquareOfDiff/len(numbers))**0.5
		return standardDeviation

