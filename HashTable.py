import random
import time
import matplotlib.pyplot as plots

class HashTable:
     
    def __init__(self):
        self.MAX = 509
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val    
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None
        
        
# Function to display hashtable 
def display_hash(hashTable): 
    
    for i in range(len(hashTable)): 
        print(i, end = " ") 
        
        for j in hashTable[i]: 
            print("-->", end = " ") 
            print(j, end = " ") 
            
        print() 

# Creating Hashtable as 
# a nested list. 
HashTable = [[] for _ in range(509)] 

# Hashing Function to return 
# key for every value. 
def Hashing(keyvalue): 
    return keyvalue % len(HashTable) 


# Insert Function to add 
# values to the hash table 
def insert(Hashtable, keyvalue, value): 
    
    hash_key = Hashing(keyvalue) 
    Hashtable[hash_key].append(value) 

sum_time = 0
start_time = time.time()

inp = int(random.uniform(16385, 65335))
# Driver Code 
insert(HashTable, 10, inp) 
insert(HashTable, 25, inp) 
insert(HashTable, 20, inp) 
insert(HashTable, 9, inp) 
insert(HashTable, 21, inp) 
insert(HashTable, 21, inp) 

display_hash (HashTable) 
end_time = time.time()
elapsed_time = end_time - start_time
elapsed_time_milliSeconds = elapsed_time * 1000
sum_time = sum_time + elapsed_time_milliSeconds
