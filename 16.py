lst=[1,2,3,4,5]
k=2
res=[]
for i in range(k,len(lst)):
    res.append(lst[i])
for i in range(0,k):
    res.append(lst[i])
print(res)
