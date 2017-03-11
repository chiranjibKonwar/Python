
import string
from mystats import average

def standardDeviation(numbers):
	for numberstring in numbers:
		value=0
		squareOfDiff=0
		sumOfsqDiff=0
		try:
			value=float(numberstring.strip())
			squareOfDiff=(value-average(numbers))**2
			AvgsumOfsqDiff=(sumOfsqDiff+squareOfDiff)/len(numbers)
			sqRootAvgsumOfsqDiff=AvgsumOfsqDiff**1/2
					
		except ValueError:
			pass
		standardDeviation=0
		standardDeviation=sqRootAvgsumOfsqDiff
		return standardDeviation
