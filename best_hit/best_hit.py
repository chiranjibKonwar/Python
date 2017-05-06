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
     
       if not rows[0] in d or  d[rows[0]][9] > float(rows[10]):
           d[rows[0]] = (rows[1],rows[2],rows[3],rows[4],rows[5],rows[6],rows[7],rows[8],rows[9], float(rows[10]), rows[11])

    for key, value in d.iteritems():
	 sys.stdout=open("best_hits.txt","a")
	 print key, value[0],value[1],value[2],value[3],value[4],value[5],value[6],value[7],value[8],value[9],value[10]
	 sys.stdout.close()

if __name__=="__main__":

    inputfile()

    file_dict()


