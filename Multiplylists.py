a1 = [1, 2, 3, 4, 5]
y = int(raw_input("enter integer: "))

def multiplylists(y, a1):
    a2 = [x * y for x in a1]
    print a2

def main():
    z = multiplylists(y, a1)
    print z

main()





    
