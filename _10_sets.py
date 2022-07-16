my_set = {1, 2, 3, 1, 3, 4, 2, 5}

# print set
print(my_set)
print(type(my_set))

# print each element
for ele in my_set:
    print(ele)

# convert to list
my_list = list(my_set)
print(my_list)
print(type(list(my_set)))

# elements of different type
set2 = {True, 1.3}
print(set2)

# operations
set3 = {"Jan", "Feb", "Mar"}
print(set3)
set3.add("Apr")
print(set3)
set3.remove("Feb")
print(set3)
# set3.remove("Dec") # error removing unknown key
# print(set3)

