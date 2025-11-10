def number(integer):
    if integer >= 0 and integer <= 50:
        print(f'{integer} is between 0 and 50')
    elif integer >= 51 and integer <= 100:
        print(f'{integer} is between 51 and 100')
    elif integer > 100:
        print(f'{integer} is greater than 100')
    elif integer < 0:
        print(f'{integer} is less than 0')

number(0)
number(25)
number(50)
number(75)
number(100)
number(101)
number(-1)

# The solution is a little different, in a way for better flow control
# Not needing the 'and' operators from my conditions, although my solution
# is correct

def number_range(number):
    if number < 0:
        print(f'{number} is less than 0')
    elif number <= 50:
        print(f'{number} is between 0 and 50')
    elif number <= 100:
        print(f'{number} is between 51 and 100')
    else:
        print(f'{number} is greater than 100')
    



    