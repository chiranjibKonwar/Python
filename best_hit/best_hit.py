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
      
       # if this is the first time the query is encounter or 
       # the new one is even smaller then the one already in 'd' then  keep it
       d[rows[0]] = []
       if not rows[0] in d or  d[rows[0]] > float(rows[10]):
           d[rows[0]] = (rows[1], float(rows[10]))

    #now print the results out
    for key, value in d.iteritems():
	 sys.stdout=open("best_hits.txt","a")
	 print key, value
	 sys.stdout.close()

if __name__=="__main__":

    inputfile()

    file_dict()


    




