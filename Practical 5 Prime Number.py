# A Program to find the prime number

Number= int(input("Enter Number: "))

if Number > 1:
    for i in range(2,Number):
        if (Number%i) == 0:
            print(Number,"is not a prime number")
            print(i,"times",Number//i,Number)
            break
    else:
        print(Number,"is a prime number")
else:
    print(Number,"is not a prime number")