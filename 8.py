contacts={}
while True:
    print("1 Add 2 Search 3 Delete 4 List 5 Exit")
    ch=input()
    if ch=="1":
        name=input("Name: ")
        phone=input("Phone: ")
        contacts[name]=phone
    elif ch=="2":
        name=input("Name: ")
        if name in contacts:
            print(contacts[name])
        else:
            print("Not found")
    elif ch=="3":
        name=input("Name: ")
        if name in contacts:
            del contacts[name]
        else:
            print("Not found")
    elif ch=="4":
        for k,v in contacts.items():
            print(k,v)
    else:
        break
