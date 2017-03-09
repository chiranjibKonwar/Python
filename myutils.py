import sys

def readnumbers(filename):
 numbers = []
 try:
    file = open(filename, 'r')     #is 'file' a varible?
    numbers = file.readlines()
    file.close()
 except:              # is try except like if-else?
#KMK this is becuase of some failure and usually unexpected 
    print "Unable to open file %s:"  %(filename)
#KMK  let's exit this is a serious error
#KMK observe in line 1 I am importing the sys module
    sys.exit(0)
 return numbers

