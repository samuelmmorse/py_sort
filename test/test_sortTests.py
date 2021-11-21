# Python program for PyTest testing of bubblesort,
# insertionsort, and quicksort python functions

# These functions create an unsorted array, then
# sort them through their respective sort functions.
# It then checks against a properly sorted array
# of the same contents.

# Imports the sort functions from the other Py files
from sort_lib.int_sort import bubble
from sort_lib.int_sort import quick
from sort_lib.int_sort import insertion

# PyTest to check if bubble sort works properly
def test_bubble():
    # sets up array to be sorted
    arr = [7, 5, 1, 3, 4, 8, 2, 6]
    # sorts array
    bubble(arr)
    # correctly sorted array
    testarr = [1, 2, 3, 4, 5, 6, 7, 8]
    # checks if they are equal
    assert arr == testarr


# PyTest to check if insertion sort works properly
def test_insertion():
    # sets up array to be sorted
    arr = [7, 5, 1, 3, 4, 8, 2, 6]
    # sorts array
    insertion(arr)
    # correctly sorted array
    testarr = [1, 2, 3, 4, 5, 6, 7, 8]
    # checks if they are equal
    assert arr == testarr


# PyTest to check if quick sort works properly
def test_quickSort():
    # sets up array to be sorted
    arr = [7, 5, 1, 3, 4, 8, 2, 6]
    # sorts array
    n = len(arr)
    quick(arr, 0, n - 1)
    # correctly sorted array
    testarr = [1, 2, 3, 4, 5, 6, 7, 8]
    # checks if they are equal
    assert arr == testarr
