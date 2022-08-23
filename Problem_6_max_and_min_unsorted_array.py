# Max and Min in an Unsorted Array
# In this problem, we will look for smallest and largest integer
# from a list of unsorted integers. The code should run in O(n) time.
# Do not use Python's inbuilt functions to find min and max.
#
# Bonus Challenge: Is it possible to find the max and min in
# a single traversal?

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min_ = ints[0]
    max_ = ints[0]

    for n in ints:
        if n < min_:
            min_ = n
        elif n > max_:
            max_ = n
    return min_, max_


## Example Test Case of Ten Integers
import random

# test1:
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# test2:
l = [1050, 59, 102, 63, 2]
print ("Pass" if ((2, 1050) == get_min_max(l)) else "Fail")

# test3:
l = [i for i in range(5, 100)]
random.shuffle(l)

print ("Pass" if ((5, 99) == get_min_max(l)) else "Fail")

# test4:
l = [0, 0, 0, 0, 0]
print ("Pass" if ((0, 0) == get_min_max(l)) else "Fail")