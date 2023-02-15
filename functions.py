import math
# function
def function_name(parameter_1, parameter_2):
    # instructions
    parameter_3=parameter_2+parameter_1
    return parameter_3

# call function
x=function_name(1,2)
print(x)

# default parameters (always after normal parameters)
def function_2(x, y=10):
    return x*y

print(function_2(3)) # 3*10
print(function_2(2,3)) # 2*3

# explicit parameters
def function_3(x,y):
    return x/y

print(function_3(y=5, x=10))
print(function_3(x=3, y=2))

# exception! - parameter y is passed twice
# print(function_3(y=4, 10))

# scopes
# local variable - exists only inside a function
# global variable - exists in the whole program

# recursion
# Fibonacci
def Fib(x):
    if x<1:
        return
    if x==1:
        return 0
    if x==2:
        return 1
    if x==3:
        return 1
    if x>3:
        return Fib(x-1)+Fib(x-2)
    
print(Fib(5))

# Function inside function
def function_outside(x,y):
    def function_inside(x):
        return x*2
    # we can call function_inside here
    return function_inside(x)*y

# it is impossible to call function_inside here
# function_inside(x) !- exception

print(function_outside(10,2))

# function with variable number of arguments
# parameter *

def different_args_fun(x, y=10, *other):
    print(x, y, other)
    
different_args_fun(10,20,[30, 39,29, 19]) # result 10 20 ([30, 39, 29, 19],)


# Task 1
# write simple calculator
def addition(x, y):
    return x+y

def subtraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    return(x/y)

def calculate(x,y,symbol):
    
    if symbol=="+":
        return addition(x,y)
    if symbol=="-":
        return subtraction(x,y)
    if symbol=="*":
        return multiplication(x,y)
    if symbol=="/":
        return division(x,y)
    return

print("Result: " +str(calculate(3,4,"+")))

# Task 2
# Check if name is male or female (Polish names)
# print names as a dictionary <name, gender>
def is_female_name(name):
    if name[-1]=='a':
        return True
    return False

names=["Agnieszka", "Maria", "Antek", "Marnian", "Ignacy"]
dict_names=dict()

for n in names:
    if is_female_name(n):
        dict_names[n]="women"
    else:
        dict_names[n]="men"
        
print(dict_names)

# Task 3 
# a) function to calculate the area of the triangle
def triangle(a, h):
    if type(a)==float and type(h)==float:
        return a*h/2
# b) function to calculate the area of the trapezoid
def trapezoid(a, b, h):
    if type(a)==float and type(b)==float and type(h)==float:
        return (a+b)*h/2
# c) use the Heron formula to calculate the area of the triangle
def heron(a,b,c):
    if type(a)==float and type(b)==float and type(c)==float:
        if a+b>c and a+c>b and b+c>a:
            s=(a+b+c)/2
            return math.sqrt(s*(s-a)*(s-b)*(s-c))
        
print("Triangle: "+str(triangle(float(4),float(2))))
print("Triangle: "+str(trapezoid(float(4),float(2),float(5))))
print("Triangle heron: "+str(heron(float(4),float(2),float(3))))


