￼def fibo2(par): 
	result = [ ]
	var1 = 0 var2 = 1
	while var2 < par:
	result = result + [var2]
	var3 = var1 + var2 var1 = var2
	var2 = var3
	return result

	finbo2(5)