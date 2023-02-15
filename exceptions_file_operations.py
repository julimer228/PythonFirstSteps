# File operations
# open file
filename="test.txt"
mode="w" # r - read, w - write, a - append, x - create
my_file=open(filename,mode)

filename2="test2.txt"
# more popular form
with open(filename2, mode) as my_file2:
    # do some operations
    my_file2.write("Writing a new sentence!")
    # we do not need to close file here

# read file
# my_file.read() # whole file
# my_file.read(4) # read four characters
# my_file.readline() # read one line
# my_file.readlines() # read all lines

# close file
my_file.close()

# Exceptions
try:
    suma=98+68/0
except ZeroDivisionError:
    print("This operation is not allowed")
except:
    print("Some other exception")

# try except finally
try:
    with open("my_file.txt", "r") as my_file3:
        my_file3.readline()
except FileExistsError:
    print("File does not exist")
except FileNotFoundError:
    print("File not found")
except:
    print("Other exception")
finally:
    print("I will print this words anyway")

# throwing exceptions
def square_area(a):
    if a<=0:
        raise ValueError
    return a*a

try:
    square_area(-10)
except ValueError:
    print("This operation is impossible")


    

