class Vehicle:
    count=0
    def rent(self,days):
        pass
class Car(Vehicle):
    def rent(self,days):
        Vehicle.count=Vehicle.count+1
        print("the rent money for car is: ",days*100)
class Bike(Vehicle):
    def rent(self,days):
        Vehicle.count+=1
        print("the rent money for bike is: ",days*50)
c=Car()
b=Bike()
c.rent(1)
b.rent(1)
print("total vehicle: ",Vehicle.count)
