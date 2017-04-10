import sys
def base():
	basefilename = sys.argv[1]
	fh = open(basefilename, 'r')
	basefile = fh.read()
	fh.close()
	return basefile

def query():
	queryfilename = sys.argv[2]
	fh1 = open(queryfilename, 'r')
	queryfile = fh1.read()
	fh1.close()
	return queryfile

def score():
	x = base()
	y = query()
	x = x.strip()
	y = y.strip()
	print ("The database sequence length is: %d" %len(x))
	print ("The query sequence length is: %d" %len(y))
	m=0
	temp = -999	
	while m <=len(x)-len(y):
		score = 0
		for j in range(len(y)):
			if y[j] == x[j+m]:
				score+=1
			else:
				score-=1
		print "Scores against different alignments is = %d" %score
		if score>temp:
			temp = score
		m+=1
	print "The best score of all possible alignment is = %d" %temp
			

if __name__=="__main__":

	score()













