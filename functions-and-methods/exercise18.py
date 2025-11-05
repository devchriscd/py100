numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []

def remainders_3(numbers):
    return any(number % 3 > 0 for number in numbers)

print(remainders_3(numbers_4))

