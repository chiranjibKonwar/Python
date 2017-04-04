#from fastareader import FastaReader, FastaRecord
import sys
from utilities.fastamodule.fastareader import *

def fprintf(file, fmt, *args):
	file.write(fmt % args)

def printf(fmt, *args):
	sys.stdout.write(fmt % args)
   	sys.stdout.flush()
 
def eprintf(fmt, *args):
   	sys.stderr.write(fmt % args)
   	sys.stderr.flush()

if __name__=="__main__":

   	filename = sys.argv[1]

   	fastaobject = FastaReader(filename)
   	for a in fastaobject:
        	print (a.name,len(a.sequence))
        	file = a.sequence
        	print(file)
        	amino_acid = ['C', 'D', 'S', 'Q', 'K', 'P', 'T', 'F', 'A', 'X', 'G', 'I', 'E', 'L', 'H', 'R', 'W', 'M', 'N', 'Y', 'V']
        	sumtotal = 0
        	for i in amino_acid:
	        	if i in file:
		    		print ("Percentage of %s is = %.4f%%" %(i,float(file.count(i))*100/len(file)))
		    		percentage = float(file.count(i))*100/len(file)
		    		sumtotal = percentage + sumtotal
			else:
				print ("%s is not in sequence." %i)
      		print ("Total percentage is = %f%%" %sumtotal)
    


   		print (filename)
   		print ('hello')





### output should be like
#  A 10%
#  B 15%
#  ....
#  N means anything

