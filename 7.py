students={}
n=int(input("Enter number of students: "))
for i in range(n):
    name=input("Name: ")
    marks=list(map(int,input("Marks: ").split()))
    students[name]=marks
for name in students:
    students[name]=sum(students[name])/len(students[name])
top=max(students,key=students.get)
print("Averages:",students)
print("Topper:",top)
