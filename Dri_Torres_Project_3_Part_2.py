#/**********************************************************************/ 
#/* CSC 280 – Programming Project 3 Part 2 								*/ 
#/* 																	*/ 
#/* modifier: Dri Torres 												*/ 
#/* 																	*/ 
#/* filename: Dri_Torres_Project_3_Part_2.py 							*/ 
#/* modified from: CSC 280 Prog Progect #3 								*/ 
#/* date last modified: 10-06-2013 										*/ 
#/* 																	*/ 
#/* action: computes the minimum value and maximum value of three total */
#/* values																*/ 
#/* 																	*/ 
#/* input: three different values, entered by the user as prompted for, */
#/* given as real numbers. 												*/
#/*																		*/
#/* output: the minimum value and the maximum value.    				*/
#/*         							                            	*/
#/**********************************************************************/

#Promps user for three different inputs given as real numbers
a = float(raw_input("Enter the first number: "))
b = float(raw_input("Enter the second number: "))
c = float(raw_input("Enter the third number: "))
#Computs the minimum and maximum of the three input values
#Prints computed minumin value and computed maximum values as real numbers
if a < b and a < c:
	print "The smallest of the values is: " +str(a)+ "."
	if b > c:
		print "The largest of the values is: " +str(b)+ "."
	else:
		print "The largest of the values is: " +str(c)+ "."
elif a > b and a > c:
	print "The biggest of the values is: " +str(a)+ "."
	if b < c:
		print "The smallest of the values is: " +str(b)+ "."
	else: 
		print "The smallest of the values is: " +str(c)+ "."
elif b > c:
	print "The biggest of the values is: " +str(b)+ "."
	print "The smallest of the values is: " +str(c)+ "."
else:
	print "The biggest of the values is: " +str(c)+ "."
	print "The smallest of the values is: " +str(b)+ "."

#Enter the first number: 20.5
#Enter the second number: 14.3
#Enter the third number: 90.9
#The biggest of the values is: 90.9.
#The smallest of the values is: 14.3.
#mgc-121-185:desktop Home$ python Dri_Torres_Project_3_Part_2.py 
#
#Enter the first number: 12.5
#Enter the second number: 25.75
#Enter the third number: 30.8
#The smallest of the values is: 12.5.
#The largest of the values is: 30.8.
#mgc-121-185:desktop Home$ 55.7
#-bash: 55.7: command not found
#mgc-121-185:desktop Home$ python Dri_Torres_Project_3_Part_2.py 
#
#Enter the first number: 55.7
#Enter the second number: 30.4
#Enter the third number: 34.5
#The biggest of the values is: 55.7.
#The smallest of the values is: 30.4.
#mgc-121-185:desktop Home$ python Dri_Torres_Project_3_Part_2.py 
#
#Enter the first number: 110.2
#Enter the second number: 43.5
#Enter the third number: 35
#The biggest of the values is: 110.2.
#The smallest of the values is: 35.0.
