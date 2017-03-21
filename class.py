class Parent:
  
	var1="parent variable1"
	var2="parent variable2"
  	def father(self):
    		print " this is father, mino\n"
  	def mother(self):
    		print "this is mother, majoni\n"


class Child(Parent):
	pass
  
cob=Child()
print cob.var2
print cob.father()
pob=Parent()
print pob.var1
print pob.mother()
