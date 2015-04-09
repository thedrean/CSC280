
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
#defines function ShoppingList, which establishes the list.

def ShoppingList():
	shoppinglist = []
	newitem = raw_input("New item: ")
	while newitem != "":
		shoppinglist.append(newitem)
		newitem = raw_input("New item: ")
	return shoppinglist

#defines function SortShoppingList which sorts the list alphabetically.

def SortShoppingList(shoppinglist):
	for j in range (len(shoppinglist)-1, 0, -1):
		for i in range(j):
			if shoppinglist[i] > shoppinglist[i + 1]:
				swap = shoppinglist[i]
				shoppinglist[i] = shoppinglist[i + 1]
				shoppinglist[i + 1] = swap

	return shoppinglist

#Defines function StripShoppingList, which returns a list of one of each item.	

def StripShoppingList(shoppinglist):
	strippedlist = []
	
	for j in shoppinglist:
		if j not in strippedlist:

			strippedlist.append(j)

	
	return strippedlist

#Defines function ReportShoppingList, which prints the sorted shoppinlist, the stripped list, and the number of instances of each item in the list.	

def ReportShoppingList(shoppinglist, strippedList):
	
	print "My sorted shopping list is: " +str(shoppinglist)+ " "
	print "My stripped list is " +str(strippedList)+ " "

	for j in range(len(strippedList)):

		instances = shoppinglist.count(strippedList[j])

		
		if instances == 1:
			instances = "one"
		elif instances == 2:
			instances = "two"
		else:
			instances = "three"

		print "The item " +str(strippedList[j])+ " has " +str(instances)+ " instences in my list."

#Defines the main which invokes all of the preciously defined functions.

def main ():
	shoppinglist = ShoppingList()

	sortedlist = SortShoppingList(shoppinglist)

	

	strippedList = StripShoppingList(sortedlist)


	ReportShoppingList(sortedlist, strippedList)

#Runs the main function	

main()

#New item: A box of milk
#New item: Turkey
#New item: Orange
#New item: Banana
#New item: Spaghetti
#New item: Potatoes
#New item: Lasagna
#New item: Juice
#New item: Banana
#New item: Banana
#New item: Zucchini bread
#New item: Turkey 
#New item: Apple
#New item: Potatoes
#New item: Zucchini bread
#New item: 
#My sorted shopping list is: ['A box of milk', 'Apple', 'Banana', 'Banana', 'Banana', 'Juice', 'Lasagna', 'Orange', 'Potatoes', 'Potatoes', 'Spaghetti', 'Turkey', 'Turkey', 'Zucchini bread', 'Zucchini bread'] 
#My stripped list is ['A box of milk', 'Apple', 'Banana', 'Juice', 'Lasagna', 'Orange', 'Potatoes', 'Spaghetti', 'Turkey', 'Zucchini bread'] 
#The item A box of milk has one instences in my list.
#The item Apple has one instences in my list.
#The item Banana has three instences in my list.
#The item Juice has one instences in my list.
#The item Lasagna has one instences in my list.
#The item Orange has one instences in my list.
#The item Potatoes has two instences in my list.
#The item Spaghetti has one instences in my list.
#The item Turkey has two instences in my list.
#The item Zucchini bread has two instences in my list.



	