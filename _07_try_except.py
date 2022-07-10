
def division_func(var1, var2):
    try:
        int_var1 = int(var1)
        int_var2 = int(var2)

        print('Performing Division operation')
        res = int_var1 / int_var2

        print(f'result for operation: {res}')
    except ValueError:
        print('Error: Invalid input provided')
    except ZeroDivisionError:
        print('Error: Dont divide by zero')
    except:  # catch all error
        print('Generic error handling')
    finally:
        print('This will always execute')


print('Welcome to Division program unit')
num1 = input('Enter first number (Numerator)\n')
num2 = input('Enter second number (Denominator)\n')

division_func(num1, num2)
