value = int(input('Enter a number: '))

if value == 3:
    print('value is 3')
else:
    print('VALUE IS NOT 3')

# Next example shows nested if statement inside of the else of the outer
# if statement

value = int(input('Enter a number: '))

if value == 3:
    print('value is 3')
else:
    if value == 4:
        print('value is 4')
    else:
        print('value is NOT 3 or 4')

# Avoid using nested if statements larger than 3 levels deep
# following example achieves the same as above with elif

if value == 3:
    print('value is 3')
elif value == 4:
    print('value is 4')
else:
    print('value is NOT 3 or 4')
