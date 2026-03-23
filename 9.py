emp={}
while True:
    print("1.Add 2.Remove 3.Display 4.Exit")
    ch=input()
    if ch=="1":
        name=input("Name: ")
        emp[name]="Present"
    elif ch=="2":
        name=input("Name: ")
        emp.pop(name,"Not found")
    elif ch=="3":
        print(emp)
    else:
        break
