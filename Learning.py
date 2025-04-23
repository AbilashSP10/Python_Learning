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

sum=0
for i in range (1,31,2):      
    sum+=i
print(sum)
    