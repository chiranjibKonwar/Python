import sys

def inputfile():

	filename = sys.argv[1]
	fh = open(filename,'r')
	file = fh.readlines()
	return file
	

def file_dict():
	file = inputfile()
	d = {}	
	for line in file:
		rows = line.split('\t')
		d = {rows[0]:rows[10]}
		print d
		

if __name__=="__main__":

	inputfile()
	file_dict()


	




