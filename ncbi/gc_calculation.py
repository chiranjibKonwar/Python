fh=open(filename,'r')
file=fh.read()
x=file

def gc_cal():

	c=0
	a=0
	g=0
	t=0
	for x in file:
		if "C" in x:
			c+=1	
		elif "G" in x:
			g+=1
		elif "A" in x:
			a+=1	
		elif "T" in x:
			t+=1
		elif "Einstein" in x:
			e+=1
	print "C=%d, G=%d, A=%d, T=%d" %(c,g,a,t)
	gc_content=(g+c)*100/(a+t+g+c)
	print "gc_content= %f" %(gc_content)

gc_cal()
	
