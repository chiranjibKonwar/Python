import sys
from statistics import median

def number():

	fileName=sys.argv[1]
	file=open(fileName,'r')
	fileread=file.readlines()
	file.close()
	numbers=[]
	try:
		for line in fileread:
			numbers.append(int(line))
		numbers.sort()
		print numbers
		median(numbers)
		print "Median of the numbers= %f " %(median(numbers))
	except ValueError:
		pass


number()


