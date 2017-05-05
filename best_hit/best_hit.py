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

       #KMK why is the following line necessary
       #d[rows[0]] = []

       #KMK if not rows[0] in d or  d[rows[0]] > float(rows[10]):
       #   d[rows[0]] means a pair "( rows[1], float(rows[10])" 
       #   d[rows[0]][0] means a pair the first element of the pair, i.e.,  rows[1]" 
       #   d[rows[0]][1] means a pair the second element of the pair, i.e., float(rows[10])" 

       if not rows[0] in d or  d[rows[0]][1] > float(rows[10]):
           d[rows[0]] = (rows[1], float(rows[10]))

    #now print the results out
    outfh = open("best_hits.txt", "w")  

    for key, value in d.iteritems():
         print  key + '\t' + value[0] + '\t' + str(value[1]) 
         outfh.write( key + '\t' + value[0] + '\t' + str(value[1]) + '\n')
    sys.stdout.close()

if __name__=="__main__":

    inputfile()

    file_dict()


    




