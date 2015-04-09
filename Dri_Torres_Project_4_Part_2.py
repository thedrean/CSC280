
#/**********************************************************************/ 
#/* CSC 280 – Programming Project 4 Part 2 								*/ 
#/* 																	*/ 
#/* modifier: Dri Torres 												*/ 
#/* 																	*/ 
#/* filename: Dri_Torres_Project_4_Part_2.py 							*/ 
#/* modified from: CSC 280 Prog Progect #4 								*/ 
#/* date last modified: 10-06-2013 										*/ 
#/* 																	*/ 
#/* action: Asks user how many times is wants to run program(how many 	*/
#/*	invacations). Program adds whole numbers between 0 and specified 	*/
#/* input number.    													*/
#/* 																	*/ 
#/* input: How many times you want to run the program. One whole 		*/
#/* number whose sum is to be computed for each invocation.				*/
#/* 																	*/ 
#/*																		*/
#/* output: One computed sum for each invocation.						*/
#/*         							                            	*/
#/**********************************************************************/

#Defines the function SumOfWhileNums which compues the addition of consecutive numbers between 1 and vaiable N.

def SumOfWholeNums(N):
	
	SumOfWholeNums = N * (N + 1) / 2

	print SumOfWholeNums

#Defines the main function which prompt user for input of number of times for SumOfWholeNums to be invoked and the arguement for SumOfWholeNums.

def main():
	inv = int(raw_input("How many invocations for SumOfWholeNums (): "))

	for i in range(inv):
		N = int(raw_input("Enter the value of the function's arguement N: "))
#Invokes function SumOfWholeNums.
		SumOfWholeNums(N)
#Invokes the main function.
main()

#mgc-123-182:CS 280 Home$ python Dri_Torres_Project_4_Part_2.py 
#How many invocations for SumOfWholeNums (): 4
#Enter the value of the function's arguement N: 15
#120
#Enter the value of the function's arguement N: 30
#465
#Enter the value of the function's arguement N: 80
#3240
#Enter the value of the function's arguement N: 110
#6105
