# Puzzle-2

# Creating a function sum_if_less_than_fifty that takes 2 parameters

# When called the function should return either
# - The sum of the two numbers if the sum is less than 50
# - None if the sum of the two numbers is more than or equal to 50

def sum_if_less_than_fifty(first,second):
    if first + second < 50:
        return first + second
    else:
        None

print(sum_if_less_than_fifty(20,20))
print(sum_if_less_than_fifty(20,30))