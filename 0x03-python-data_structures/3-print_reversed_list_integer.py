#!/usr/bin/python3
# 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    """
    Print all integers of a list in reverse order.

    This function takes a list of integers as an argument and prints each
    integer in reverse order. The function uses the `reversed` built-in
    function to iterate over the elements of the list in reverse order and
    the `str.format()` method to format the output.
    """
    for i in reversed(my_list):
        print("{:d}".format(i))
