#/**********************************************************************/ 
#/* CSC 280 – Programming Project 5 									*/ 
#/* 																	*/ 
#/* modifier: Dri Torres 												*/ 
#/* 																	*/ 
#/* filename: Dri_Torres_Project_5.py 									*/ 
#/* modified from: CSC 280 Prog Progect #4 								*/ 
#/* date last modified: 10-24q-2013 										*/ 
#/* 																	*/ 
#/* action: Computes a 15% annual increase of tuition between user  	*/
#/* specified date in years. The program terminates when 0 is entered at*/
#/* any time for any input.												*/
#/* 																	*/ 
#/* input: Initial tuition, the current year, and the target year 		*/
#/* 																	*/
#/*																		*/
#/* output: The new predicted tuition with 15% yearly compounded 		*/
#/* increase        							                        */
#/**********************************************************************/



#Defines function Tuition which computes a %15 yearly compounded increase in initian tuition

def Tuition(current, thisYear, targetYear):
    difference = targetYear - thisYear
    Tuition = current *(1.15 ** difference)

    print "In "+str(thisYear)+ " tuition will be $" +str(Tuition)+ "."


#Defines the main function which prompts user for current year, initial tuition, and targeted year.
def main():

	print "Tuition predictions at 15% annual increase"
	print "At the ?, enter a tuition, the current year, and the target year. Enter zero in any field to quit."
	current = 1
	thisYear = 1
	targetYear = 1

#Ensures the program will terminate if the value 0 is enteres at any time

	while current > 0 and thisYear > 0 and targetYear > 0:

		current = float(raw_input("Enter the current tuition: "))
		if current == 0:
			break
		thisYear = int(raw_input("Enter the current year: ")) 	
		if thisYear == 0:
			break
 		targetYear = int(raw_input("Enter the target year: "))
 		if targetYear == 0:
 			break
# Invokes Tuition function when all variables are above 0 in input value
 		
 		else:
 			Tuition(current, thisYear, targetYear)

 		

# Invokes main function        			

main ()

#mgc-122-150:CS 280 Home$ python Dri_Torres_Project_5.py 
#Enter the current tuition: 4500
#Enter the current year: 2013
#Enter the target year: 2017
#In 4500.0 tuition will be $7870.528125.
#Enter the current tuition: 2000
#Enter the current year: 2013
#Enter the target year: 2019
#In 2000.0 tuition will be $4626.12153125.
#Enter the current tuition: 12000
#Enter the current year: 2013
#Enter the target year: 2027
#In 12000.0 tuition will be $84908.4691739.
#Enter the current tuition: 0
#mgc-122-150:CS 280 Home$ 
        
        


                    
