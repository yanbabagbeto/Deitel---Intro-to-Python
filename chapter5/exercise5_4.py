# 5.4 (Iteration Order) Create a 2-by-3 list, then use a nested loop to:
# a) Set each element’s value to an integer indicating the order in which it was processed
# by the nested loop.


my_list = [
    [10, 12, 16],
    [45, 52, 65]
]

# a) Set each element’s value to an integer indicating the order in which it was processed by the nested loop.

count_order = 0

for i in range(2):
    for j in range(3):
        count_order += 1
        my_list[i][j] = count_order
    print(my_list[i])

# print(my_list)

# b) Display the elements in tabular format. Use the column indices as headings
# across the top, and the row indices to the left of each row.
