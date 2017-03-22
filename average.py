import sys, statistics
sys.stdout=open('output.txt','w')
print ("\n =================================\n")


#KMK 16 do not do  from statistics import median

from myutils import readnumbers
#KMK 17 readnumbers should convert themto numbers


#KMK 8 removed the above lines and you can do this in one line
from mystats import average, median , standardDeviation

#KMK 15 Note that I removed the un-necessary modules of median and std when they can be added as functions in the mystats module and simply import them when you need them

#KMK 16 "git rm --cache std.py, median.py"


#KMK 9 need the following line for the command line option manual
from optparse import OptionParser


#KMK 10 check usage
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


#KMK 11 note the dest variable mean, and store_true  and default 
    parser.add_option('--mean', dest='mean', action='store_true', default =False, 
                           help='compute the mean for the numbers')

#KMK 12 note the dest variable std, and store_true  and default 
    parser.add_option('--std', dest='std', action='store_true', default =False, 
                           help='compute the standard deviation of the numbers')


#KMK 13 note the dest variable std, and store_true  and default 
    parser.add_option('--median', dest='median', action='store_true', default =False, 
                           help='compute the meidan for  the numbers')



#KMK 7 this is where work begins
def main(argv):
    global parser

    options, args = parser.parse_args(argv)

#KMK 6 no need of this any more of explicit array access 
#    fileName = sys.argv[1]


#KMK 5 we need is ouside the if loop to be visible after the if else statment 
    numbers = [] 


#KMK 4 see were the destination is coming from 
    if options.filename:
       numbers = readnumbers(options.filename)
    else:
       print "ERROR: file " + options.filename + " does not exist!"

    if options.mean:
        print "Average = %f for %d numbers in file \"%s\"" %(average(numbers), len(numbers), options.filename)

    if options.std:
        print "StandardDev = %f for %d numbers in file \"%s\"" %(standardDeviation(numbers), len(numbers), options.filename)

    if options.median:
#KMK 14 note that I am having to import the statistics module in thid file 
        print "Median = %f for %d numbers in file \"%s\" (computed using statistics module)" %(statistics.median(numbers), len(numbers), options.filename)
#KMK 17 note that I am using the definiton inthe mystats module 
        print "Median = %f for %d numbers in file \"%s\" (coputed using mystats module)" %(median(numbers), len(numbers), options.filename)



#KMK 1 observer that this is the file actual code that is being executed, so far it has been only imports and function definiont
if __name__ == '__main__':
     createParser()

#KMK 2 this is where work begins

#KMK 3 Notice that I did not do sys.argv[0:] because I don't need the script name "average.py"
     main(sys.argv[1:])   


