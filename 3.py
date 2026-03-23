t=(1,"a",5,8.5,12,"b")
nums=tuple(x for x in t if isinstance(x,(int,float)))
print("Numeric values:",nums)
try:
    t[0]=100
except TypeError:
    print("Tuple cannot be modified")
t1=(1,2,3)
t2=(4,5,6)
t3=t1+t2
print("Concatenated tuple:",t3)
