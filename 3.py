#Reverse a string (without slicing).

s= input("Enter a string: ")
reverse = " "
for i in s:
    reverse = i+reverse
print("Reversed string:", reverse)
