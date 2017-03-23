import sys, statistics

#do not do  from statistics import median

from myutils import readnumbers
#readnumbers should convert themto numbers


#removed the above lines and you can do this in one line
from mystats import average, median , standardDeviation

# Note that I removed the un-necessary modules of median and std when they can be added as functions in the mystats module and simply import them when you need them

#"git rm --cache std.py, median.py"


# need the following line for the command line option manual
from optparse import OptionParser


#check usage
usage = sys.argv[0] + """ -file <filename>  [ OPTIONS --std/median/mean ]"""

parser = None
def createParser():
	global parser
	epilog = """This script is used for computing stats for numbers listed in a text file
                e.g. 1.  python average.py --fiile <name> --std  2.  python average.py --fiile <name> --average --std .... or any other combination"""
	parser = OptionParser(usage=usage, epilog=epilog)

    # Input options
	parser.add_option('--file', dest='filename', 
                           help='the name of the file that has the numbers')


#note the dest variable mean, and store_true  and default 
	parser.add_option('--mean', dest='mean', action='store_true', default =False, 
                           help='compute the mean for the numbers')

# note the dest variable std, and store_true  and default 
	parser.add_option('--std', dest='std', action='store_true', default =False, 
                           help='compute the standard deviation of the numbers')


# note the dest variable std, and store_true  and default 
	parser.add_option('--median', dest='median', action='store_true', default =False, 
                           help='compute the meidan for  the numbers')

#KMK 1 add an option like --out to provide a output file name
# and complete the line
	parser.add_option('--out', dest='outfile',  default =None,) 



# this is where work begins
def main(argv):
	global parser
	options,args = parser.parse_args(argv)

# no need of this any more of explicit array access 
#    fileName = sys.argv[1]


# we need is ouside the if loop to be visible after the if else statment 
	numbers = [] 


# see were the destination is coming from 

#KMK 6  you can open all files at once in one place
	fhavg=open("rikuAverage",'a')
	fhstd=open("rikustd",'a')
	fhmed=open("rikumedian",'a')


	if options.filename:
      		 numbers = readnumbers(options.filename)
	else:
      	 	print ("ERROR: file " + options.filename + " does not exist!")
	if options.mean:
		#fh=open("rikuAverage",'a')
#KMK 8  may be just use write instead of print 

#		print ("Average = %f for %d numbers in file \"%s\"" %(average(numbers), len(numbers), options.filename), file = fhavg)
		fhavg.write("Average = %f for %d numbers in file \"%s\"" %(average(numbers), len(numbers), options.filename))
		#fh.close()

	if options.std:
		#fh=open("rikustd",'a')
		print ("StandardDev = %f for %d numbers in file \"%s\"" %(standardDeviation(numbers), len(numbers), options.filename), file=fhstd)
		#fh.close()
	if options.median:
# note that I am having to import the statistics module in thid file 
		#fh=open("rikumedian",'a')
		print ("Median = %f for %d numbers in file \"%s\" (computed using statistics module)" %(statistics.median(numbers), len(numbers), options.filename), file=fhmed)

#KMK 4 you don't have to keep closing until you are done writing to this file
#		fh.close()
# note that I am using the definiton inthe mystats module 

#KMK 5 remove this open
#		fh=open("rikumedian",'a')
		print ("Median = %f for %d numbers in file \"%s\" (coputed using mystats module)" %(median(numbers), len(numbers), options.filename), file=fhmed)
		#fh.close()

#KMK 7 Close all the above files
	fhavg.close()
	fhstd.close()
	fhmed.close()
       

#KMK 3 follow the following template and 
#	if options.outfile:
#		outfile=open(options.outfile,'w')
#		outfile.write('hello')


# observer that this is the file actual code that is being executed, so far it has been only imports and function definiont
if __name__ == '__main__':
	createParser()

# this is where work begins

# Notice that I did not do sys.argv[0:] because I don't need the script name "average.py"
	main(sys.argv[1:])   


