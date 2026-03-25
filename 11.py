lst=[10,20,4,45,99]
largest=lst[0]
second=lst[0]
for i in lst:
    if i>largest:
        second=largest
        largest=i
    elif i>second and i!=largest:
        second=i
print(second)

