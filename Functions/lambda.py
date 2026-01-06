#lambda function also known as one liner function;
#It is used for large program in one line:

# Example 1 :  To find the Square: "larger Method:"
def square(n):
    return n * n

print("Result of Square:",square(4))

# Now, We use lambda function to solve the problem also in one line:

square = lambda x: x * x
print("Result of Square", square(15))