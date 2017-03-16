
import string


def average(numbers):
	sum = 0
	for numberstring in numbers:
       	   value = 0
           try:
              value = float(numberstring.strip()) # i don't understand this line
       	   except ValueError:
          	pass  
           sum = sum + value
        averageval=0 
        if sum!=0:
          averageval = sum/ len(numbers)
        else : 
           averageval = sum
        return averageval
