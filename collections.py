# Collections and operations on collections
# list 
tab=[10, 20, 30, 40, 50]

# negative index 
print(tab[-1]) # print the last element
# length of the list
print(len(tab))
# max element of the tab
print(max(tab))
# min element of the tab
print(min(tab))
# sum of elements
print(sum(tab))
# sort the list
sorted(tab, reverse=1)
# add element to the list 
tab.append(45)
# insert element to the list
tab.insert(2, 3)
# take an element from the last position
x=tab.pop()
print(x)
# reverse list
tab.reverse()

# concat list
list_1=[0, 1]
list_2=[2, 3]
list_sum=list_1+list_2

# list multiplication
list_multiplication=list_1*3

# part of the list
list1=[1, 2, 3, 4, 5, 6, 7, 8]
print(list1)

# Create a list with four names and sort it. 
names=["Adam", "Zygmunt", "Beata", "Agnieszka"]
names=sorted(names)
print(names)

# add an element to the end
names.append("Karolina")

# insert an element into the list
position=2
element="Maryla"
names.insert(position, element)
print(names)

# two dimensional lists
list2d=[[1,2,3],[4,5,6]]
list2d[0] #[1,2,3]
list2d[0][1] #[2]

# Tuples - structures similar to lists but unmodifiable.

# Create tuple
element_1=3
element_2="Agata"
element_3=False
tuple1=(element_1, element_2, element_3)
# not recommended
tuple2=element_1, element_2, element_3 
print(tuple1)

# first element
print("First:" +str(tuple1[0]))

# when you add two tuples you will get a new tuple
tuple_sum=tuple1+tuple2
print(tuple_sum)

# when tuples should be used? -> when we do not want to modify something - better optimization

# Dictionaries - key, value (keys should be uniq, key is unmodifiable)
dict1={"cats": 10, "dogs": 5, "fish": 20, "mice": 200}

# print the first element
print(dict1["cats"])
# add element dict.update({key:value})
dict1.update({"zebras":55})
print(dict1)

# add element dict[key]=value
dict1["monkey"]=90
print(dict1)

# remove element
del dict1["mice"]
print(dict1)

# Task 2
# Create a shopping list (article:price). Print values and count sum of prices.
shopping={"Apples":20, "Milk":5, "Tomatoes":2, "Pepper":20}
sum_shopping=sum(shopping.values())
print(sum_shopping)

# Set 
# - unordered elements without repetition
# - better optimization than lists

set1={"element_1", 2, False}
# add element
set1.add(66)
print(set1)
# remove element set.remove(value)
set1.remove(2)
# take the last element
print(set1.pop())
# check if element is in the set
print(False in set1) # True or False

# String
# - unmodifiable - modification = new string in memory
my_string="My funny string"
# find a position of an element 
print(my_string.find("funny")) # if the element doesn't exist returns -1

# uppercase and lowercase
print(my_string.upper())
print(my_string.lower())

# change elements
print(my_string.replace("funny", "dummy"))

# split string
print("Anna, Maria, Maryla, Aneta".split(", "))

# concat strings
print("".join(["my ","funny", " string!"]))

# empty collections
# list
empty_list1=[]
empty_list2=list()

# tuple - it is impossible to modify this tuple
empty_tuple1=()
empty_tuple2=tuple()

# dictionary
empty_dict1=()
empty_dict2=dict()

# set
empty_set=set()

# Type conversion
# string to list
print(list("I am a list"))
# list to string 
print("my string: "+str(["Cat", "Dog", "Mouse"])) # adds space and comas
# set to list (in random order)
print(list({1,2,3,4,4,4,4,4,2,2})) 
# tuple form set
print(tuple({1, 2, 3, 3, 3}))

# Tasks
# Task 1
tab_task1 =[5, 15, 1, 25, 2]
tab_task1[0] #5
tab_task1[2] # 15
print(tab_task1[-1]) # 2 (last element)
print(tab_task1[-3]) # 1
# print(tab[10]) # error list index out of range
len(tab_task1) #5
print(max(tab_task1)) #25
print(sum(tab_task1))

#Task 2
# Create a dictionary with electricity bills for different months. Print maximal and minimal values,
# sum, average value. Check if the amount for the last month is greater than average if yes print warning.
spending={"January":200, "February":20, "March":40, "April":60, "May":90, "June":150, "July":400, "August":300}

sum_spending=0

for month, value in spending.items():
    print("Month: {0}, Spending: {1}".format( month, value))
    sum_spending=sum_spending+value

average=sum_spending/len(spending)
print(average)

current="August"
if average<spending[current]:
    print("You should save money!")
else:
    print("Everything is ok :)")

# Task 3
# User should enter five different numbers separate with comas. 
# Create a list. 
# Change the datatype to set. Take one element and print it.
# If user entered less than five numbers don't do anything

num_string=input()
list_numbers=list(num_string.split(","))
print(list_numbers)
if len(list_numbers)>=5:
    set_numbers=set(list_numbers)
    print(set_numbers.pop())
