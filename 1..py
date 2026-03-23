'''1. Write a program that takes two integers, computes their sum, difference, product, and 
division, checks if they’re even/odd, and converts one to a float.'''

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
sum=a+b
diff=a-b
prod=a*b
if b!=0:
    div=a/b
else:
    div="Undefined"
if a%2==0:
    print("First number is Even")
else:
    print("First number is Odd")
if b%2==0:
    print("Second number is Even")
else:
    print("Second number is Odd")
a_float=float(a)
print("Sum:",sum)
print("Difference:",diff)
print("Product:",prod)
print("Division:",div)
print("Float conversion:",a_float)
