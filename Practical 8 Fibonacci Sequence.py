# A Program to display the Fibonacci sequence up to n-th term

NumberofTerms = int(input("How Many Terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if NumberofTerms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif NumberofTerms == 1:
   print("Fibonacci sequence upto",NumberofTerms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < NumberofTerms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1