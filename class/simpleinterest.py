

class SimpleInterest:

	principal=None
	time=None
	Rate=None
	simpleInterest=None

	def principal(self):
		self.principal=input("Enter principal amount in rupees: ")

	def time(self):
		self.time=input("Enter time duration in year: ")

	def Rate(self):
		self.Rate=input ("Enter the rate of interest per annum: ")

	def SimpleInt(self):
		
		self.principal()
		self.time()
		self.Rate()
		self.simpleInterest=(self.principal*self.time*self.Rate/100)
		print "The simple interest is: %f " %self.simpleInterest


if __name__ == '__main__':

	init=SimpleInterest()

	init.SimpleInt()


	
