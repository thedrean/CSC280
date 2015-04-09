#/**********************************************************************/
#/* CSC 280 Programming Project 2 Part 1                                         */
#/*                                                                                                      */
#/* modifier:       Dri Torres                                                                */
#/*                                                                                                      */
#/* filename: Part_2_Assignment_2.py                                              */
# /* modified from: CSC 280 HW #2 lab                                              */
#/* date last modified: 09/29/2013                                                   */
#/*                                                                                                      */
#/* action: computes whether specified age is of the pegal limit to drive,*/
#/*  vote, drink, rent a car, retire, and collect Social Security             */
#/* input: the circles's radius, entered by the                                     */
#/*                                                                                                      */
#/*                                                                                                      */
#/* output: Y for "yes" or N for "no" answering all questions age       */
#/*                                                                                                      */
#/**********************************************************************/

# Promt user for subject's age

x = int(raw_input("Enter the subject's age now: "))

#Conditional block 

if x >= 15:
    print "Is subject old enough to drive? \t Y"
else:
    print "Is subject old enough to drive? \t N"
if x >= 18:
    print "Is the subject old enough to vote? \t Y"
else:
    print "Is the subject old enough to vote? \t N"
if x >= 21:
    print "Is the subject old enough to drink? \t Y"
else:
    print "Is the subject old enough to drink? \t N"
if x >= 25:
    print "Is the subject old enough to rent a car? \t Y"
else:
    print "Is the subject old enough to rent a car? \t N"
if x >= 50:
    print "Is the subject old enough to retire? \t Y"
else:
    print "Is the subject old enough to collect SS? \t N"
if x >= 65:
    print "Is the subject old enough to collect SS? \t Y"
else:
    print "Is the subject old enough to collect SS? \t N"

# Enter the subject's age now: 12
# Is subject old enough to drive? 	 N
# Is the subject old enough to vote? 	 N
# Is the subject old enough to drink? 	 N
# Is the subject old enough to rent a car? 	 N
# Is the subject old enough to collect SS? 	 N
# Is the subject old enough to collect SS? 	 N

# Enter the subject's age now: 15
# Is subject old enough to drive? 	 Y
# Is the subject old enough to vote? 	 N
# Is the subject old enough to drink? 	 N
# Is the subject old enough to rent a car? 	 N
# Is the subject old enough to collect SS? 	 N
# Is the subject old enough to collect SS? 	 N

# Enter the subject's age now: 51
# Is subject old enough to drive? 	 Y
# Is the subject old enough to vote? 	 Y
# Is the subject old enough to drink? 	 Y
# Is the subject old enough to rent a car? 	 Y
# Is the subject old enough to retire? 	 Y
# Is the subject old enough to collect SS? 	 N

# Is subject old enough to drive? 	 Y
# Is the subject old enough to vote? 	 Y
# Is the subject old enough to drink? 	 Y
# Is the subject old enough to rent a car? 	 Y
# Is the subject old enough to retire? 	 Y
# Is the subject old enough to collect SS? 	 Y
