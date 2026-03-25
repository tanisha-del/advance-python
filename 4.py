#Count vowels in a string.

s=input("enter the string : ")
vowels="AEIOUaeiou"
count=0
for i in s:
    if i in vowels:
        count=count+1
print("no of vowels: ",count)
