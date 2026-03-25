#Check if a string is a palindrome.

t=input("enter the string: ")
rev=t[::-1]
if t==rev:
    print("its palindrome")
else:
    print("its not palindrome")
