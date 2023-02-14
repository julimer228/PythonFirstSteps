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
