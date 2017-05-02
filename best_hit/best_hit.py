import sys

def inputfile():

	filename = sys.argv[1]
	fh = open(filename,'r')
	return fh
	

def file_dict():
	fh = inputfile()
	d = {}	
	for line in fh:
		rows = line.split('\t')
		print rows
	for row in rows:
		d = {row[0]:row[10:]}
		print d

if __name__=="__main__":

	inputfile()
	file_dict()


	




