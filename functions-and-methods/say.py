def say():
    print('Output from say')

print('First')
say()
print('Last')

# This is an updated version of the above code to still give an output
# When there is no argument in the function call

def say(text='hello'):
    print(text + '!')

say('Howdy') # Howdy!
say()        # hello!