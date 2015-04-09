def multiplylists(a1, y):
	total = a1
	i = 0
	while i < (y-1):
		storedlist = a1
		total = total + storedlist
		i = i + 1
	return total

def main():
	datlist = [1, 2, 3, 4, 5]
	y = int(raw_input("enter integer: "))
	z = multiplylists(datlist,y)
	print z

#main()


def test(x):
	i = 0
	while i < x:
		print "bomb diggity"
		i += 1

def main():
	z = 10
	test(z)
	
main()


        
            
