import sys
from fastareader import FastaReader, FastaRecord
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
      print a.name,  len(a.sequence)
    

   print filename
   print 'hello'


### output should be like
#  A 10%
#  B 15%
#  ....
#  N means anything

