# Exercise 5_1
# 5.1 (What’s Wrong with This Code?) What, if anything, is wrong with each of the following
# code segments?
# a) day, high_temperature = ('Monday', 87, 65)
    # There is not enough item in the left side
# b) numbers = [1, 2, 3, 4, 5]
# numbers[10]
    #There are not 10 terms int the list
# c) name = 'amanda'
# name[0] = 'A'
    # strings are immutable. You can not change name[0] 
# d) numbers = [1, 2, 3, 4, 5]
# numbers[3.4]
    #index are only integers. numbers[3.4] will generate an error
# e) student_tuple = ('Amanda', 'Blue', [98, 75, 87])
    # tuples are immutable like strings. You cannot change student_tuple nmber of elements.
# student_tuple[0] = 'Ariana'
# f) ('Monday', 87, 65) + 'Tuesday'
    #This will generate a type error
# g) 'A' += ('B', 'C')
    # The augmentated operator += don't work for strings when they are on the left side of the operant
# h) x = 7
# del x
# print(x)
    # This will generate the error that x doesn't exist as it is deleted
# i) numbers = [1, 2, 3, 4, 5]
# numbers.index(10)
    # This will generate a value error as 10 is not in the list
# j) numbers = [1, 2, 3, 4, 5]
# numbers.extend(6, 7, 8)
    # This will generate an error because the list method extend take only one argument but has been provided 3 
# k) numbers = [1, 2, 3, 4, 5]
# numbers.remove(10)
    #This will generate an error as the list doesn't contain 10
# l) values = []
# values.pop()
    #This will generate an  error as the list pop method only works when list length is 1 or more