#Find the sum of digits of a number.

n=int(input("Enter a digit: "))
sum=0
while n>0:
    sum=sum+n%10
    n=n//10
print("Sum:", sum)
