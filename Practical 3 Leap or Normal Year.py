# A Proram to check if year is lea or normal

Year = int(input("Enter year: "))

if (Year % 4)== 0:
    if (Year % 100)== 0:
        if (Year % 400)== 0:
            print(Year,"is a leap year")
        else:
            print(Year,"is not a leap year")
    else:
     print(Year,"is a leap year")
else:
    print(Year,"is not a leap year")