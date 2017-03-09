import sys
from mystats import average
from myutils import readnumbers

fileName = sys.argv[1]

numbers = readnumbers(fileName)

#KMK observe how I am able to show in double quote around the filename
print "Average = %f for %d numbers in file \"%s\"" %(average(numbers), len(numbers), fileName)


#KMK see the file I created .gitignore 
#KMK what do you think are the .pyc files?




