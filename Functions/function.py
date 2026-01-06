# Using Defining function:

a = 10
b = 20
c = 30

average = (a + b + c)/3
print(average)

#using (def) keyword --> with defining the function:

def average(a, b, c):
    d = (a + b + c)/3
    print(d)
    
average(3, 5, 6)

#function arguments and return values:

#1. Possible Arguments
def add(a, b): # (a ,b) are parameters:
    x = a + b
    return x
c = add(6, 9) # (6, 9) are argument of parameters:
print(c)


#2. Default Arguments --> It means parameter already have a default values, it can be overridden also:
def add (a , b = 10):
    x = a + b
    return x
c = add(10, 20) # 20 is overidden at (b = 10)
print(c)


#3. Keyword Arguments --> It means you can give any specific parameter to any specific arguments:
def add(a , b, c = 10):
    x = a + b + c
    return x
d = add(3, 5, 7)
print (d)

d1 = add(b = 3, a = 7, c = 5) # that's call keyword arguments:
print(d1)