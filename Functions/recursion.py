# Recursion: When a function calling itself to solve the problem that called recursion:

# Example: Fibnaccio Series/Sequence:
'''
series:    0 1 1 2 3 5 8 13  # (0 1) are default value/ base value 
numbering: 0 1 2 3 4 5 6 7 
'''

#Example 2: To find the fib(6) using recursion of fibnaccio series:
def fib(n):
    if(n == 0) or (n == 1):
        return n
    
    return fib(n-2) + fib(n-1)

print(fib(6))      # Output --> 8

# How it is possible:
'''
fib(n-2) + fib(n-1)
fib(6-2) + fib(6-1)
fib(4) + fib(5)
fib(2) + fib(3) + fib(5)
fib(0)+ fib(1) + fib(1) + fib(2) + fib(5)
0 + 1 + 1 + 0 + 1 + fib(5)
0 + 1 + 1 + 0 + 1 + fib(5-2)+ fib(5-1)
0 + 1 + 1 + 0 + 1 + fib(3) + fib(4)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + fib(2) + fib (3)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + 0 + 1 = 8 
'''
# 8 is Output: 


# Example: To find the factorial:
def fact(n):
    if(n == 1):
        return n
    return n * fact(n-1)

print(fact(5))        # Output --> 120
   