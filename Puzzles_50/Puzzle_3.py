# Define a function sum_even that takes one parameter:
# Name Type Example Input
# input_nums list of int [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# When called, the function should return the sum of even integers in
# the list.

def sum_even(lst):
    result = 0
    for num in lst:
        if num%2 == 0 :
            result += num
    return result

ex_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_even(ex_list))