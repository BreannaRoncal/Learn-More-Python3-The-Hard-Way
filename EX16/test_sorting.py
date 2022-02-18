from sorting import *
from random import randint

#choose how long the list to sort is
MAX_LEN = 30

#make random list of integers
def randomList(list_size):
    numbers = []
    for i in range(list_size):
        numbers.append(randint(0, 10000))
    return numbers

def testBubbleSort():
    print("test: Bubble Sort")
    numbers = randomList(MAX_LEN)
    #print("BEFORE:" + str(numbers))
    bubbleSort(numbers)
    #print("AFTER: " + str(numbers))
    assert isSorted(numbers) == True
    print("Pass Bubble Sort test")

#check to make sure it is sorted
def isSorted(numbers):
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True

testBubbleSort()
