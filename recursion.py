#def IterativeSum(list1):
#	sum = 0
#	for x in list1:
#		sum = sum + x
#
#	return sum
#
#def main():
#	datlist = [1,2,3,4,5]
#	y = IterativeSum(datlist)
#	print y

#main()

#def RecursiveSum(Parlist):

def IterativeFactorial(num):
	i = 1
	result = 1
	while i <= num:
		result = result * i 
		i = i + 1 


	return result




def main():
	x = 5
	y = IterativeFactorial(x)
	print y


# a recursive function that returns a factorial for parameter number n.


def RecursiveFactorial(n):
	if n == 0:
		fact = 1
		return fact
	else:
		fact = n * RecursiveFactorial(n-1)
		return fact

def main():
	x = 5
	y = RecursiveFactorial(x)
	print y 


#main()


# and iterative function to decrement perameter number initial to 0 and then print the word 'great'


def IterativeDecrement(initial):
	while initial > -1:
		if initial == 0:
			print "great"
			break
		print initial
		initial = initial - 1
		
		
		
	

def main():
	x = 5
	y = IterativeDecrement(x)
	print y

#main()

# a recursive function to decrement parameter initialnum to 0 and print the word 'great'

def RecursiveDecrement(initialnum):
	
	if initialnum <= 0:
		print "Great"
		
	else:
		print initialnum
		RecursiveDecrement(initialnum-1)
		


		
 
def main():
	x = 5
	RecursiveDecrement(x)
	 

#main()













def MultipleIterative(n):
	i = 1
	while i < n + 1:
		
		r = n * i
		print r 
		i = i + 1

def main():
	x = 5
	MultipleIterative(x)
	

#main()

def MultipleRecursive(n, lst):

	if n == 1:
		print 5 

	else:
		a = n * 5
		lst.append(a)
		print a
		MultipleRecursive(n-1, lst)

	

		#return z



	







def main():
	x = 3
	y = MultipleRecursive(x)
	print y
	

#main()


def FibonacciIterative(par):
	result = []
	var1 = 0
	var2 = 1
	while var2 < par:
		result = result + [var2]
		var3 = var1 + var2
		var1 = var2
		var2 = var3
		
		print result



##########


def FibonacciRecursive(num):
	
	if num < 1:
		return 0
		#print 0
	elif num < 2:
		return 1 
		#print 1

	else:
				
		return FibonacciRecursive(num - 1) + FibonacciRecursive(num - 2)


def allfibo(n):
	x = range(n+1)
	for i in x:
		print FibonacciRecursive(i)

#def main():
#	v = 10
#	allfibo(v)
	
	

#main()






def PrintStringIterative(string, number):
		i = 0
		while i < number:
			print string
			i = i + 1

def main():
	x = "I love CS"
	y = 10
	PrintStringIterative(x, y)

#main()

def PrintStringRecursive(string, number):
	if number == 1:
		print string
	else:
		print string
		PrintStringRecursive(string, number-1)
		

def main():
	x = "I love CS"
	y = 10
	PrintStringRecursive(x, y)

#main()
	



def main():
	print "going to run function IterativeFactorial"
	x = 10
	y = IterativeFactorial(x)
	print y

	print "going to run function RecursiveFactorial"

	x = 10
	y = RecursiveFactorial(x)
	print y 

	print "going to run function IterativeDecrement"
	x = 10
	IterativeDecrement(x)
	

	print "going to run function RecursiveDecrement"


	x = 10
	RecursiveDecrement(x)

	print "going to run function MultipleIterative"

	x = 10
	MultipleIterative(x)

	print "Going to run function MultipleRecursive"

	newlist = []
	x = 10
	MultipleRecursive(x, newlist)


	print "going to run function fibonacciIterative"
	x = 10
	FibonacciIterative(x)

	print "going to run function FibonacciRecursive"

	v = 10
	allfibo(v)

	#d = AllFibo(v)
	#print d

	print "goint to run finction PrintStringIterative"
	x = "I love CS"
	y = 10
	PrintStringIterative(x, y)

	print "going to run function PrintStringRecursive"
	x = "i love CS"
	y = 10
	PrintStringRecursive(x, y)	

	
	

main()


#def RecursiveFactorial(num):
#	for i in range (len())
#		num[0]= 0 
		 

