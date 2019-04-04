# Implementation of hash tables with chaining using strings
#Lab 5
#Cesar Lopez

class HashTableC(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self,size,num_items = 0):  
        self.item = []
        for i in range(size):
            self.item.append([])
        if num_items/size == 1:
            num_items = (num_items*2)+1
        self.num_items = num_items
        
def InsertC(H,k,l):
    # Inserts k in appropriate bucket (list) 
    # Does nothing if k is already in the table
    H.num_items += 1
    b = h(k,len(H.item))
    if H.num_items/len(H.item) == 1:
        for i in range(len(H.item)+1):
            H.item.append([])
        b = h(k,len(H.item))
    H.item[b].append([k,l]) 
   
def FindC(H,k):
    # Returns bucket (b) and index (i) 
    # If k is not in table, i == -1
    b = h(k,len(H.item))
    for i in range(len(H.item[b])):
        if H.item[b][i][0] == k:
            return b, i, H.item[b][i][1]
    return b, -1, -1
 
def h(s,n):
    r = 0
    for c in s:
        r = (r*n + ord(c))% n
    return r

def sim(H, w1, w2):
    e1 = FindC(H, w1)
    e2 = FindC(H, w2)
    h = e1* e2
    return h

import numpy as np
'''
choice = input("Type 1 for Binary Search Tree, or 2 for Hash Table with chaining")
print(choice)
if(choice == '1'):
    print("Your choice is: Binary Search Tree")
elif(choice == '2'):
    print("Your choice is: Hash Table")
else:
    print("Choose either 1 or 2")
'''
a = []
H = HashTableC(13)
embed = np.empty(50)
f = open('glove.6B.50d.txt', encoding='utf-8')
for line in f:
    a = line.split(' ')
    word = a[0]
    e = a[1:-1]
    InsertC(H, word, e)
print(len(H.item))
print(FindC(H, "the"))
file = open('input.txt', encoding='utf-8')
for lin in file:
    b = line.split(' ')
    word1 = b[0]
    word2 = b[1]
    print(sim(H, word1, word2))
