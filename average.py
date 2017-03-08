import string
fileName = raw_input("What file name: ")
lines = []
try:
    file = open(fileName)     #is 'file' a varible?
    lines = file.readlines()
    file.close()
except:              # is try except like if-else?
    print "Unable to open file"

def average(sum,values):
	sum = 0
	values = 0
	if(len(lines) > 0):
    		for line in lines:
        		value = 0
        	try:
            		value = float(string.strip(line)) # i don't understand this line
        	except ValueError:
            		pass
        		if(value != 0):
            			sum = sum + value
            			values += 1
    		print "Average = %f for %d lines, sum = %f" %(sum/values,values,sum)
	else:
    		print "No lines in the file"
