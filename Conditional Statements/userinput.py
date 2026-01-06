# How to take User Input in Python.

# using input() to take user input in program.
# VS Code: Automatically Knows the input type is string/Integer/Float based on the input value.

# Example 1: Taking a string input from the user
name = input("Enter your name: ")
print(name)
print(type(name)) # This will show that the type is str:

# Example 2: Taking an integer input from the user

age = int(input("Enter the age: "))
print(age)
print(type(age)) # This will show that the type is int:

# Final of Both:
user_name = input("enter your name: ")
user_age = int(input("enter your age: "))

print(type(user_name)) # str
print(type(user_age))  # int

print(user_name)
print(user_age)


# Typecasting & Type Coversion: It is process to convert one datatype to another datatype:

# Example 3: Converting string to integer
num1 = input("enter the number : ")
print(type(num1))

# to convert string to integer:
num2 = int(num1)

# After the Conversion:
print(num2)
print(type(num2))