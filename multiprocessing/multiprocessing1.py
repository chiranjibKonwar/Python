


from multiprocessing import Pool

def f(n):
	return n**2

Array = [1,2,3,4,5]

p = Pool()
result = p.map(f,Array)
print result


# using single core


"""
def f(n):
	return n**2

if __name__=="__main__":

	Array = [1,2,3,4,5]

	result = []
	for n in Array:
		result.append(f(n))
	print result

"""
