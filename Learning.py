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

window=tk.Tk()
window.title("My First Tkinter App!")

w=Canvas(window,width=600,height=600)
w.pack()
w.create_line(2,0,2,300, fill="red")
w.create_line(0,2,300,2, fill="red")
w.create_line(300,300,0,300, fill="red")
w.create_line(300,300,300,0, fill="red")

w.create_line(0,0,300,300, fill="red")
w.create_line(300,0,0,300, fill="red")

# w.create_rectangle(100,100,200,200, fill="green")

window.mainloop()