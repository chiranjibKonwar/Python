fh=open("homosapiens.fasta",'r')

file=fh.read()
x=file
c=0
a=0
g=0
t=0
for x in file:
	if "C" in x:
		c+=1
print "C=%d"%c

for x in file:	
	if "G" in x:
		g+=1
print "G=%d" %g

for x in file:
	if "A" in x:
		a+=1
print "A=%d"%a

for x in file:	
	if "T" in x:
		t+=1
print "T=%d" %t

gc_content=(g+c)*100/(a+t+g+c)

print "gc_content= %f" %(gc_content)
