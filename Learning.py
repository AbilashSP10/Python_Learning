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

class BankDetails:
    Acc_Name='Krishnan'
    Acc_Number=98765898650
    Acc_Balance=5000

obj=BankDetails()

print(obj.Acc_Name)
print(obj.Acc_Number)
print(obj.Acc_Balance)

obj.Acc_Name=input('Enter the Account holder name: ')
obj.Acc_Number=int(input('Enter your Account Number: '))
obj.Acc_Balance=int(input('Enter your Account Balance: '))

print(obj.Acc_Name)
print(obj.Acc_Number)
print(obj.Acc_Balance)