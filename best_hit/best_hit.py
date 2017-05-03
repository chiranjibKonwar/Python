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
		rows = line.split(' ')
		for row in rows:
			d = {row[0]:row[10]}
			print d

if __name__=="__main__":

	inputfile()
	file_dict()


	




