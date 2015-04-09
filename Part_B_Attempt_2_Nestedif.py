#/**********************************************************************/ 
#/* CSC 280 – Programming Project 3 Part 2 Attempt 2 								*/ 
#/* 																	*/ 
#/* modifier: Dri Torres 												*/ 
#/* 																	*/ 
#/* filename: Part_B_Attempt_2_Nestedif.py 							*/ 
#/* modified from: CSC 280 Prog Progect #3 								*/ 
#/* date last modified: 10-18-2013 										*/ 
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

f =  float(raw_input("Input the first number: "))
s = float(raw_input("Input the second number: "))
t = float(raw_input("Input the second number: "))

if f > s:
	if f > t:
		print "max = " +str(f)+ " "
		if s > t:
			print "min = " +str(t)+ " "
		else:
			print "min = " +str(s)+ " "
	else:
		print "max = " +str(s)+ " "
		print "min = " +str(s)+ " "
else:
	if s > t:
		print "max = " +str(s)+ " "
		if  t > f:
			print "min = " +str(f)+ " "
		else:
			print "min = " +str(t)+ " "
	else:
		print "max = " +str(t)+ " "
		print "min = " +str(f)+ " "