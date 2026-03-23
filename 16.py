class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def show(self):
        print("Student:",self.name,"Marks:",self.marks)
    def avg(self):
        print("Average:",sum(self.marks)/len(self.marks))
class Teacher:
    def __init__(self,name,subject):
        self.name=name
        self.subject=subject
    def show(self):
        print("Teacher:",self.name,"Subject:",self.subject)
    def teach(self):
        print(self.name,"is teaching",self.subject)
class Admin:
    def __init__(self,name):
        self.name=name
    def show(self):
        print("Admin:",self.name)
    def manage(self):
        print(self.name,"is managing attendance of students")
s=Student("Anil",[80,90,85])
t=Teacher("Ravi","Math")
a=Admin("Suresh")
s.show()
s.avg()
t.show()
t.teach()
a.show()
a.manage()
