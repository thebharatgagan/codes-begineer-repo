# All about the string:

name = "Bharat"
print(type(name))
print(name)

# There are 3 Ways to write the method of string:

name = "Bharat"
name1 = 'Bharat'
name2 = '''Bharat''' # It is multi-line string, when a code in multiple line then, we used it:
print(name)
print(name1)
print(name2)

# String indexing:
name = "Bharat"
    #   B h a r a t
    #   0 1 2 3 4 5
    
print(name[0]) # Output --> B

# Example 1: 
print(name[5]) # Output --> t
#print(name[6]) # It will be showing in runtime error, because at index{6}, no letter doesn't found

# String Slicing:
name = "Bharat"
print (name[0:6]) # Output --> Bharat

# String Methods/ String Common Function: 

#1. for Upper Case 
name = "hello world"
print(name.upper()) # Output --> HELLO WORLD

print(name.lower()) # Output --> hello world

print(name.title()) #Output --> Hello World

# To finding and replacing the text in string:
#using .find() and .replace() function respectively:

text = "Python is loved and good language."
print(text.find("good"))
print(text.replace("loved", "easy"))


# string formatting:
template  = "Dear {}, You are good and best teacher."
a = "Ram"
print(f"{a},You are good and best teacher.")


#End the program.