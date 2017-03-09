#def averageTotal():   There is not need to call it "average Total" just "average"
import string
#KMK we need this module to clean up trailing spaces or tabs


def average(numbers):
	sum = 0

# KMK removed	values = 0
#	if(len(numbers) > 0):  # KMK unnecessary if statement because if len(numbers) is 0 then the for loop will not loop anyway and hence the variable sum will remain 0 as before
	for numberstring in numbers:
       	   value = 0
           try:
#               value = float(string.strip(numberstring)) # i don't understand this line

#KMK you can also write like this 
               value = float(numberstring.strip()) # i don't understand this line
       	   except ValueError:
          	pass
# KMK unnecessary line because a + 0 is again a    	if(value != 0):   
           sum = sum + value
# KMK not needed 			values += 1


# KMK must define averageval outside of the if else block for scope  outside of it
        averageval=0 

        if sum!=0:
          averageval = sum/ len(numbers)
        else : 
# KMK this else  is to avoid division by zer0 if len(numbers) is 0
           averageval = sum

         
# KMK now return the value
        return averageval


#KMK these print statements should not be in a function that only computes average

#    		print "Average = %f for %d lines, sum = %f" %(sum/values,values,sum)
#	else : 
#    		print "No lines in the file"


