class Division(object):



	firstNo=None
	secondNo=None
	result=None

	def first(self):
		self.firstNo=input("enter the first number: ")
		pass

	def second(self):

		self.secondNo=input("enter the second number: ")
		pass


	def division(self):

		first(self)
		second(self)


		result="The result of dividing first number by second nubmer is %f" %(self.firstNo / self.secondNo)
		print result

if __name__=="__main__":
	init=Division()
	init.division()
