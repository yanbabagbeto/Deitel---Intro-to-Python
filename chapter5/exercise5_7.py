# TODO:
# 5.7 (Duplicate Elimination) Create a function that receives a list and returns a (possibly
# shorter) list containing only the unique values in sorted order. Test your function with
# a list of numbers and a list of strings.
# create 2 lists for the test list_a and list_b


list_a = [1, 2, 3, 4, 5, 5, 4, 2, 3, 4, 18, 101, 12, 18, 2, 9, 7]
list_b = ['a', 'b', 1, 2, 3, 'c']
list_test = [1, 2, 3, 4, 3, 5, 7]
list_long = list_a + list_b + list_test
# PSEUDOCODE 1st pass
# verify if there is any duplicate
# go through the list and for every item verify if the is an identical item
# with the same value on the list
# starting at the current item index+1

# PSEUDOCODE 2nd pass
# repeat until there is no  more duplicate
# if any item is found on that list
# find it's index in the original list
# delete it

# if any duplicate


def duplicate_exist(my_list):
    for i in range(len(my_list)):
        if my_list[i] in my_list[i+1:]:
            return True


# return the identified duplicate index
def return_index(my_list):
    for i in range(len(my_list)):
        if my_list[i] in my_list[i+1:]:
            return my_list.index(my_list[i], i+1)
            break


def eliminate(my_list):
    while duplicate_exist(my_list):
        x = return_index(my_list)
        del my_list[x]
        # print(my_list)
    return my_list


print(eliminate(list_a))
# eliminate(list_b)
# eliminate(list_test)
# eliminate(list_long)

# print(list_a)
