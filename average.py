import string

fileName = raw_input("What file name: ")
lines = []
try:
    file = open(fileName)
    lines = file.readlines()
    file.close()
except:
    print "Unable to open file"
sum = 0
values = 0
if(len(lines) > 0):
    for line in lines:
        value = 0
        try:
            value = int(string.strip(line))
        except ValueError:
            pass
        if(value != 0):
            sum = sum + value
            values += 1
    print "Average = %f for %d lines, sum = %f"%(sum/values,values,sum)
else:
    print "No lines in the file"
