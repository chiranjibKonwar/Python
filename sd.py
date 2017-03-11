
import string
from mystats import average

def standardDeviation(numbers):
	sd=0
	for numberstring in numbers:
		value=0
		sumOfsqDiff=0
		try:
			value=float(numberstring.strip())
			squareOfDiff=(value-average(numbers))^2
			sumOfsqDiff=sumOfsqDiff+squareOfDiff
					
		except ValueError:
			pass
		standardDeviation=0
		standarDeviation=sumOfsqDiff/len(numbers)
		return standardDeviation
