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
		print "max = " +str(t)+ " "
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