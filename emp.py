from validations import *
import sys
class Employee:
    empdict={}
    def __init__(self,i,nm,sal,a,g,ad,c,doj,dob,dpn,des,pan,aadhar):
        self.id=i
        self.name=nm
        self.salary=sal
        self.age=a
        self.gender=g
        self.address=ad
        self.city=c
        self.DOJ=doj
        self.DOB=dob
        self.dept=dpn
        self.designation=des
        self.pancard=pan
        self.aadharcard=aadhar
        if self.dept in self.empdict.keys():
            self.empdict[self.dept].append(self.name)
        else:
            self.empdict[self.dept]=[self.name]
    def display(self):
            print(self.id,"",self.name,"",self.salary,"",self.age,"",self.gender,"",self.address,"",self.city,"",self.DOJ,"",self.DOB,"",self.dept,"",self.designation,"",self.pancard,"",self.aadharcard)

emplist=[]
while(1):
    print("press 1 to insert employee records")
    print("press 2 to display all employee records")
    print("press 3 to update employee records")
    print("press 4 to search the details of employee")
    print("press 5 to delete employee record")
    print("press 6 to display details of Employee with max salary")
    print("press 7 to quit")
    ch=int(input('enter your choice:'))
    if ch==1:
        while True:
            i=input('enter your employee id:')
            if (isEmpidValid(i)):
                break
            else:
                print("Invalid EmpId ")
        while True:
            nm=input('enter your name:')
            if (isNameValid(nm)):
                break
            else:
                print("Invalid Emp Name")
        while True:
            sal=input('enter your salary:')
            if (isSalValid(sal)):
                break
            else:
                print("Invalid Salary")
        while True:
            a=input('enter your age:')
            if (isAgeValid(a)):
                break
            else:
                print("Invalid Age")
        while True:
            g=input('enter your gender(male/female):')
            if g=='male' or g=='female':
                break
            else:
                print('please enter valid gender')
        ad=input('enter your address:')
        c=input('enter your city:')
        doj=input('enter your doj')
        while True:
            dob=input('enter your dob')
            if (isDobValid(dob)):
                break
            else:
                print("Invalid Date Of Birth")
        dpn=input('enter your department name:')
        des=input('enter your designation:')
        while True:
            pan=input('enter your pan card number:')
            if (isPanValid(pan)):
                break
            else:
                print("Invalid Pan Number")
        while True:
            aadhar=input('enter your aadhar number:')
            if (isAdharValid(aadhar)):
                break
            else:
                print("Invalid Aadhar Number")
        em=Employee(i,nm,sal,a,g,ad,c,doj,dob,dpn,des,pan,aadhar)        
        emplist.append(em)
    elif ch==2:
        for i in emplist:
            i.display()
    elif ch==3:
        print('press A to update name of employee:')
        print('Press B to update employee address:')
        print('press C to update salary of employee:')
        print('press D to update date of birth of employee:')
        ch2=input('enter your choice:')
        if ch2=='A':
                empid=input('enter employee id:')
                for i in emplist:
                    if i.id==empid:
                        name=input('enter name:')
                        i.name=name
                        i.display()
        elif ch2=='B':
                empid=input('enter employee id')
                for i in emplist:
                    if i.id==empid:
                        ad=input('enter new address:')
                        i.address=ad
                        i.display()
        elif ch2=='C':
            print('press i to update salary of specific employee by empid')
            print('press ii to update salary of all employees working in a department')
            print('press iii to update salary of all employees')
            ch3=input('enter your choice:')
            if ch3=='i':
                    empid=input('enter employee id:')
                    for i in emplist:
                        if i.id==empid:
                            new_sal=int(input('enter updated salary:'))
                            i.salary=new_sal
                            i.display()
            elif ch3=='ii':
                dep=input('enter department of employee:')
                for i in emplist:
                    if i.dept==dep:
                        new_sal=input('enter updated salary:')
                        i.salary=new_sal
                        i.display()
            elif ch3=='iii':
                for i in emplist:
                    new_salary=int(input('enter new salary:'))
                    i.salary=new_salary
        elif ch2=='D':
            empid=input('enter employee id')
            for i in emplist:
                if i.id==empid:
                    new_date=input('enter new date of birth:')
                    i.DOB=new_date
                    i.display()
    elif ch==4:
        print('press P to search by employee id')
        print('press Q to search by employee name')
        print('press R to search by employee department')
        ch4=input('enter your choice:')
        if ch4=='P':
            empid=input('enter employee id:')
            for i in emplist:
                if i.id==empid:
                    i.display()
        if ch4=='Q':
            name=input('enter name of employee:')
            for i in emplist:
                if i.name==name:
                    i.display()
        if ch4=='R':
            dep=input('enter department name:')
            for i in emplist:
                if i.dept==dep:
                    i.display()
    elif ch==5:
        empid=input('enter employee id:')
        for i in emplist:
            if i.id==empid:
                emplist.remove(i)
    elif ch==6:
        max=0
        for i in emplist:
            a=int(i.salary)
        if a > max:
            max=a
            i.display()
    elif ch==7:
        sys.exit()
