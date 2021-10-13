import math

while True:
    print ("\n Welcome")

    print ("+")
    print ("-")
    print ("*")
    print ("/")
    print ("sin")
    print ("cos")
    print ("tan")
    print ("cot")
    print ("log")

    print ("exit")

    print ("Please input your request: ")


    inp = input()

    if inp == 'exit':
        print ("bye")
        break
    
    elif inp == '+':
        x = int(input("a : "))
        y = int(input("b : "))        
        res = x + y

    elif inp == '-':
        x = int(input("a : "))
        y = int(input("b : "))
        res = x - y

    elif inp == '*':
        x = int(input("a : "))
        y = int(input("b : "))
        res = x * y

    elif inp == '/':
        x = int(input("a : "))
        y = int(input("b : "))
        if y == 0:
            res = 'Error , Because b should be != 0'
        else:
            res = x / y
    
    elif inp == 'sin':
        x = int(input("d : "))
        res = math.sin(math.radians((x)))

    elif inp == 'cos':
        x = int(input("d : "))
        res = math.cos(math.radians((x)))

    elif inp == 'tan':
        x = int(input("d : "))
        res = math.tan(math.radians((x)))

    elif inp == 'cot':
        x = int(input("d : "))
        res = math.atan(math.radians((x)))

    elif inp == 'log':
        x = int(input("x : "))
        res = math.log10(x)

    else:
        res = 'Can not found this request , try again'

    print ("Result is : " , res)