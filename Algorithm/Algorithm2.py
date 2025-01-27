#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pandas


# In[2]:


import pandas as pd


# In[3]:


retailData = pd.read_csv("geolytix_retailpoints_v25_202209.csv")
retailData


# In[2]:


#This is the hash function with 2 parameters.
#Key and size are the parametres.
def hash_function(key, size):
    return hash(key) % size
#This function is used to calculate the index for the given key.
#Checks if there is a collision in that index.
#Inserts a key-value pair.
def insert_into_hashtable(hashtable, key, value):
    index = hash_function(key, len(hashtable))
    if hashtable[index] is None:
        hashtable[index] = [(key, value)]
    else:
        hashtable[index].append((key, value))
# This function calculates the index for a given key using hash function.
# Checks if there is a non-empty list.
# Returns the values associated with the key if found.
def retrieve_from_hashtable(hashtable, key):
    index = hash_function(key, len(hashtable))
    if hashtable[index] is not None:
        return [info[1] for info in hashtable[index] if info[0] == key]
    else:
        return None

# Read the CSV file into a pandas DataFrame
retailData = pd.read_csv("geolytix_retailpoints_v25_202209.csv")

# Create a dictionary and use it as a hashtable
hashtable_dict = [None] * 1000  # Adjust the size as needed

# Populate the hashtable with data from the retailData DataFrame
for index, row in retailData.iterrows():
    retailer = str(row['retailer'])
    postcode = str(row['postcode'])
    key = f"{retailer.strip().lower()}_{postcode.strip().lower()}"
    value = {
        'store_name': row['store_name'],
        'address': f"{row['add_one']}, {row['town']}, {postcode}",
        'size_band': row['size_band']
    }
    insert_into_hashtable(hashtable_dict, key, value)

# Example of retrieving information based on a retailer's name and postcode
while True:
    retailer_name_to_lookup = input("Enter the retailer's name: ").strip().lower()
    postcode_to_lookup = input("Enter the postcode: ").strip().lower()
    key_to_lookup = f"{retailer_name_to_lookup}_{postcode_to_lookup}"

    retrieved_info_list = retrieve_from_hashtable(hashtable_dict, key_to_lookup)

    # Displaying the output or prompting to try again
    if retrieved_info_list:
        for info in retrieved_info_list:
            print(f"Store information for {retailer_name_to_lookup} with postcode {postcode_to_lookup}:")
            print(f"Store Information: {info['store_name']}{info['address']}{info['size_band']}")
        break
    else:
        print(f"Store information for {retailer_name_to_lookup} with postcode {postcode_to_lookup} not found. Please try again.")


# In[ ]:




