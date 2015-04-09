#/**********************************************************************/ 
#/* CSC 280 – Programming Project 4 Part 1 								*/ 
#/* 																	*/ 
#/* modifier: Dri Torres 												*/ 
#/* 																	*/ 
#/* filename: Dri_Torres_Project_4_Part_1.py 							*/ 
#/* modified from: CSC 280 Prog Progect #4 								*/ 
#/* date last modified: 10-06-2013 										*/ 
#/* 																	*/ 
#/* action: computes the total and average scores of a total specified  */
#/* scores																*/
#/* 																	*/ 
#/* input: value of each score given as real numbers					*/ 
#/*																		*/
#/* output: the total and average of all scores 						*/
#/*         							                            	*/
#/**********************************************************************/

print "Enter the scores: "
a = int(raw_input("Score 1: "))
b = int(raw_input("Score 2: "))
numofscores = 2
totalscore = a + b 

while b > a:
	a = b
	b = int(raw_input("Score " +str(numofscores + 1)+ ": "))
	numofscores = numofscores + 1
	totalscore = totalscore + b

totalscore = totalscore - b
print "Total: " +str(totalscore)+ " "
numofscores = numofscores - 1
print "Average: " +str(totalscore / numofscores)+ " "



#gc-123-182:CS 280 Home$ python Dri_Torres_Project_4_Part_1.py 
#Enter the scores: 
#Score 1: 80
#Score 2: 89
#Score 3: 90
#Score 4: 98
#Score 5: 100
#Score 6: 100
#Total: 457 
#Average: 91  

#mgc-123-182:CS 280 Home$ python Dri_Torres_Project_4_Part_1.py 
#Enter the scores: 
#Score 1: 30
#Score 2: 32
#Score 3: 45
#Score 4: 47
#Score 5: 74
#Score 6: -1
#Total: 228 
#Average: 45 

