# DocString: It is used for document function, class and modules:

def sum(a,b):
    '''This program sum of given two number:'''
    c = a + b
    return c

# We want to accessed this line --> '''This program sum of given two number:''' 
print(sum.__doc__) 
# Output --> '''This program sum of given two number:'''