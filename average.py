import string
import sys

#fileName = raw_input("What file name: ")
fileName = sys.argv[1]

#KMK learn how to pass command line  arguments to a python script so that you can you the file name as an argument
lines = []
try:
    file = open(fileName, 'r')     #is 'file' a varible?
#   KMK 'r' is for readonly mode   look up open permissions
    lines = file.readlines()
    file.close()
except:              # is try except like if-else?
    print "Unable to open file"


#KMK lear how to create a function

def averageTotal():
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
	#else : 
    	#print "No lines in the file"

averageTotal()
averageTotal()




