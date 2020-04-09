#pickle is a module in python which is use for read content in obj and store it in file 

import pickle

#define class of Employee
class Employee:
    def __init__(self,eno,ename,esal,eadd):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eadd=eadd
    
    #to display details of employee
    def display(self):
        print("Employee no.:",self.eno)
        print("Employee name:",self.ename)
        print("Employee salary:",self.esal)
        print("Employee address:",self.eadd)

#open dat file of name emp in write binary mode with instance in f
#if we open it by 'with' then we dont need to close it 
with open("emp.dat","wb") as f:
    #object of class
    e=Employee("1","ketan","1000","Dhule")
    #dump function stores binary data of object in file 
    pickle.dump(e,f)
    print("pickling is done.")

#open same file now in read mode   
with open("emp.dat","rb") as f:
    #create different object to store binary data of object stored in file
    obj=pickle.load(f)
    print("unpickling is done")
    obj.display()
    #lets print the content of obj 
    print(obj)

#### OUTPUT ####
#pickling is done.
#unpickling is done
#Employee no.: 1
#Employee name: ketan
#Employee salary: 1000
#Employee address: Dhule
#<__main__.Employee object at 0x000001E758C87910>