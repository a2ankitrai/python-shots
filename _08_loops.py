# while loop
def loop_func(seed):
    num = seed
    while num < 10:
        num = num + 1
        print(num)


# loop_func(3)

#  ---
# for loop

my_list = [1, 2, 3, 5, 8]

for val in my_list:
    double = int(val) * 2
    print(double)
print('first for loop finished')

my_list = '100, 200, 300'
print(type(my_list.split(',')))
print(my_list.split(','))

for val in my_list.split(','):
    double = int(val) * 2
    print(double)
print('loop finished')
