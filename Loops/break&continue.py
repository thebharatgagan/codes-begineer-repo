#using the break statement in python.
# using break statement to exit from the loop when a condition is met. 

for i in range(1, 11):
    print(i)
    if(i == 6):
        break # when i is equal to 6 the loop will terminate.

# Example 2: using break statement in while loop.
num = 1
while(num <= 10):
    print(num)
    if(num == 5):
        break # when num is equal to 5 the loop will terminate.
    num = num + 1
    
    
# using continue statement in python.
# continue statement is used to skip the current iteration of the loop and move to the next iteration.

for i in range(1, 11):
    if(i == 2):
        continue
    print(i)  # when i is equal to 2 it will skip the print statement for that iteration.
    
    
# Example 2: using continue statement in while loop.
num = 1
while(num <= 10):
    if(num == 5):
        num = num + 1
        continue
    print(num)
    num = num + 1