def power(base,exp):
    result=1
    for i in range(exp):
        result*=base
    return result
b=int(input("Enter base: "))
e=int(input("Enter exponent: "))
print(power(b,e))
