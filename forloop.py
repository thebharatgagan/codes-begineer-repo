# #using for loop ;

# Example 1: Simple for loop to print numbers from 1 to 10
for i in range (1,11):
    #range function goes to (n to n-1) so, we put 11 than 10.
    print(i)
    
# Example 2: for loop to print the table of number:

for i in range(1,11):
    print(5*i)
    
# Example 3: for loop to printing the even number of 1 to 100:

for i in range(1,101):
    if(i%2==0): 
        # (%) is modulus operator:
        print(i)

# Example 4: for loop to print the table using user input:

num = int(input("Enter the number of Table: "))
for i in range(1,11):
    print(num * i)
    
    
# Example 5: for loop to printing the pattern printing;

for i in range(1,11):
    print("*" * i)

# Example 6: for loop to printing the reverse pattern printing;
for i in range(11, 1, -1):
    print("*" * i)

# Example 7: for loop to printing n time of number:

n = int(input("enter the value of n: "))
for i in range(1, n): # In n = (n-1) then if I will give n = 101, then it will printing counting to 1 to 100.
    print(i)