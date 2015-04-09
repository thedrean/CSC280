#/**********************************************************************/ 
#/* CSC 280 – Extra Credit Pascal's Triangle							*/ 
#/* 																	*/ 
#/* modifier: Dri Torres 												*/ 
#/* 																	*/ 
#/* filename: Dri_Torres_Project_9.py 									*/ 
#/* modified from: CSC 280 Prog Progect #9								*/ 
#/* date last modified: 11-03-2013 										*/ 
#/* 																	*/ 
#/* action: Creates recursive and iterative versions of prodicing,  	*/
#/*	Pascal's Triangle													*/
#/*     																*/
#/* 																	*/ 
#/* input: number for rows of Pascal's triangle as prompted by user		*/
#/* 																	*/ 
#/*																		*/
#/* output: Pascal's Triangle with the amount of rows prompted by user	*/
#/* both iteratively and recursively  									 */
#/**********************************************************************/


#Defines iterative function for pascals triangle

def tri(x):
	trilist = [[1]]
	for i in range(1, x):
		new = [1]
		for v in range(0,i-1):
			new.append(trilist[i-1][v]+trilist[i-1][v+1])

		new.append(1)
		trilist.append(new)
	return trilist

#Defines recursive version of pascal's triangle

def trirecursive(x):
	trilist = [[1]]
	if x < 0:
		return " "
	elif x == 1:
		return trilist
	else:
		new = [1]
		final = trirecursive(x-1)
		bottom = final[-1]
		for t in range(len(bottom)-1):
			new.append(bottom[t] + bottom[t+1])

		new = new + [1]
		final.append(new)
	return final

def main():

	a = int(raw_input("give me number for pascal's triangle: "))
	#tri = tri(a)
	
	for i in tri(a):
		print " " * (a*2), i 

		a-= 1


	a = int(raw_input("give me number for racursive pascals triangle: "))

	#trirecursive = trirecursive(a)
	for i in trirecursive(a):
		print " " * (a * 2), i

		a -= 1

#main()

def newmain():
	x = 10
	y = trirecursive(x)
	print y

newmain()



#x = 5
#y = range(x)

#for i in y:
#	print i 