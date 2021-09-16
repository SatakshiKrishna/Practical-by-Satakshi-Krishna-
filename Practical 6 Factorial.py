# A Program to display the factorial of any number

Num = int(input("Enter your number "))
Factorial = 1
if Num < 0:
    print("Factorial does not exist for negative numbers")
elif Num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, Num + 1):
        Factorial = Factorial * i
    print("The factorial of",Num,"is",Factorial)