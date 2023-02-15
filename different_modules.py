# import module to perform different operations
import time # time operations
import datetime # more advanced time and date operations
import math # mathematical operations
import random # random numbers generator
import keyword # key words 
import numpy as np # numpy 

# different ways to import modules
# check where are the functions 
for i in math, random, keyword, list, tuple:
    print("Functions in " + str(i))
    print(dir(i)) # print in which directory 
    print("\n")




# draw a number <a,b>
lower_bound=1 
upper_bound=23
x=random.randint(lower_bound, upper_bound)
# choose a random number from the array
numbers=[3,4,5,6]
y=random.choice(numbers)

# draw a number from <0, 1)
z=random.random()


# chooses k uniq elements from the set or population sequence
print(random.sample(numbers, 2))

# Math module
# calculate roots
x=math.sqrt(81)
z=math.cos(180)
y=math.pow(2,3) 

root=math.pow(8, 1/3)
print(root)

math.floor(6.40) # round the number down to 6
math.ceil(5.4) # round the number up to 6
math.trunc(5.683) # remove fractional part

# Time module - operations connected with time
time.sleep(1) # delay of 50 seconds
time.localtime() # get local time
time.time() # number of seconds from 01.01.1970
print(time.strftime("%H: %M: %S", time.localtime())) # format

# datetime module
datetime.datetime.today() 
datetime.date.today() 
print(datetime.date.today().year) # print the current year
# operation on dates
d1=datetime.date.today()
d2=datetime.date(year=2020, month=4, day=30)
print(d1-d2)
number_of_days=datetime.timedelta(days=6)
d3=d1+number_of_days
print(d3)

# keyword module
print(keyword.kwlist) # print the list of keywords

# Task 1 
# Define a tuple with 10 random elements. Count geometric mean.
elements=np.random.randint(10, 20, size=3)
elements=tuple(elements)
print(type(elements))
print(elements)

def geometric_mean(numbers):
    if type(numbers)!=tuple:
        return
    res=1
    for i in numbers:
        res=res*i
    return math.sqrt(res)

print(geometric_mean(elements))

# Task 2
# Count the area of the acute triangle with given a, b and alpha.
a=10
b=20
alpha=85

def triangle_area(a,b,alpha):
    return a*b/2*math.sin(alpha)
