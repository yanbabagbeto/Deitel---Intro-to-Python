# 5.5
#  (IPython Session: Slicing) Create a string called alphabet containing 'abcdefghi-
# jklmnopqrstuvwxyz', then perform the following separate slice operations to obtain:
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# a) The first half of the string using starting and ending indices.
print(alphabet[0:13])
# b) The first half of the string using only the ending index.
print(alphabet[:13])
# c) The second half of the string using starting and ending indices.
print(alphabet[13:-1])
# d) The second half of the string using only the starting index.
print(alphabet[13:])
# e) Every second letter in the string starting with 'a'.
print(alphabet[0::2])
# f) The entire string in reverse.
print(alphabet[::-1])
# g) Every third letter of the string in reverse starting with 'z'.
print(alphabet[-1::-3])