lst = []
n = int(input("Enter number of elements: "))
for i in range(n):
    num = int(input("enter the numbers: "))
    lst.append(num)
minimum=lst[0]
maximum=lst[0]
for i in lst:
    if i<minimum:
        minimum=i
    if i>maximum:
        maximum=i
print("Minimum:", minimum)
print("Maximum:", maximum)
