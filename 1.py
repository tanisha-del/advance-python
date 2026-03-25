n = int(input("How many numbers: "))
largest = 0
for i in range(n):
    num = int(input("Enter number: "))
    if num > largest:
        largest = num
print("Largest:", largest)
