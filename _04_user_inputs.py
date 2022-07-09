user_name = input("Hi! What's your name?\n")
print(f'hello {user_name}. Pleased to meet you.')


def num_square(number):
    res = number * number
    return res


num = input("Enter a number to be squared. \n")
square = num_square(int(num))
print(f'The square of {num} is {square}')


