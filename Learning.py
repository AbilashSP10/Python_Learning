# gender=input('enter the gender:')
# if(gender=='boy'):
#     print('you are a boy')
# elif(gender=='girl'):
#     print('you are a girl')
# else:
#     print('invalid gender')

# a = int(input('Enter the number you want to check: '))
# if(a%2==0):
#     print("The entered number is even")
# else:
#     print("The entered number is odd")

# a = int(input('enter the number you want to check: '))
# if(a%3==0 and a%4==0):
#     print('The entered number is divided by 4 and 3')
# elif(a%3==0):
#     print('The entered number is divided by 3')
# elif(a%4==0):
#     print('The entered number is divided by 4')
# else:
#     print('The entered number cannot be divided by 3 and 4')

# Uage = int(input('Enter your age: '))
# if(Uage<=10):
#     print('You are child')
# elif(Uage>10 and Uage<=18):
#     print('You are Minor')
# else:
#     print('You are Major')

# Uage = int(input('Enter your age: '))
# if(Uage<=10):
#     print('You are child')
# elif(10 < Uage <=18):
#     print('You are Minor')
# else:
#     print('You are Major')

# V1=int(input('Enter the first value of the triangle: '))
# V2=int(input('Enter the second value of the triangle: '))
# V3=int(input('Enter the third value of the triangle: '))
# if(V1==V2==V3):
#     print('This is equilateral triangle')
# else:
#     print('This is a normal triangle')

# V1=int(input('Enter the first number: '))
# V2=int(input('Enter the second number: '))
# V3=input('Enter the operation to perform: ')

# if(V3=='+' or V3=='sum'):
#     print(V1 + V2)
# elif(V3=='-' or V3=='sub'):
#     print(V1 - V2)
# elif(V3=='*' or V3=='mul'):
#     print(V1 * V2)
# elif(V3=='/' or V3=='div'):
#     print(V1 / V2)
# else:
#     print('You have entered wrong choice')

# V1=int(input('Enter the starting number: '))
# V2=int(input('Enter the ending number: '))
# V3=int(input('Enter the limit: '))

# for i in range (V1,V2,V3):
#     print(i)

# for i in range(1,31):
#     if(i%3==0):
#         print(i)

# V1='*'
# for i in range(1,6):    
#     print(i*V1)

# V1=int(input('''Enter which number's multiplication table you wish to display: '''))

# for i in range(1,11):
#     print(i, '*', V1, '=', i*V1)

# sum=0
# for i in range (1,31,2):      
#     sum+=i
# print(sum)

# i=10
# while i>=0:
#     print(i,end=', ')
#     i-=1

# i=10
# while i<=200:
#     print(i, end=', ')
#     i+=10

# V1=int(input('Enter the number you want to find the Factorial: '))
# F=1

# while V1>=1:    
#     F*=V1    
#     V1-=1
# print(F)

# while True:
#     x=int(input('Enter a number '))
#     if x==0:
#         break

# Log=1
# Reg=2
# Das=3
# Ext=4

# while True:
#     print('1] Login')
#     print('2] Register')
#     print('3] Dashboard')
#     print('4] Exit')
#     V1=int(input('Enter your choice: '))
#     if V1==1:
#         VL1=input('Enter your name: ')
#         VL2=input('Enter your email: ')       
#         #print('Hello', VL1, 'your login is successful')
#         print(f"Hello {VL1} Welcome and your email is {VL2}")        
#         break
#     elif V1==2:
#         VR1=input('Enter your name: ')
#         VR2=input('Enter your email: ')
#         VR3=input('Enter a password: ')
#         print('Hello', VR1 ,'your registration is successfull')
#         break
#     elif V1==3:
#         print('Site Information')
#         print('Dashboard')
#         print('Contact US')
#         print('Go back to home page')
#         break
#     elif V1==4:
#         print('Thank you for visiting')
#     else:
#         print('You entered a wrong choice')
#         break


# def addi(V1, V2):
#     V3 = V1 + V2
#     return V3

# def subt(V1, V2):
#     V3 = V1 - V2
#     return V3

# def divi(V1, V2):
#     V3 = V1/V2
#     return V3

# def mult(V1, V2):
#     V3 = V1*V2
#     return V3

# def modul(V1, V2):
#     V3 = V1%V2
#     return V3

# V1=int(input('Enter the first number: '))
# V2=int(input('Enter the second number: '))
# opr=(input('Enter which operation you would like to perform [+, -, /, *, %]: '))

# if opr == '+':
#     print(f"Addition of {V1} and {V2} gives:", addi(V1, V2))
# elif opr == '-':
#     print(f"Subtraction of {V1} and {V2} gives:", subt(V1, V2))
# elif opr == '*':
#     print(f"Multiplication of {V1} and {V2} gives:", mult(V1, V2))
# elif opr == '/':
#     print(f"Division of {V1} and {V2} gives:", divi(V1, V2))
# elif opr == '%':
#     print(f"Modulus of {V1} and {V2} returns:", modul(V1, V2))
# else:
#     print('You have entered a wrong operation')

# class Car:
#     no_of_wheels=4
#     mileage=20
#     car_make='BMW'

# obj=Car()

# print(obj.no_of_wheels)
# print(obj.mileage)
# print(obj.car_make)

# obj.car_make=input('Enter your Car Make: ')
# print(obj.car_make)

# class BankDetails:
#     Acc_Name='Krishnan'
#     Acc_Number=98765898650
#     Acc_Balance=5000

# obj=BankDetails()

# print(obj.Acc_Name)
# print(obj.Acc_Number)
# print(obj.Acc_Balance)

# obj.Acc_Name=input('Enter the Account holder name: ')
# obj.Acc_Number=int(input('Enter your Account Number: '))
# obj.Acc_Balance=int(input('Enter your Account Balance: '))

# print(obj.Acc_Name)
# print(obj.Acc_Number)
# print(obj.Acc_Balance)

# class Car:
#     def __init__(self,number_of_wheels):
#         self.number_of_wheels=number_of_wheels
#         print(self.number_of_wheels)

# number_of_wheels=int(input('Enter the number of Wheels: '))
# obj=Car(number_of_wheels)
# obj

# class Calct:

#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         print('This is constructor', a+b)

#     def __del__(self):        
#         # print('This is destructor', self.a, self.b, self)
#         print('This is destructor', self)

#     def __str__(self):        
#         return f"First value: {self.a} and Second value: {self.b}"

# a=int(input('Enter the First value: '))
# b=int(input('Enter the Second value: '))

# obj = Calct(a,b)    

# print(f"{a} and {b}")
# print('This is a test message')

# class Students:

#     def __init__(self,sname,M1,M2,M3,M4,M5):
#         self.sname=sname
#         self.M1=M1
#         self.M2=M2
#         self.M3=M3
#         self.M4=M4
#         self.M5=M5
    
#     def Details(self):    
#         print(f"Student Name is: {self.sname}")
#         print(f"Marks got for first subject: {self.M1}")
#         print(f"Marks got for second subject: {self.M2}")
#         print(f"Marks got for third subject: {self.M3}")
#         print(f"Marks got for fourth subject: {self.M4}")
#         print(f"Marks got for fifth subject: {self.M5}")

#     def Avrg(self):
#         A=(self.M1+self.M2+self.M3+self.M4+self.M5)/5
#         print(f"Average Marks are: {A}")

#     def __del__(self):
#         print('Initialising destructor',self.sname)

#     def __str__(self):
#        return self.sname

# sname=input("Enter your Full Name: ")
# M1=int(input("Enter the Mark got for the first Subject: "))
# M2=int(input("Enter the Mark got for the second Subject: "))
# M3=int(input("Enter the Mark got for the third Subject: "))
# M4=int(input("Enter the Mark got for the fourth Subject: "))
# M5=int(input("Enter the Mark got for the fifth Subject: "))

# obj=Students(sname,M1,M2,M3,M4,M5)
# obj.Details()
# obj.Avrg()


# class Hospital:

#     def __init__(self,sname,Temp,Bdyp,tirness):
#         self.sname=sname
#         self.Temp=Temp
#         self.Bdyp=Bdyp
#         self.tirness=tirness

#     def Pdetails(self):
#         print(f"Your name is: {self.sname}")
#         print(f"Your Temperature is: {self.Temp}")
#         print(f"You have Body Pain: {self.Bdyp}")
#         print(f"You have Tiredness: {self.tirness}")

#     def Sick(self):
#         if (self.Temp>99) or (self.Bdyp=='Y') and (self.tirness=='Y'):
#             print(f"Hi {self.sname} you have fever")
#         else:
#             print(f"Hi {self.sname} you don't have fever")

#     def __del__(self):
#         print(f"Record for {self.sname} is deleted")

#     def __str__(self):
#         return self.sname
    
# sname=input('Enter your name: ')
# Temp=int(input('Enter the current reading of your Temperature in digits: '))
# Bdyp=input('''Enter Y if you have body pain and N if you don't have body pain: ''')
# tirness=input('''Enter Y if you have tiredness and N if you don't have tiredness: ''')

# hsptl=Hospital(sname,Temp,Bdyp,tirness)
# hsptl.Pdetails()
# hsptl.Sick()


# class Actor:

#   def Vote(self):

#     print("Name the two Actors who you want to do Voting")

#     ActO=input("Enter the First Actor Name: ")
#     ActT=input("Enter the Second Actor Name: ")

#     CountAO=0
#     CountBT=0

#     while True:
      
#       print(f"Enter A for {ActO} and B for {ActT}")
#       C=input("Enter your choice: ")

#       if C=='A' or C=='a':
#         CountAO+=1        
#         print("If you wish to continue voting Press Y else N")
#         VA=input("Enter Y/N: ")
#         if VA=='Y' or VA=='y':
#           print("Voting continuing")
#           continue
#         else:
#           print("Voting closed")
#           break

#       elif C=='B' or C=='b':
#         CountBT+=1
#         print("If you wish to continue voting Press Y else N")
#         VA=input("Enter Y/N: ")
#         if VA=='Y' or VA=='y':
#           print("Voting continuing")
#           continue
#         else:
#           print("Voting closed")
#           break

#       else:
#         print("Wrong choice")
#         break
    
#     print(f"{ActO} got {CountAO} votes and {ActT} got {CountBT} votes")    

# Voting=Actor()
# Voting.Vote()
      

# class StudentDetails:

#     def __init__(self,sname,Rno,M1,M2,M3,M4,M5):
#         self.sname=sname
#         self.Rno=Rno
#         self.M1=M1
#         self.M2=M2
#         self.M3=M3
#         self.M4=M4
#         self.M5=M5

#     def DispDetails(self):
#         print(f"\n{self.sname} Please see your result below:")
#         print(f"Name: {self.sname}")
#         print(f"Roll Number: {self.Rno}")
#         print(f"Marks for the 5 subjects are: {self.M1}, {self.M2}, {self.M3}, {self.M4}, {self.M5}")

#     def MrkAvg(self):
#         Avg=(self.M1 + self.M2 + self.M3 + self.M4 + self.M5)/5
#         return Avg
        

#     def TotMrk(self):
#         Tot=(self.M1 + self.M2 + self.M3 + self.M4 + self.M5)
#         print(f"{self.sname} your total marks are {Tot}")

# class Result(StudentDetails):
    
    
#     def __init__(self, sname, Rno, M1, M2, M3, M4, M5):
#         super().__init__(sname, Rno, M1, M2, M3, M4, M5)   
    

#     def Grade(self):
#       C=super().MrkAvg()
#       if C >80:
#         print(f"{self.sname} you have got distinction\n")

#       elif C>60 and C<80:
#          print(f"{self.sname} you have got First Class\n")

#       elif C>50 and C<60:
#          print(f"{self.sname} you have got Second Class\n")

#       elif C>40 and C<50:
#          print(f"{self.sname} you have got Third Class\n")

#       elif C<40:
#          print(f"{self.sname} you have failed\n")
        
#       else:
#         print(f"{self.sname} your result is withheld\n")
            

# sname=input("Enter your Name: ")
# Rno=int(input("Enter your Roll Number: "))
# M1=int(input("Enter your First Mark: "))
# M2=int(input("Enter your Second Mark: "))
# M3=int(input("Enter your Third Mark: "))
# M4=int(input("Enter your Fourth Mark: "))
# M5=int(input("Enter your Fifth Mark: "))

# StudDtls=Result(sname,Rno,M1,M2,M3,M4,M5)
# StudDtls.DispDetails()
# StudDtls.Grade()
# StudDtls

# class Sickdtls():
    
#     def __init__(self,pname,Temp,BdyPn,CouCol):
#         self.pname=pname
#         self.Temp=Temp
#         self.BdyPn=BdyPn
#         self.CouCol=CouCol
        
#     def DispDetls(self):
#       print(f"You have entered the details below: ")
#       print(f"Your Name: {self.pname}")
#       print(f"Temperature: {self.Temp}")
#       print(f"Body Pain: {self.BdyPn}")
#       print(f"Cough or Cold: {self.CouCol}")

# class SickOrNo(Sickdtls):
   
#    def __init__(self,pname,Temp,Bdypn,CouCol):
#       super().__init__(pname,Temp,Bdypn,CouCol)
  
#    def SickRslt(self):
      
#       if self.Temp>99:
#          print(f"{self.pname} you have fever")

#       elif self.BdyPn=='Y' or self.BdyPn=='y' and self.CouCol=='Y' or self.CouCol=='y':
#          print(f"{self.pname} you have fever")

#       else:
#          print(f"{self.pname} you do not have fever")

# class Parent():
    
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
        
#     def Name(self):
#       print(f"Your name is: {self.name}")

#     def Age(self):
#        print(f"Your age is {self.age}")

# class Child(Parent):

#    def Welcome(self):
#       print("You are welcome")

# class Schild(Child):

#    def Hello(self):
#       print("Hello")

# name=input("Enter your name: ")
# age=int(input(f"Hello {name} enter your age: "))

# Multiherit=Schild(name,age)
# Multiherit.Hello()
# Multiherit.Welcome()
# Multiherit.Name()
# Multiherit.Age()
         
# import getpass
# username=getpass.getuser()
# print(username)
       
# class Student:

#     def Name(self):
#         print(f"Enter your Name: ")

# class detail:

#     def Age(self):
#         print(f"Enter your Age")

# class Mark:

#     def MarkT(self):
#         print(f"Enter your marks ")

# class wholedet(Student,detail,Mark):
#     pass

# obj=wholedet()
# obj.Name()
# obj.Age()
# obj.MarkT()
        
# def Sum(a,b=0,c=0):
#    return a+b+c

# print(Sum(4,5))    
# print(Sum(4,5,1))    

# def Tot(*args):
#     ans=0
#     for i in args:
#         ans+=i
#     return ans

# def Sum(*args):
#    ans=0
#    for i in args:
#       ans+=i
#    return ans

# Totv=[]
# while True:    
    
#    Numb=int(input("Enter the Number to add: "))
    
#    if Numb ==0:
#       break
   
#    Totv.append(Numb)

# obj=Sum(*Totv)
# print(obj)
   
# def SuperMarket(*args):
    
   # for i in args:
      # print(i)
   # return i

# TotUser=[]
# UserItems={}

# while True:
    
#    UserM=input("\nEnter the User Name: ")

#    if UserM=='stop' or UserM=='Stop' or UserM=='STOP':
#       break
#    TotUser.append(UserM)

#    ItemC=[]

#    while True:

#       Items=input("Enter the Items purchased by the User: ")   

#       if Items=='Nil':
#          break

#       ItemC.append(Items)
   
#       # print(ItemC)
#    # TotUser.append(UserM)
#    UserItems.append(UserM)
#    UserItems[UserM]=ItemC

#    for user,Items in UserItems:
#       print(f"user: {user} and item is {" , ".join(Items)}")


#    # UserItems.append(ItemC)
   
#    # for i in TotUser:
#    #    print(f"User: {i}")

   
   
   #    # for j in ItemC:
   #    #    print(j, end=",")
   
   # # while True:

   # #    if Items=='stop' or UserM=='Stop' or UserM=='STOP':
   # #       break
   

   # for j in ItemC:      
   #    print(j, end=", ")      

# class Details:
    
#    def __init__(self,sname,age):
#       self.age=age
#       self.sname=sname

#    def Name(self):
#       print(f"Your Name is {self.sname}")
   
#    def Aged(self):
#       print(f"Your age is {self.age}")

# class child(Details):
   
#    # def __init__(self,sname,age):
#    #    super().__init__(sname,age)
   
#    def Name(self):
#       print(f"{self.sname} you are welcome")



# sname=input("Enter your name: ")
# age=int(input("Enter your age: "))

# obj=child(sname, age)
# obj.Name()
# obj


# class Demo:
#    def __init__(self,sname,sage):
#       self.sname=sname
#       self.sage=sage
        
#    def display(self):
#       print(f"{self.sname}")
#       print(f"{self.sage}")

# obj=Demo('Abilash', 32)
# print(obj.sname)

# class Demo:
#    def __init__(self,sname,sage):
#       self.sname=sname
#       self.sage=sage
        
#    def _display(self):
#       print(f"{self.sname}")
#       print(f"{self.sage}")

# obj=Demo('Abilash', 32)
# obj._display()

# class Demo:
#    def __init__(self,sname,sage):
#       self.__sname=sname
#       self.sage=sage
        
#    def __display(self):
#       print(f"{self.__sname}")
#       print(f"{self.sage}")

#    #Getters

#    def Pdisplay(self):
#       print(f"Your name is {self.__sname}")
#       self.__display()

# obj=Demo('Abilash', 32)
# obj.Pdisplay()

# class Demo:
#    def __init__(self,sname,sage):
#       self.__sname=sname
#       self.sage=sage
        
#    def __display(self):
#       print(f"{self.__sname}")
#       print(f"{self.sage}")

#    #Getters

#    def Pdisplay(self):
#       print(f"Your name is {self.__sname}")
#       self.__display()

#    #setters

#    def hello(self,pname):
#       self.__sname=pname

#       print(self.__sname)

# obj=Demo('Abilash', 32)
# obj.Pdisplay()
# obj.hello('Sun')

# def add(a,b):
#     return a+b

# def mul(a,b):
#     return(a*b)

# print(TotUser)
    
   # obj=SuperMarket(UserM)
              
# from datetime import datetime, timedelta
# # import datetime

# print("Local version of date and time: ", datetime.now().strftime("%c"))
# print("Day number of the year: ", datetime.now().strftime("%j"))
# print(datetime.now().strftime("%Y"))

# def Rdays():
   
#    Year=datetime.now().strftime("%Y")
#    RemDays=datetime.now().strftime("%j")

#    if int(Year)%4==0:
#       R1=366-int(RemDays)
#       print(f"Current no of days passed is {RemDays} and Remaining days of the year are {R1}")

#    else:
#       R2=365-int(RemDays)
#       print(f"Current no of days passed is {RemDays} and Remaining days of the year are {R2}")
        

# obj=Rdays()
# obj
   

# R1=datetime.now().strftime("%d")
# R2=int(R1)-1

# print(f"Yesterday: {datetime.now().strftime("%Y-%m")}-{R2}")

# today=datetime.now()

# yesterday = datetime.now() - timedelta(days=1)
# print("Yesterday is: ", yesterday.strftime("%Y-%m-%d"))

# two_days_ago = datetime.now() - timedelta(days=2)
# print("Two days ago date: ", two_days_ago.strftime("%Y-%m-%d"))

# from random import random

# import random

# print(random.random())

# print(random.randint(1000,9999))

# Choice=["Pen", "Pencil", "Bottle", "Ink", "Bag"]

# print(random.choices(Choice))

# V1=random.randint(100000, 999999)

# print(V1)

# U1=input("Enter the OTP: ")

# if V1==int(U1):
#     print("OTP validated successfully")

# else:
#     print("OTP validation failed")
   
            
# try:
#     a=int(input("Enter the first number: "))
#     b=int(input("Enter the second number: "))

#     x=a/b

#     print(x)

# except Exception as error:
    
#     print("The error is: ", error)

# finally:
    
#     print("Completed")
        

# try:
#     a=int(input("Enter the first number: "))
#     b=int(input("Enter the second number: "))

#     x=a/b

#     print(x)

# except ZeroDivisionError:
#     print("Number is not divisible by Zero")

# except ValueError:
#     print("Your entered not a number")

# except Exception as error:
    
#     print("The error is: ", error)

# finally:
    
#     print("Completed")
                
    
# Filenew=open("inheritance.py", "r")

# print(Filenew.read())

# Filenew.close()

# hi=open("demo.csv", "r")

# print(hi.read())

# hi.seek(0)

# print(hi.readline())

# hi.seek(0)

# for i in hi.readlines():
#     print(i)

# hi.close()

# hi=open("demo.csv", "r+")

# print(hi.read())

# print(hi.write("hello\n"))

# InsText=["Hi\n", "hello\n", "and\n", "welcome\n", "to\n", "Python\n", "Learning\n"]

# hi.writelines(InsText)

# hi.close()

# hello=open("abilash.csv", "w+")

# hello.write("New Document\n")

# InsText=["Hi\n", "hello\n", "and\n", "welcome\n", "to\n", "Python\n", "Learning\n"]

# hello.writelines(InsText)

# hello.seek(0)

# print(hello.read())

# print(hello.readable())
# print(hello.writable())


# hello.close()


# hello=open("abilash.csv", "a")

# hello.write("Append1\n")

# print(hello.readable())

# print(hello.writable())

# hello.close()


# FileNew=open("Task.csv", "a+")

# FileNew.write("New File created\n")

# FileNew.seek(0)
# print(FileNew.read())

# FileNew.write("Appending Hello\n")

# FileNew.seek(0)
# print(FileNew.read())

# FileNew.close()

# import os

# print(dir(os))

# print(os.getcwd())

# print(os.listdir())

# for i in os.listdir():
#     print(i)

# os.chdir("C:\\Users\\Abilash SP\\Documents")

# print(os.getcwd())

# print(os.listdir("."))

# os.chdir("D:\\learning\\Git_Main\\python_learning")

# print(os.listdir())
# print(os.getcwd())

# os.chdir("C:\\Users\\Abilash SP\\Documents")

# os.makedirs("Test1")

# os.removedirs("Test1")

# os.chdir("D:\\learning\\Git_Main\\python_learning")

# print(os.getcwd())

# print(open("test.txt", "a+"))

# os.remove("test.txt")

# File=input("Enter the filename: ")

# if os.path.exists(File):
    
#     print("File exists")

# else:
#     fp=open(File,"w")
#     fp.write("Hello\n")
#     fp.write("World\n")
#     fp.write("Python\n")
#     fp.close()

# import csv

# # with open("abilash.csv", "r") as files:
# #     read_content=csv.reader(files)
# #     print(read_content)

# #     for i in read_content:
# #         print(i)

# with open("abilash.csv", "r") as files:
#     read_content=csv.reader(files)

#     print(next(read_content))
#     print(next(read_content))
#     print(next(read_content,"End"))
#     print(read_content)

#     for x in read_content:
#         print(x)

# import tkinter

# window=tkinter.Tk()
# window.title("First GUI")
# label=tkinter.Label(window,text="WELCOME TO MY FIRST GUI",font=("Arial", 24), fg="green", bg="white")
# label.pack()
# window.geometry("600x600")

# x=tkinter.Button(window,text="Click me if you want X", font=("Comic Sans MS", 10), fg="white", bg="red", command=lambda: print("You have clicked X"), padx=10,pady=10)
# x.pack()

# y=tkinter.Button(window,text="Click me if you want Y", font=("Comic Sans MS", 10), fg="white", bg="blue", command=lambda: print("You have clicked Y"),padx=10,pady=10)
# y.pack()

# window.mainloop()

import tkinter as tk

# window=tk.Tk()
# window.title("Function Check")

# label=tk.Label(window,text="Display on the Interface", font=("Cambria", 20), fg="white", bg="green")
# label.pack()
# window.geometry("400x400")

# def MyName():
#    label.config(text="Abilash", font=("Comic Sans MS", 20))

# def DefaultName():
#    label.config(text="Have a Nice Day!", font=("Comic Sans MS", 20))

# x=tk.Button(window,text="Click me to display my Name", font=("Comic Sans MS", 10), fg="white", bg="red", command=MyName)
# x.pack()

# y=tk.Button(window,text="Click for some text", font=("Comic Sans MS", 10), fg="white", bg="blue", command=DefaultName)
# y.pack()

# window.mainloop()

# window=tk.Tk()
# window.title("New Window Check")

# label=tk.Label(window,text="Hello to Program", font=("Cambria", 20), fg="white", bg="green")
# label.pack()
# window.geometry("400x400")

# def MyName():
#    Window1=tk.Tk()
#    Window1.title("Welcome to Window one")
#    label1=tk.Label(Window1,text="Hello to Window1").pack()
#    Window1.geometry("400x400")
   

# def DefaultName():
#    Window2=tk.Tk()
#    Window2.title("New Window Two")
#    label2=tk.Label(Window2,text="Hello to Window2").pack()
#    Window2.geometry("400x400")
   
# # Button to appear at the bottom use frame

# button_frame = tk.Frame(window)
# button_frame.pack(side='bottom', pady=10)

# x=tk.Button(button_frame,text="Window One", font=("Comic Sans MS", 10), fg="red", bg="black", padx=10, pady=10, command=MyName)
# x.pack(padx=(30), pady=(20,30),side=tk.LEFT)

# y=tk.Button(button_frame,text="Window Two", font=("Comic Sans MS", 10), fg="blue", bg="yellow", padx=10, pady=10, command=DefaultName)
# y.pack(padx=(30), pady=(20,30),side=tk.BOTTOM)



# window.mainloop()

from tkinter import *

# window=tk.Tk()
# window.title("My First Tkinter App!")

# w=Canvas(window,width=600,height=600)
# w.pack()
# w.create_line(2,0,2,300, fill="red")
# w.create_line(0,2,300,2, fill="red")
# w.create_line(300,300,0,300, fill="red")
# w.create_line(300,300,300,0, fill="red")

# w.create_line(0,0,300,300, fill="red")
# w.create_line(300,0,0,300, fill="red")

# # w.create_oval(100,100,300,300, fill="red")
# w.create_rectangle(0,100,200,300,fill="yellow",outline="red")
# w.create_polygon(0,300, 300,300, 300,0, fill="blue",outline="red")
# w.create_polygon(0,0, 300,300, 300,0, fill="green",outline="red")

# # w.create_rectangle(100,100,200,200, fill="green")

# # button = tk.Button(w, text="Click Me")

# # w.create_window(150, 100, window=button)

# w.create_arc(0,100,200,300,fill="magenta",outline="white")
# w.create_arc(0,100,200,300, start=0, extent=50, fill="white",outline="white")



# window.mainloop()

# window=tk.Tk()
# window.title=("Calculator")
# window.geometry("600x600")
    

# w=Canvas(window, width=600)
# w.pack()

# UsInp=tk.Entry(w,width=100,font=("Arial", 12),border=5).pack(ipady=20,padx=(150),pady=(20,0),side=tk.TOP)



# button1=tk.Button(w,text="1")
# w.create_window(150,200, window=button1)
# button1.pack(ipadx=5,ipady=5,padx=(150), pady=(20,100),side=tk.LEFT)

# button2=tk.Button(w,text="2")
# w.create_window(150,100, window=button2)
# button2.pack(ipadx=5,ipady=5, padx=(10), pady=(20,100),side=tk.LEFT)



# window.mainloop()

# import tkinter as tk

# window=tk.Tk()
# window.title("Calculate")
# window.geometry("600x600")

# def add():
#    try:
#       Num1=float(entry1.get())
#       Num2=float(entry2.get())
#       res_label.config(text=f"Result: {Num1 + Num2}")
    
#    except ValueError:
#       res_label.config(text="Enter Valid Numbers")

# def sub():
#    try:
#       Num1=float(entry1.get())
#       Num2=float(entry2.get())
#       res_label.config(text=f"Result: {Num1 - Num2}")

#    except ValueError:
#       res_label.config(text="Enter Valid Numbers")

# def mul():
#    try:
#       Num1=float(entry1.get())
#       Num2=float(entry2.get())
#       res_label.config(text=f"Result: {Num1 * Num2}")

#    except ValueError:
#       res_label.config(text="Enter Valid Numbers")

# def div():
#    try:
#       Num1=float(entry1.get())
#       Num2=float(entry2.get())
#       res_label.config(text=f"Result: {Num1 / Num2}")

#    except ValueError:
#       res_label.config(text="Enter Valid Numbers")            


# entry1=tk.Entry(window,border=2)
# entry1.pack(ipadx=120,ipady=10,pady=20)

# entry2=tk.Entry(window,border=2)
# entry2.pack(ipadx=120,ipady=10,pady=5)

# button_frame = tk.Frame(window)
# button_frame.pack(side='top', pady=10)



# B1=tk.Button(button_frame,text="+",font=("Arial",15),background="orange",fg="white",command=add).pack(ipadx=2,ipady=2,padx=5,side=tk.LEFT)
# B2=tk.Button(button_frame,text="-",font=("Arial",15),background="orange",fg="white",command=sub).pack(ipadx=5,ipady=2,padx=5,side=tk.LEFT)
# B3=tk.Button(button_frame,text="*",font=("Arial",15),background="orange",fg="white",command=mul).pack(ipadx=5,ipady=2,padx=5,side=tk.LEFT)
# B4=tk.Button(button_frame,text="/",font=("Arial",15),background="orange",fg="white",command=div).pack(ipadx=5,ipady=2,padx=5,side=tk.LEFT)

# res_label=tk.Label(window, text="Result: ",font=("Arial",20))
# res_label.pack(side=tk.TOP)

# window.mainloop()

# window=tk.Tk()
# window.title("Calculator")

# entry=tk.Entry(window,width=25,border=4,background="ivory",foreground="red",font=("Comic Sans MS", 12))
# entry.pack(ipady=10,pady=10)

# window.geometry("300x300")
# window.configure(bg="gray")

# frame1=tk.Frame(window,bg="gray")
# frame1.pack(side="top", padx=2)

# B1=tk.Button(frame1,text="1", font=("Comic Sans MS", 12), width=3, background="ivory", foreground="red", border=5, command=lambda: entry.insert(tk.END, "1")).pack(padx=5,pady=2,side=tk.LEFT)
# B2=tk.Button(frame1,text="2", font=("Comic Sans MS", 12), width=3, background="ivory", foreground="red", border=5, command=lambda: entry.insert(tk.END, "2")).pack(padx=5,pady=2,side=tk.LEFT)
# B3=tk.Button(frame1,text="3", font=("Comic Sans MS", 12), width=3, background="ivory", foreground="red", border=5, command=lambda: entry.insert(tk.END, "3")).pack(padx=5,pady=2,side=tk.LEFT)
# B4=tk.Button(frame1,text="+", font=("Comic Sans MS", 12), width=3, background="ivory", foreground="red", border=5, command=lambda: entry.insert(tk.END, "+")).pack(padx=5,pady=2,side=tk.LEFT)

# frame2=tk.Frame(window,bg="gray")
# frame2.pack(side="top",padx=2,pady=2)

# B5=tk.Button(frame2,text="4", font=("Comic Sans MS", 12), width=3, background="ivory", foreground="red", border=5, command=lambda: entry.insert(tk.END, "4")).pack(padx=5,pady=2,side=tk.LEFT)
# B6=tk.Button(frame2,text="5", font=("Comic Sans MS", 12), width=3, background="ivory", foreground="red", border=5, command=lambda: entry.insert(tk.END, "5")).pack(padx=5,pady=2,side=tk.LEFT)
# B7=tk.Button(frame2,text="6", font=("Comic Sans MS", 12), width=3, background="ivory", foreground="red", border=5, command=lambda: entry.insert(tk.END, "6")).pack(padx=5,pady=2,side=tk.LEFT)
# B8=tk.Button(frame2,text="-", font=("Comic Sans MS", 12), width=3, background="ivory", foreground="red", border=5, command=lambda: entry.insert(tk.END, "-")).pack(padx=5,pady=2,side=tk.LEFT)

# frame3=tk.Frame(window,bg="gray")
# frame3.pack(side="top",padx=2,pady=2)

# B9=tk.Button(frame3,text="7", font=("Comic Sans MS", 12), width=3, background="ivory", foreground="red", border=5, command=lambda: entry.insert(tk.END, "7")).pack(padx=5,pady=2,side=tk.LEFT)
# B10=tk.Button(frame3,text="8", font=("Comic Sans MS", 12), width=3, background="ivory", foreground="red", border=5, command=lambda: entry.insert(tk.END, "8")).pack(padx=5,pady=2,side=tk.LEFT)
# B11=tk.Button(frame3,text="9", font=("Comic Sans MS", 12), width=3, background="ivory", foreground="red", border=5, command=lambda: entry.insert(tk.END, "9")).pack(padx=5,pady=2,side=tk.LEFT)
# B12=tk.Button(frame3,text="*", font=("Comic Sans MS", 12), width=3, background="ivory", foreground="red", border=5, command=lambda: entry.insert(tk.END, "*")).pack(padx=5,pady=2,side=tk.LEFT)

# frame4=tk.Frame(window,bg="gray")
# frame4.pack(side="top",padx=2,pady=2)

# B13=tk.Button(frame4,text="/", font=("Comic Sans MS", 12), width=3, background="ivory", foreground="red", border=5, command=lambda: entry.insert(tk.END, "/")).pack(padx=5,side=tk.LEFT)
# B14=tk.Button(frame4,text="%", font=("Comic Sans MS", 12), width=3, background="ivory", foreground="red", border=5, command=lambda: entry.insert(tk.END, "%")).pack(padx=5,side=tk.LEFT)
# B15=tk.Button(frame4,text="=", font=("Comic Sans MS", 12), width=3, background="ivory", foreground="red", border=5, command=lambda: Calculate()).pack(padx=5,side=tk.LEFT)
# B16=tk.Button(frame4,text="C", font=("Comic Sans MS", 12), width=3, background="ivory", foreground="red", border=5, command=lambda: entry.delete(0, tk.END)).pack(padx=5,side=tk.LEFT)


# def Calculate():
#    Expression=entry.get().strip()

#    try:

#       if "+" in Expression or "-" in Expression or "*" in Expression or "/" in Expression or "%" in Expression:
#          result=eval(Expression)
#          entry.delete(0,tk.END)
#          entry.insert(0,result)

#       else:
#          entry.delete(0,tk.END)
#          entry.insert(0, "Invalid")

#    except Exception as e:
#       entry.delete(0,tk.END)
#       entry.insert(0, e)

# window.mainloop()

# def add_to_expression(value):
#     entry.insert(tk.END, value)

# def clear_entry():
#     entry.delete(0, tk.END)

# def calculate():
#     expression = entry.get()
#     try:
#         result=eval(expression)
#         entry.delete(0, tk.END)
#         entry.insert(0, result)

#     except:
#         entry.delete(0, tk.END)
#         entry.insert(0, "Error")

# #Create main window
# root = tk.Tk()
# root.title("Mini Calculator")
# root.geometry("250x500")

# # Entry box
# entry = tk.Entry(root,font=("Arial", 18), justify="right", width=15, borderwidth=2, bg="ivory", relief="ridge")
# entry.pack(pady=20, padx=10, fill=tk.X)

# buttons = [
#     ['7', '8', '9'],
#     ['4', '5', '6'],
#     ['1', '2', '3'],
#     ['0', '+', '-'],
#     ['C', '%', '=']
# ]

# #Create buttons

# for row in buttons:
#    frame = tk.Frame(root)
#    frame.pack(pady=2)
#    for btn_text in row:
#       if btn_text == 'C':
#          action = clear_entry
#       elif btn_text == '=':
#           action = calculate
#       else:
#           action = lambda value = btn_text: add_to_expression(value)
#       if btn_text in ['+', '-', '%', '=']:
#           btn = tk.Button(frame, text=btn_text, width=5, height=2, font=("Arial", 14), command=action)
#       else:
#           btn = tk.Button(frame, text=btn_text, width=5, height=2, font=("Arial", 14), command=action)
#       btn.pack(side=tk.LEFT, padx=5, pady=5)

# root.mainloop()

######## Stop Watch ######

# import tkinter as tk

# window=tk.Tk()
# window.title("Stop Watch")

# window.geometry("300x100")
# window.configure(bg="ivory")

# S1=0
# S2=0
# M1=0
# M2=0
# H1=0
# H2=0

# wat_label=tk.Label(window, text=f"{H2}{H1}:{M2}{M1}:{S2}{S1}",font=("Arial",20))
# wat_label.pack(side=tk.TOP)

# def Start():
#     global S1
#     global S2
#     global M1
#     global M2
#     global H1
#     global H2

#     #Seconds

#     if S1<10:
#         S1+=1
#         # S2+=1
#         wat_label.config(text=f"{H2}{H1}:{M2}{M1}:{S2}{S1}")
#         window.after(10, Start)        
#     if S1==10:
#         S2+=1
#         S1=0
#         wat_label.config(text=f"{H2}{H1}:{M2}{M1}:{S2}{S1}")

#     #Minutes

#     if S2==6:
#         M1+=1
#         S2=0
#         wat_label.config(text=f"{H2}{H1}:{M2}{M1}:{S2}{S1}")
#     if M1==10:
#         M2+=1
#         M1=0
#         wat_label.config(text=f"{H2}{H1}:{M2}{M1}:{S2}{S1}")
    
#     #Hours

#     if M2==6:
#         H1+=1
#         M2=0
#         wat_label.config(text=f"{H2}{H1}:{M2}{M1}:{S2}{S1}")
#     if H1==10:
#         H2+=1
#         H1=0
#         wat_label.config(text=f"{H2}{H1}:{M2}{M1}:{S2}{S1}")
    
#     if H2==2 and H1==4:
#         H1=0
#         H2=0
#         wat_label.config(text=f"{H2}{H1}:{M2}{M1}:{S2}{S1}")
        


# def Stop():
#     pass

# def Restart():
#     pass


# frame=tk.Frame(window,bg="gray")
# frame.pack(side="top",padx=2,pady=2)

# start_button = tk.Button(frame, text="Start",font=("Comic Sans MS", 12), width=3, background="ivory", foreground="red", border=5, command=Start)
# start_button.pack(ipadx=10,padx=2,side=tk.LEFT)

# stop_button = tk.Button(frame, text="Stop",font=("Comic Sans MS", 12), width=3, background="ivory", foreground="red", border=5, command=Stop)
# stop_button.pack(ipadx=10,padx=2,side=tk.LEFT)

# restart_button = tk.Button(frame, text="Restart",font=("Comic Sans MS", 12), width=3, background="ivory", foreground="red", border=5, command=Restart)
# restart_button.pack(ipadx=20,padx=2,side=tk.LEFT)

# window.mainloop()

# def new_file():
#     print("New File Created")

# window=tk.Tk()
# window.title("Multiple Menubutton")
# window.geometry("400x300")

# #======File MenuButton =========

# file_menubutton=tk.Menubutton(window, text="File")
# file_menubutton.grid(row=0, column=0, padx=10, pady=10)

# file_menu=tk.Menu(file_menubutton, tearoff=0)
# file_menu.add_command(label="New", command=new_file)
# file_menu.add_command(label="Exit", command=window.quit)
# file_menubutton.config(menu=file_menu)

# #========= Menu Menubutton =========

# menu_menubutton = tk.Menubutton(window, text="Menu")
# menu_menubutton.grid(row=0, column=1, padx=10, pady=10)

# menu_menu = tk.Menu(menu_menubutton, tearoff=0) #tearoff=1, detach menu
# menu_menu.add_command(label="Open", command=new_file)
# menu_menu.add_command(label="Save", command=new_file)
# menu_menu.add_separator()

# menu_menu.add_command(label="Exit", command=window.quit)
# menu_menubutton.config(menu=menu_menu)

# window.mainloop()

# from tkinter import *

# def selection():
#     selected_language = "You selected the option: " + radio.get()
#     label.config(text=selected_language)

# window = Tk()
# window.geometry("300x150")

# radio = StringVar() # Change to StringVar instead of IntVar

# lbl = Label(text="Favourite programming language:")
# lbl.pack()

# R1 = Radiobutton(window, text="C", variable=radio, value="C", command=selection)
# R1.pack(anchor=W) #be n, ne, e, se, s, sw, w, nw, or center; Anchor position all capital letters

# R2 = Radiobutton(window, text="C++", variable=radio, value="C++", command=selection)
# R2.pack(anchor=W)

# R3 = Radiobutton(window, text="Python", variable=radio, value="Python", command=selection)
# R3.pack(anchor=W)

# label = Label(window)
# label.pack()

# window.mainloop()


# def select():
#     sel = "Value = " + str(v.get())
#     label.config(text=sel)

# window = Tk()
# window.geometry("200x100")
# v = DoubleVar()
# scale = Scale(window, variable=v, from_= 1, to=100, length=200, orient=HORIZONTAL)
# scale.pack(anchor=CENTER)
# btn = Button(window, text="Value", command=select)
# btn.pack(anchor=CENTER)
# label=Label(window)
# label.pack()
# window.mainloop()

import tkinter as tk

def on_scroll(*args):
   """
   Function to handle scrollbar movement and adjust the view of the Text widget accordingly.
   """
   text_widget.xview(*args)

# Create the main Tkinter window
root = tk.Tk()
root.title("Adding a X-Scrollbar to Text Widget")
# Set window dimensions
root.geometry("720x250")

# Step 1: Create a Text widget
text_widget = tk.Text(root, wrap="none", width=40, height=10)
text_widget.pack(padx=10, pady=10)

# Step 2: Create a horizontal scrollbar
xscrollbar = tk.Scrollbar(root, orient="horizontal")

# Step 3: Link the scrollbar to the Text widget
text_widget.config(xscrollcommand=xscrollbar.set)

# Step 4: Configure the scrollbar to call the on_scroll function
xscrollbar.config(command=on_scroll)

# Pack the scrollbar to make it visible
xscrollbar.pack(fill="x")

# Step 5: Insert some text into the Text widget
text_widget.insert("1.0", "This is Tutorialspoint.com-Simply Easy Learning At Your Fingertips. " * 10)

# Start the Tkinter event loop
root.mainloop()