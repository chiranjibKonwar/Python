import sys

filename = sys.argv[1]
fh = open(filename, 'r')
file = fh.read()

print file

amino_acid = ['C', 'D', 'S', 'Q', 'K', 'P', 'T', 'F', 'A', 'X', 'G', 'I', 'E', 'L', 'H', 'R', 'W', 'M', 'N', 'Y', 'V']
sumtotal = 0
for a in amino_acid:
	if a in file:
		print "Percentage of %s is = %.4f" %(a,float(file.count(a))*100/len(file))
		percentage = float(file.count(a))*100/len(file)
		sumtotal = percentage + sumtotal
	else:
		print "%s is not in sequence." %a
print "Total percentage is = %f " %sumtotal



