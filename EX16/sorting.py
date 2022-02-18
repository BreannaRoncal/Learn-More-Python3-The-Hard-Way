#Bubble, Quick, and Merge Sort on a random list of integers
#sort list from least to greatest

def bubbleSort(numbers):
    #length of numbers list
    n = len(numbers)
    
    while True:
        #if there are no swaps, then the list is sorted
        is_sorted = True
        
        #go through the while list
        for i in range(n-1):
            #swap if not in order
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                is_sorted = False
        if is_sorted:
            break
