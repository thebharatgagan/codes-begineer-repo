# There are 2 Types of Variable:

#1. Local Variable: {Inside the Function} --> Accessible within function:
def sum(a , b):
    #(a , b) are the local variable
    c = a + b
    return c

print(sum(5, 6))      # Output --> 11

#2. Global Variable: {Accessible Everywhere} --> Throughout the Program: 
z = 8
# Z is global variable: 
print(z)

# Eg:

def sum(c ,d):
    e = c + d   # c ,d are local
    z = 8  # This z is local 
    return e

z = 3 # this z is global it destroyed & replace the local variable value:
print(sum(10, 20))
print(z)     #Output --> 3 

# --------------------------------------------New Concept------------------------------------------------

# Global keyword: It can convert local variable whose inside the function to global variable using "global keyword"

def sum(a, b):
    print("Hello World")
    global z
    z = 13
    c = a + b
    return c
z = 10
print (sum(2, 3))
print(z) # Output --> 13, Because Global Variable is "z = 13"