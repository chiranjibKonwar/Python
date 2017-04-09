import sys
basefilename = sys.argv[1]
fh = open(basefilename, 'r')
basefile = fh.read()
fh.close()

queryfilename = sys.argv[2]
fh1 = open(queryfilename, 'r')
queryfile = fh1.read()
fh1.close()

x = basefile
y = queryfile
x = x.strip()
y = y.strip()
print ("The database sequence is: \n %s \n and it's length is: \n %d" %(x,len(x)))
print ("The query sequence is: \n %s \n and it's length is: \n %d" %(y,len(y)))

import sys

def score():
	m=0
	temp = 0	
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
			
score()
















