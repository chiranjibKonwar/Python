
import string
from mystats import average

def standardDeviation(numbers):
	for numberstring in numbers:
		value=0
		squareOfDiff=0
		AvgOfsqOfDiff=0
		sumOfsquareOfDiff=0
		sqRoot=0
		try:
			value=float(numberstring.strip())
			squareOfDiff=(value-average(numbers))**2
			sumOfsquareOfDiff=sumOfsquareOfDiff + squareOfDiff
			
		except ValueError:
			pass
		AvgOfsqOfDiff=sumOfsquareOfDiff/len(numbers)
		sqRoot=AvgOfsqOfDiff**1/2
		standardDeviation=0
		standardDeviation=sqRoot
		return standardDeviation
