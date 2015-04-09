#list1 = [1, 2, 3, 2]

#list1.append([4, 5])
#print list1

#print list1.count(2)

#list1.extend([4,5])
#print list1

#list1.index(3)
#print list1
#list1.insert(5, 9)

#print list1.remove(1)

#print list1.reverse(list1)






def passbyref(refpasslist):
	print "passing parameters by reference"
	refpasslist.append([1, 2, 3, 4])
	print "reflist inside the function:" +str(refpasslist)+ " "

#main1()

def main2():
	reflist = [4, 3, 2, 1]
	passbyref(reflist)
	#print "reflist outside the function:" +str(reflist)+ " "

main2()
   

####

def passbyref(refpasslist):
	print "passing parameter by value"
	refpasslist = [1, 2, 3, 4]
	print "reflist inside the function" +str(refpasslist)+ " "

def main4():
	reflist = [4, 3, 2, 1]
	passbyref(reflist)
	print "reflist outside the function:" +str(reflist)+ " "



















main4()

for letter in 'Computer Science is Fun':
	if letter == ' ':
		break
	#print "Current Letter: " +str(letter)+ " "






















#import turtle
#from turtle import left as l, right as r, fd, color, speed, setheading


#def snake(n):
#    size = 400/(2**n-1)
#    turtle.clear()
#    turtle.color("Blue")
#    turtle.speed(1000)
#    turtle.setheading(0)
#    turtle.penup()
#    turtle.setposition(-300,300)
#    turtle.pendown()
#    m((n,size,90))

#def m(t):
#    (lv,s,a)=t
#    a=[(r,a),(m,(lv-1, s, -a)),(fd,s),(l,a),(m,(lv-1,s, a)),(fd,s)]
#    if lv:
#        for (f,p) in a + list(reversed(a[0:-1])):
#            f(p)
#
#def main():
#	a = m(t)
#	print a
#
#main()