from numpy import random
from sort_lib.int_sort import bubble
from sort_lib.int_sort import quick
from sort_lib.int_sort import insertion


def test_bubble():
    n = random.randint(100)
    i = random.randint(2147483646, size=(n))
    a = bubble(i)
    for k in range(len(i) - 1):
        print(f"Given: {i}")
        assert a[k] <= a[k + 1]


def test_insertion():
    n = random.randint(100)
    i = random.randint(2147483646, size=(n))
    a = insertion(i)
    for k in range(len(i) - 1):
        print(f"Given: {i}")
        assert a[k] <= a[k + 1]


def test_quick():
    n = random.randint(100)
    i = random.randint(2147483646, size=(n))
    a = quick(i, 0, len(i) - 1)
    for k in range(len(i) - 1):
        print(f"Given: {i}")
        assert a[k] <= a[k + 1]
