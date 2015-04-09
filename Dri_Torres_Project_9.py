#/**********************************************************************/ 
#/* CSC 280 – Programming Project 9										*/ 
#/* 																	*/ 
#/* modifier: Dri Torres 												*/ 
#/* 																	*/ 
#/* filename: Dri_Torres_Project_9.py 									*/ 
#/* modified from: CSC 280 Prog Progect #9								*/ 
#/* date last modified: 11-03-2013 										*/ 
#/* 																	*/ 
#/* action: Creates recursive and iterative versions of Factorial,  	*/
#/*	Multiple, Decrement, Fibonacci, and PrintString						*/
#/*     																*/
#/* 																	*/ 
#/* input: the value 10 for all functions								*/
#/* 																	*/ 
#/*																		*/
#/* output: Factorial 10, Multiple 10, Decrement 10, Fibonacci 10,		*/
#/* and PrintString 10 	  									 			*/
#/**********************************************************************/





#defines function IterativeFactorial


def IterativeFactorial(num):
	i = 1
	result = 1
	while i <= num:
		result = result * i 
		i = i + 1 


	return result

#defines function RecursiveFactorial

def RecursiveFactorial(n):
	if n == 0:
		fact = 1
		return fact
	else:
		fact = n * RecursiveFactorial(n-1)
		return fact

#defines function IterativeDecriment

def IterativeDecrement(initial):
	while initial > -1:
		if initial == 0:
			print "great"
			break
		print initial
		initial = initial - 1

#defines function RecursiveDecrement

def RecursiveDecrement(initialnum):
	
	if initialnum <= 0:
		print "Great"
		
	else:
		print initialnum
		RecursiveDecrement(initialnum-1)

#defines function MultipleIterative

def MultipleIterative(n):
	i = 1

	while i < n + 1:
		
		r = 5 * i
		print r 
		i = i + 1

#defines function MultipleRecursive

def MultipleRecursive(n, lst):

	if n == 1:
		print 5 

	else:
		a = n * 5
		lst.append(a)
		print a
		MultipleRecursive(n-1, lst)

#defines function FibinacciIterative

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

#defines function FibonacciRecursive 

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

#defines function PrintStringIterative

def PrintStringIterative(string, number):
		i = 0
		while i < number:
			print string
			i = i + 1

#defines function PrintStringRecursive

def PrintStringRecursive(string, number):
	if number == 1:
		print string
	else:
		print string
		PrintStringRecursive(string, number-1)

#defines main function that runs all previous function with the value 10 set to variable x
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


	print "goint to run finction PrintStringIterative"
	x = "I love CS"
	y = 10
	PrintStringIterative(x, y)

	print "going to run function PrintStringRecursive"
	x = "i love CS"
	y = 10
	PrintStringRecursive(x, y)	

main()


#Output:

#going to run function IterativeFactorial
#3628800
#going to run function RecursiveFactorial
#3628800
#going to run function IterativeDecrement
#10
#9
#8
#7
#6
#5
#4
#3
#2
#1
#great
#going to run function RecursiveDecrement
#10
#9
#8
#7
#6
#5
#4
#3
#2
#1
#Great
#going to run function MultipleIterative
#5
#10
#15
#20
#25
#30
#35
#40
#45
#50
#Going to run function MultipleRecursive
#50
#45
#40
#35
#30
#25
#20
#15
#10
#5
#going to run function fibonacciIterative
#[1]
#[1, 1]
#[1, 1, 2]
#[1, 1, 2, 3]
#[1, 1, 2, 3, 5]
#[1, 1, 2, 3, 5, 8]
#going to run function FibonacciRecursive
#0
#1
#1
#2
#3
#5
#8
#13
#21
#34
#55
#goint to run finction PrintStringIterative
#I love CS
#I love CS
#I love CS
#I love CS
#I love CS
#I love CS
#I love CS
#I love CS
#I love CS
#I love CS
#going to run function PrintStringRecursive
#i love CS
#i love CS
#i love CS
#i love CS
#i love CS
#i love CS
#i love CS
#i love CS
#i love CS
#i love CS
#localhost:CS 280 Home$ 
