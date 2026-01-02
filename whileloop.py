# Using the While loop in Python.

#Printing the number 1 to 5 Using While loop:
i = 1
while(i < 5):
    print(i)
    i = i + 1
    
    
# Example 2: Printing numbers from 1 to 10 using while loop:
num = 1
while(num < 11):
    print(num)
    num  = num + 1
    
# Example 3: Printing even numbers from 1 to 20 using while loop:

i = 1
while(i < 21):
    if(i % 2 == 0):
        print(i)
    i = i + 1  # It is Outside of (if Block) and Inside the (While Block)
    
# Example 4: Printing the table of 5 using the while loops:
i = 1
while(i <= 10):
    print( 5 * i)
    i = i + 1
    
# Example 5: Printing the table of user input number using while loop:
num = int(input("enter the number to print the table: "))
i = 1
while(i <= 10):
    print(num * i)
    i = i + 1
    
    
# End the Program.