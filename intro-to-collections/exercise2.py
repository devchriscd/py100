# Can you write some code to change the value 'bye' in the 
# following tuple to 'goodbye'?

stuff = ('hello', 'world', 'bye', 'now')

change_stuff = list(stuff)
change_stuff[2] = 'goodbye'
stuff = tuple(change_stuff)

print(stuff)
print(type(stuff))

