# A Program to display the multipication table 
number = int(input("Enter the number : "))

print("Multiplication Table of", number)
for i in range(0, 11):
   print(number,"X",i,"=",number * i) 