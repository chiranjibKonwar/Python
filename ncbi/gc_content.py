import sys
from gc_calculation import gc_cal

from optparse import OptionParser
usage = sys.argv[0] + """ -file <filename>  [ OPTIONS --std/median/mean ]"""

parser = None
def createParser():
	global parser
	epilog = """This program calculates the gc_content of a ATGC sequence"""
	parser = OptionParser(usage=usage, epilog=epilog)

	parser.add_option('--file', dest='filename', 
                           help='the name of the fasta file')



	parser.add_option('--out', dest='outfile',  default =None,) 

def main(argv):
	global parser
	options,args = parser.parse_args(argv)
	gc_content = []
	if options.filename:
      		 gc_content = gc_cal()

if __name__ == '__main__':
	createParser()

	main(sys.argv[1:])   


