import random
import time

#Implement masive search
def naive_search(l, target):
    for i in range (len(l)):
        if l[i] == target:
            return i

    return -1

#Starts the binary search taking midpoints to find the number faster
def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) -1
    
    if high < low:
        return -1

    #getting the midpoint
    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        new_high = midpoint - 1
        return binary_search(l, target, low, new_high)
    else:
        #Target > l(midpoint)
        new_low = midpoint + 1
        return binary_search(l, target, high, new_low)

if __name__ == '__main__':

    #Defines the target number from a random list
    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    target_list = [random.randint(-3*length, 3*length) for _ in range(length)]

    #Takes time from the naive search and prints the target defined
    start = time.time()
    for target in target_list:
        naive_search(sorted_list, target)
    end = time.time()
    naive_time = float(end - start)
    print(f"The number was: {target}")
    print(f"Naive Search time: {round(naive_time, 7)} seconds")
    
    #Takes time from the binary search and prints the target defined
    start = time.time()
    for target in target_list:
        binary_search(sorted_list, target)
    end = time.time()
    binary_time = float(end - start)
    print(f"Binary Search time: {round(binary_time, 7)} seconds")

    #Prints the difference between the time in the naive search and binary search
    print(f"The Binary Search found the number {round(naive_time - binary_time, 7)} seconds before the Naive Search :O")