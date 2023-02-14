import json
import matplotlib.pyplot as plt
import time
import sys
sys.setrecursionlimit(20000)

with open("ex2.json", "r") as file:
    text = json.load(file)

import random

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi - 1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    pivindx = random.randint(start, end)
    pivot = array[pivindx]
    array[pivindx], array[start] = array[start], array[pivindx]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


arrays = []
index = []

for i in range(len(text)):
    arr = text[i]
    start_time = time.perf_counter()
    func1(text[i], 0, len(text[i]) - 1)
    end_time = time.perf_counter()
    
    total_time = end_time - start_time
    arrays.append(total_time)
    index.append(len(arr))
    
print("Time taken: ", total_time, "seconds")

plt.plot(index, arrays)
plt.xlabel("Index Used")
plt.ylabel("Time taken")
plt.show()