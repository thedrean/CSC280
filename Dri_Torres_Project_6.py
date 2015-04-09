
#/**********************************************************************/ 
#/* CSC 280 – Programming Project 6										*/ 
#/* 																	*/ 
#/* modifier: Dri Torres 												*/ 
#/* 																	*/ 
#/* filename: Dri_Torres_Project_6.py 									*/ 
#/* modified from: CSC 280 Prog Progect #6								*/ 
#/* date last modified: 11-03-2013 										*/ 
#/* 																	*/ 
#/* action: Computes monthly cost of a loan with a specified interest 	*/
#/*	rate over a specified number of months								*/
#/*     																*/
#/* 																	*/ 
#/* input: the yearly interest rate, the principal amount of the loan,	*/
#/* and the number of months 											*/
#/* 																	*/ 
#/*																		*/
#/* output: The cost of the loan after interest as well as the monthy   */
#/* payment of the loan.       									 		*/
#/**********************************************************************/

#Defines function MonthlyPayment which returnes a type long integer for the payment each month

def MonthlyPayment(amountOfLoan, numberOfPeriods, rate):
	pay = (((rate/12)/(((1-(1+(rate/12))**(-numberOfPeriods))))) * amountOfLoan)
	return pay

#Defines function LoanCost which returnes the cost of the of the loan computed with the additional inerest rate

def LoanCost(principal, months, payment1):
	cost = months * payment1 - principal
	return cost

#Defines the main function which promps user for data to be used in functions MonthlyPayment and LoanCost calls LoanCost with arguements principal, months, and rate. Prints the cost.

def main():
	
	rate = float(raw_input("Enter the yearly interest rate: "))
	principal = long(raw_input("Enter the principal: $ "))
	months = int(raw_input("Enter the amount of months: "))
	payment = MonthlyPayment(principal, months, rate)
	cost = LoanCost(principal, months, payment)
	print "The monthly payment is: $" +str(payment)+ " "
	print "The loan cost is : $" +str(cost)+ " "

#Calls the main function

main()

#letts-agg-101-145:CS 280 Home$ python Dri_Torres_Project_6.py 
#Enter the yearly interest rate: .0825
#Enter the principal: $ 180000
#Enter the amount of months: 360
#The monthly payment is: $1352.27988729 
#The loan cost is : $306820.759425 

#letts-agg-101-145:CS 280 Home$ python Dri_Torres_Project_6.py 
#Enter the yearly interest rate: .1025
#Enter the principal: $ 180000
#Enter the amount of months: 360
#The monthly payment is: $1612.98233305 
#The loan cost is : $400673.639896

#letts-agg-101-145:CS 280 Home$ python Dri_Torres_Project_6.py 
#Enter the yearly interest rate: .0825
#Enter the principal: $ 180000
#Enter the amount of months: 180
#The monthly payment is: $1746.25264403 
#The loan cost is : $134325.475925 

#letts-agg-101-145:CS 280 Home$ python Dri_Torres_Project_6.py 
#Enter the yearly interest rate: .0825
#Enter the principal: $ 200000
#Enter the amount of months: 360
#The monthly payment is: $1502.5332081 
#The loan cost is : $340911.954917









