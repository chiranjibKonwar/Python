import numpy
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
print "The database sequence is %s and it's length is %d" %(x,len(x))
print "The query sequence is %s and it's length is %d" %(y,len(y))


def alignScore():
	m=0
	while m <=len(x)-len(y):
		score = 0
		Max = 0
		for j in range(len(y)):
			if y[j] == x[j+m]:
				score+=1
			elif y[j] != x[j+m]:
				score-=1		
		m+=1 
		print score
alignScore()





















