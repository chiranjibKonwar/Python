import sys



def number():

	fileName=sys.argv[1]
	file=open(fileName,'r')
	fileread=file.readlines()
	file.close()
	numbers=[]
	try:
		for line in fileread:
			numbers.append(float(line))
		numbers.sort()
		print numbers
		print "Total count of numbers: %d" %(len(numbers))
		if(len(numbers)%2==0):
			print "The median of the numbers= "
			print (numbers[len(numbers)/2] + numbers[len(numbers)/2-1])/2
		else:
			print "The median of the numbers= "
			print numbers[(len(numbers)+1)/2-1]
		print "Mode of the numbers= %f" %(numbers[-1])
	except ValueError:
		pass


number()


