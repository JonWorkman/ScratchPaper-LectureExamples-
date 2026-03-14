#simple calculator menu
print("*** Simple Calc ***")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print()

#get input for choice of operation
operation = int(input("What operation do you want to do?: "))
print()

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
    print("Sorry, I didn't quite get that")
#print results
print(num1, op, num2, "=", output)