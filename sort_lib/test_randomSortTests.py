from numpy import random
from BubbleSort import bubbleSort
from InsertionSort import insertionSort
from QuickSort import quickSort


def test_bubbleSort():
    n = random.randint(100)
    i = random.randint(2147483646, size=(n))
    a = bubbleSort(i)
    for k in range(len(i) - 1):
        print(f"Given: {i}")
        assert a[k] <= a[k + 1]


def test_insertionSort():
    n = random.randint(100)
    i = random.randint(2147483646, size=(n))
    a = insertionSort(i)
    for k in range(len(i) - 1):
        print(f"Given: {i}")
        assert a[k] <= a[k + 1]


def test_quickSort():
    n = random.randint(100)
    i = random.randint(2147483646, size=(n))
    a = quickSort(i, 0, len(i) - 1)
    for k in range(len(i) - 1):
        print(f"Given: {i}")
        assert a[k] <= a[k + 1]
