#y = '\t'
#x = [str(y)]

#print (x * 2)

#print x + x
	




def FibonacciRecursive(num):
	
	if num == 0:
		n = [0]
		#print 0
	elif num == 1:
		n = [0, 1]

	elif num == 2:
		n = [0,1,1]
		#print 1

	else:
		#n = range(num+1)
		
		fibolist = FibonacciRecursive(n[num-1]) + FibonacciRecursive(n[num-2]) + [FibonacciRecursive(n[num-3])]
		fibolist.append(fibo)
		return fibolist

		


def main():
	x = 10
	for i in FibonacciRecursive(x):
		print i 




#def allfibo(n):
#	x = range(n+1)
#	for i in x:
#		print FibonacciRecursive(i)

#def main():
#	v = 10
#	allfibo(v)
	
	

main()

def MultipleRecursive(n, lst):

	if n == 1:
		print 5 

	else:
		a = n * 5
		lst.append(a)
		print a
		MultipleRecursive(n-1, lst)
		


	
	

def MultipleIterative(n):
	i = 1

	while i < n + 1:
		
		r = 5 * i
		print r 
		i = i + 1

def main():
	x = 10

	MultipleIterative(x)
#main()




#def allmultrecursive(v):
	#x = range(v+1)
	#for i in x:
		#print MultipleRecursive(i)









