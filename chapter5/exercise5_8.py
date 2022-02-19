# 5.8
#  (Sieve of Eratosthenes) A prime number is an integer greater than 1 that’s evenly
# divisible only by itself and 1. The Sieve of Eratosthenes is an elegant, straightforward
# method of finding prime numbers. The process for finding all primes less than 1000 is:
# a) Create a 1000-element list primes with all elements initialized to True. List el-
# ements with prime indices (like 2, 3, 5, 7, 11, ...) will remain True. All other
# list elements will eventually be set to False.
my_list = list(range(2, 1000))
initial_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 19, 31]
for j in initial_primes:
    [my_list.remove(item) for item in my_list if item % j == 0]

# b) Starting with index 2, if a given element is True iterate through the rest of the
# list and set to False every element in primes whose index is a multiple of the
# index for the element we’re currently processing. For list index 2, all elements
# beyond element 2 in the list that have indices which are multiples of 2 (i.e., 4,
# 6, 8, 10, ..., 998) will be set to False.
# c) Repeat Step (b) for the next True element. For list index 3 (which was initial-
# ized to True), all elements beyond element 3 in the list that have indices which
# are multiples of 3 (i.e., 6, 9, 12, 15, ..., 999) will be set to False; and so on. A
# subtle observation (think about why this is true): The square root of 999 is
# 31.6, you’ll need to test and set to False only all multiples of 2, 3, 5, 7, 9, 11,
# 13, 17, 19, 23, 29 and 31. This will significantly improve the performance of
# your algorithm, especially if you decide to look for large prime numbers.
# When this process completes, the list elements that are still True indicate that the index is
# a prime number. These indices can be displayed. Use a list of 1000 elements to determine
# and display the prime numbers less than 1000. Ignore list elements 0 and 1. [As you work
# through the book, you’ll discover other Python capabilities that will enable you to cleverly
# reimplement this exercise.]
my_list = initial_primes + my_list
my_list.sort()
print(my_list)
