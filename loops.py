# for loop
tab = [1,2,3,4,5]
for element in tab:
    print(element)
    
# range generator 
# - generates numbers from m to n-1 in increments of k (k can be omitted)
# print numbers from 1 to 99
for i in range(100):
    print(i)
    
# print numbers from 1 to 10 (step 5) - 1, 6
for i in range(1,10,5):
    print(i)
    
# while loop
# break - breaks the loop
# continue - ignore some instructions anf continue loop
sum=0
x=0
while x<50:
    sum=sum+1
    if sum==25:
        print("sum is: "+str(sum))
        break

y=0
while y<100:
    y=y+1
    if y%2==0:
        continue
    print(y)
    
# Loops for collections
# dictionary
fruits={"orange":20, "apple":10, "pineapple":1}
for key in fruits.keys():
    print(key)
    
for key, value in fruits.items():
    print(key,value)

# set - display elements in random order
set_of_fruits={"apple", "pineapple", "orange", "pear"}
for fruit in set_of_fruits:
    print(fruit)
    
# Task 1
# print numbers with for and while loop
# a) for loop
for i in range(0,13,3):
    print(i)
# b) while loop
i=3
while i>-3:
    i=i-1
    print(i)
    
tabx = [1,3,5,7]
taby = [2,4,6]
for x in tabx:
    for y in taby:
        if (x != 3 and y != 2):
            print(str(x) + "," +str(y))
            
# Task 2
# Input - name of products separated with comas (repetitions are possible)
# Output - all elements in dictionary with prices
products_string=input()
products_list=products_string.split(",")
products_set=set(products_list)
products_dictionary=dict()

price=10
for p in products_set:
    price=price+10
    products_dictionary[p]=price

for p, price in products_dictionary.items():
    print(p,price)

# Task 3
# try to create a do while loop with loops available 
if i<=100==False:
    print(i)
while i<100:
    print(i)


        
    
    
    