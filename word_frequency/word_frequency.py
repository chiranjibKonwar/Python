import sys
from operator import itemgetter
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
print "="*50
#print count

print sorted([(key,value) for (key,value) in count.items()])





	


