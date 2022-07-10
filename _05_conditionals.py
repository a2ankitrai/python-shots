def my_validator_func(input_num):
    if input_num > 0:
        return f"{input_num} is a positive number"
    elif input_num == 0:
        return f"{input_num} is well a ZERO"
    else:
        return f"{input_num} is a negative number"


user_input = input('Enter a number:\n')

if user_input.isnumeric():
    res = my_validator_func(int(user_input))
    print(res)
else:
    print('Please enter integer numeric value only')
