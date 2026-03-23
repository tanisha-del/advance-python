records=[]
n=int(input("Enter number of students: "))
for i in range(n):
    name=input("Name: ")
    roll=input("Roll: ")
    marks=int(input("Marks: "))
    records.append({"name":name,"roll":roll,"marks":marks})
for r in records:
    if r["marks"]>=40:
        print(r["name"],"Pass")
    else:
        print(r["name"],"Fail")
