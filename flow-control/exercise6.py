def caps(ten):
    ten = str() # This line is breaking my function, don't need to state the parameter into a str()
    # Without line 2 function works great.
    if len(ten) > 10:
        print(ten.upper())
    else:
        print(ten.lower())

caps('begvbaevehvgnaeiabn')

# Solution

def caps_long(string):
    if len(string) > 10:
        return string.upper()
    else:
        return string

print(caps_long("Sue Smith"))     # Sue Smith
print(caps_long("Sue Roberts"))   # SUE ROBERTS
print(caps_long("Joe Shea"))      # Joe Shea
print(caps_long("Joe Stevens"))   # JOE STEVENS

# Returning vs. Printing: The exercise asks the function to return a value. 
# Your function currently uses print() to display the value directly. 
# Using return is more flexible because it allows the code that calls 
# the function to decide what to do with the result 
# (e.g., print it, save it to a variable, etc.).
