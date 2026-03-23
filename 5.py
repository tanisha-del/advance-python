lst=["apple","madam","python","level","hi there"]
sorted_lst=sorted(lst,key=len)
pal=[x for x in lst if x==x[::-1]]
replaced=[x.replace(" ","-") for x in lst]
print(sorted_lst)
print(pal)
print(replaced)
