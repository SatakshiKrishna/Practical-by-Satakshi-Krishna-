# A Program to calculate the largest number among three number 
number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))
number3 = int(input("Enter your third number: "))

if (number1 >= number2)and(number1 >= number3):
    largest = number1
  
elif (number2 >= number1)and(number2 >= number3):
    largest = number2

else:
    largest = number3

print("The Largest Number is",largest)