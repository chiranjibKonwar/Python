import sys

def readnumbers(filename):
 numbers = []
 try:
    file = open(filename, 'r')     #is 'file' a varible?

#    numbers = file.readlines()

# create an empty array numbers
    numbers =[] 

#
    for num in file.readlines():
       numbers.append( float(num.strip()))
     

    file.close()
 except:              # is try except like if-else?
    print ("Unable to open file %s:"  %(filename))
    sys.exit(0)
 return numbers

