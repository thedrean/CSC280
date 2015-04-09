
#/**********************************************************************/ 
#/* CSC 280 – Programming Project 3 Part 1 								*/ 
#/* 																	*/ 
#/* modifier: Dri Torres 												*/ 
#/* 																	*/ 
#/* filename: Dri_Torres_Project_3_Part_1.py 							*/ 
#/* modified from: CSC 280 Prog Progect #3 								*/ 
#/* date last modified: 10-06-2013 										*/ 
#/* 																	*/ 
#/* action: computes the minimum score, maximum score, and average score*/
#/* of a total specified scores											*/
#/* 																	*/ 
#/* input: total number of scores, value of each score given as real 	*/
#/* numbers																*/ 
#/*																		*/
#/* output: the minimum score, maximum score, and average of all scores */
#/*         							                            	*/
#/**********************************************************************/  

#Prompt user for the total number number of scores, given as real numbers
t= int(raw_input("Enter the total number of scores: \t \t"))
min = 101
max = -1
totalscore = 0 
print "Enter the scores: "
#Prompt user for previously specified number of scores, given as real numbers 
for index in xrange (1, t +1):
    currentscore = float(raw_input("Score " + str(index) +" \t \t \t \t \t"))
#Computes the minimum score, maximum score, and ta
    if currentscore < min:
        min = currentscore
    if currentscore > max:
        max = currentscore 
    totalscore = totalscore + currentscore 
 #Outputs the minimum and maximim values, given as real numbers
print "The minimum is:\t \t \t \t \t" + str(min) + " "
print "The maximum is:\t\t \t \t \t" + str(max) + " "
#Computes average of all values, given as real numbers
average = (totalscore / t)
print "The average is:\t \t \t \t \t" +str(average)+ " "

#Enter the total number of scores: 	 	4
#Enter the scores: 
#Score 1 	 	 	 	 	10
#Score 2 	 	 	 	 	36
#Score 3 	 	 	 	 	5.5
#Score 4 	 	 	 	 	0.5
#The minimum is:	 	 	 	 	0.5 
#The maximum is:		 	 	 	36.0 
#The average is:	 	 	 	 	13.0 
#mgc-121-185:desktop Home$ 

   







   
    
