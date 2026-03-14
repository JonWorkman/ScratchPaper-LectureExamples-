operation = 0
while operation != 5:
    #simple calculator menu
    print("*** Simple Calc ***")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print()

    #get input for choice of operation
    #get initial input
    operation = int(input("What operation do you want to do?: "))
    #check the input
    while operation < 1 or operation > 5:
        print("Sorry, I didn't quite get that.")
        operation = int(input("What operation do you want to do?: "))
    print()

    #Beak the program
    if operation == 5:
        print("Well, ok then, bye, I guess")
        break

    #get input for numbers
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print()

    #do math
    output = 0
    op = ""

    if operation == 1:
        #print(num1, "+", num2, "=", num1 + num2)
        output = num1 + num2
        op = "+"
    elif operation == 2:
        #print(num1, "-", num2, "=", num1 - num2)
        output = num1 - num2
        op = "/"
    elif operation == 3:
        #print(num1, "x", num2, "=", num1 * num2)
        output = num1 * num2
        op = "x"
    elif operation == 4:
        #print(num1, "/", num2, "=", num1 / num2)
        output = num1 / num2
        op = "/"
    else:
        print("Sorry, I didn't quite get that.")
    #print results
    print(num1, op, num2, "=", output)
    print()
    print()