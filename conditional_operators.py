import time;
#print numbers
print(5)

#print string
print("Julia")

#Calculate 
a=3*15*99/121+3
print(a)

#Add strings
print("Hello "+"World!")

#convert into to string
print("I have "+str(3)+" cats.")

#If we don't want to go to the next line -> use end=''
print("Do not go to the next line!", end="")
print(" Here we are!")

#It is possible to multiply strings
print(5*"Cat ")

# Print book title
print("\"DeepLearning with Tensorflow\"")

age=input("Enter your age:")
year=time.localtime().tm_year
print("You were born in "+str(int(year)-int(age)))

#integer part from division
print(int(100/33))
#or
a=100/33
print(int(a))

#calculate rectangular trapezoid area
a=4
b=9
h=12
d=13
area=((a+b)/2*h)
print(area)

#Calculate 55*66*77-3 and print the result
print("Here is the result: "+str(44*66*77-3))

#conditions
age=int(input("Enter your age: "))
if age>=18:
    print("You are an adult in Poland!")
elif age>=0:
    print("You are a child!")
else:
    print("Age cannot be lover than 0")
    
#calculations
x=float(input("Enter the first number!: "))
y=float(input("Enter the second number!: "))
print("Sum: "+str(x+y))
print("Subtraction: "+str(x-y))
print("Multiplication: "+str(x*y))
if y!=0:
    print("Division: "+str(x/y))
else:
    print("You cannot division by zero!")

if x%2==0:
    print("First number is even")
else:
    print("First number is odd")
    
age=int(input("Enter your age: "))
money=float(input("Enter how much money you have: "))
if age>=18:
    if money>20:
        print("You can buy alcohol")
    if money<20:
        print("You do not have enough money!")
elif age>0:
    print("You are a child! You can't buy alcohol!")
else:
    print("Age is smaller than zero!")
               