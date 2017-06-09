import sys
filename = sys.argv[1]
fp = open(filename,'r')
text = fp.readlines()
text = str(text)
print text
words = text.split()
fp.close()
count = {}
for x in words:
	word = x.strip()	
	if word not in count:
		count[word] = 1
	elif word in count:
		count[word]+=1
for key,value in count.iteritems():
	print key,value

#print sorted([(key,value) for (key,value) in count.iteritems()])





	


