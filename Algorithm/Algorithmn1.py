#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


# This is used to read the CSV file.
retailData = pd.read_csv("geolytix_retailpoints_v25_202209.csv")


# In[4]:



# Postcodes are converted as strings.
postcodes = retailData['postcode'].astype(str).unique().tolist()

# Bubble Sort Algorithm
def bubble_sort(arr):
    n = len(arr)
    steps = 0  # This is a variable to count steps.
    for i in range(n):
        for j in range(0, n - i - 1):
            steps += 1  # This is used to count each comparison.
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return steps

# This is used to get the number of steps.
sorting_steps = bubble_sort(postcodes)

# Binary Search Algorithm
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    steps = 0  # This is a variable to count steps.

    while low <= high:
        steps += 1  # This is used to count each comparison.
        mid = (low + high) // 2
        if arr[mid].startswith(target):
            return steps  # This is used to return the number of steps when the optimal amont is found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return steps  # This returns the number of steps if the number is not found.

# This is used to get number of steps of the postcodes starting with NW10
search_target = "NW10"
binary_search_steps = binary_search(postcodes, search_target)

# This is the output that adds the number of steps from both algothims.
total_steps = sorting_steps + binary_search_steps
print(f"Sorting steps: {sorting_steps}")
print(f"Binary search steps for postcodes starting with {search_target}: {binary_search_steps}")
print(f"Total steps: {total_steps}")


# In[ ]:




