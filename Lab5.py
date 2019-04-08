# Implementation of hash tables with chaining using strings
#Lab 5
#Cesar Lopez
#Professor - Olac Fuentes
#TA - Anadita
#Class - 10:30 - 12:00

class HashTableC(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self,size):  
        self.item = []
        self.num_items = 0#used to keep track of number of items, used for load factor
        for i in range(size):
            self.item.append([])
        
def InsertC(H,k,l):
    # Inserts k in appropriate bucket (list) 
    # Does nothing if k is already in the table
    H.num_items += 1#used to update and check load factor
    b = h(k,len(H.item))
    if H.num_items/len(H.item) >= 1:#checks load factor
        for i in range(len(H.item)+1):#updates hash table length with empty nodes
            H.item.append([])
    H.item[b].append([k,l]) 
   
def FindC(H,k):
    # Returns bucket (b) and index (i) 
    # If k is not in table, i == -1
    b = h(k,len(H.item))
    for i in range(len(H.item[b])):
        if H.item[b][i][0] == k:
            return H.item[b][i][1]#updated to return array of numbers instead of extra stuff
    return -1#returns -1 like stated in comments above.
 
def h(s,n):
    r = 0
    for c in s:
        r = (r*n + ord(c))% n
    return r

def dotProduct(w1, w2):#uses for loop to iterate the 2 arrays and gets do product
    hold = 0
    for i in range(len(w1)):
        hold += float(w1[i])*float(w2[i])
    return hold

def magni(w):#gets out magnitude, **2 is squared, and sqrt gets our square root
    hold = 0
    for i in range(len(w)):
        hold += float(w[i]) ** 2
    return math.sqrt(hold)

def sim(H, w1, w2):#here we determine our similarities. First we get do product, next we get magnitudes, and lastly divide dot product my both magnitudes
    e1 = FindC(H, w1)
    e2 = FindC(H, w2)
    dp = dotProduct(e1, e2)
    m1 = magni(e1)
    m2 = magni(e2)
    return dp/(m1*m2)

def IsEmpty(H):#checks for our empty nodes in our hash table
    count = 0
    for i in range(len(H.item)):
        if len(H.item[i]) <= 0:
            count += 1
    return count

# Code to implement a binary search tree 
# Programmed by Olac Fuentes
# Last modified February 27, 2019

class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

def Delete(T,del_item):
    if T is not None:
        if del_item < T.item:
            T.left = Delete(T.left,del_item)
        elif del_item > T.item:
            T.right = Delete(T.right,del_item)
        else:  # del_item == T.item
            if T.left is None and T.right is None: # T is a leaf, just remove it
                T = None
            elif T.left is None: # T has one child, replace it by existing child
                T = T.right
            elif T.right is None:
                T = T.left    
            else: # T has two chldren. Replace T by its successor, delete successor
                m = Smallest(T.right)
                T.item = m.item
                T.right = Delete(T.right,m.item)
    return T
         
def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.item,end = ' ')
        InOrder(T.right)
  
def InOrderD(T,space):
    # Prints items and structure of BST
    if T is not None:
        InOrderD(T.right,space+'   ')
        print(space,T.item)
        InOrderD(T.left,space+'   ')
  
def SmallestL(T):
    # Returns smallest item in BST. Returns None if T is None
    if T is None:
        return None
    while T.left is not None:
        T = T.left
    return T   
 
def Smallest(T):
    # Returns smallest item in BST. Error if T is None
    if T.left is None:
        return T
    else:
        return Smallest(T.left)

def Largest(T):
    if T.right is None:
        return T
    else:
        return Largest(T.right)   

def Find(T,k):#updated to check T.item[0] instead of T.item, because T.item[0] is where our string is located
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item[0] == k:
        return T.item
    if T.item[0]<k:
        return Find(T.right,k)
    return Find(T.left,k)

def NumNodes(T):#counts our number of nodes with our return statement, base case checks for empty nodes and returns 0 if found any
    if T is None:
        return 0
    return NumNodes(T.left) + NumNodes(T.right)+1
    
def FindAndPrint(T,k):
    f = Find(T,k)
    if f is not None:
        print(f.item,'found')
    else:
        print(k,'not found')
        
def HeightT(T):#we have 2 holds that checks if either is larger than the other, if one is larger, that gives us our larger end of the height, and we add up the larger.
    hold = 0
    hold1 = 0
    if T is None:
        return 0
    hold += HeightT(T.left)
    hold1 += HeightT(T.right)
    if(hold > hold1):
        return 1+hold
    else:
        return 1+hold1

def BSTDot(w1, w2):#dot product but for our bst, similar to hash one
    i = 1
    hold = 0 
    while i<len(w1):
        hold+= float(w1[i])*float(w2[i])
        i +=1
    return hold

def BSTMagni(w):#magnitude but for our bst, similar to hash one
    i = 1
    hold = 0
    while i<len(w):
        hold+=float(w[i])**2
        i += 1
    return math.sqrt(hold)

def BSTSim(T, w1, w2):#comparison method for bst's, similar to hash one
    e1 = Find(T, w1)
    e2 = Find(T, w2)
    dp = BSTDot(e1, e2)
    m1 = BSTMagni(e1)
    m2 = BSTMagni(e2)
    return dp/(m1*m2)
    

import math
import time
choice = input("Type 1 for Binary Search Tree, or 2 for Hash Table with chaining")
print("Your choice is: ",choice)
if(choice == '1'):
    print("Your choice is: Binary Search Tree")
    print()
    print("Building Binary Search Tree..")
    start = time.time()
    T = None
    f = open('glove.6B.50d.txt', encoding='utf-8')#opens file and we read it, store it into an array, and splice it to store into bst
    for line in f:
        a = line.split(' ')
        T = Insert(T, a)
    print("Binary Search Tree stats:")
    print("Number of nodes: ", NumNodes(T))
    print("Height of Tree: ", HeightT(T))
    print("Running time for Binary Search Tree construction ", time.time()-start)
    file = open('input.txt', encoding='utf-8')
    for lin in file:
        b = lin.split()
        print("Similarity [",b[0],", ", b[1],"] =",end=" ")#we compare the line with 2 words in it
        print(BSTSim(T, b[0], b[1]))
elif(choice == '2'):
    print("Your choice is: Hash Table")
    start = time.time()
    print()
    print("Building Hash Table...")
    H = HashTableC(13)
    f = open('glove.6B.50d.txt', encoding='utf-8')#opens file and we read it, store it into an array, and splice it to store into our hash
    for line in f:
        a = line.split(' ')
        word = a[0]
        embed = a[1:]
        InsertC(H, word, embed)
    print("Hash Table Stats:")
    print("Initial Size: 13")
    print("final size: ",len(H.item))
    print("Load Factor: ", H.num_items/len(H.item))
    print("Percentage of Empty list", (IsEmpty(H)/len(H.item))*100)
    print("Standard Deviation of Lengths of list: ")
    file = open('input.txt', encoding='utf-8')
    for lin in file:
        b = lin.split()
        print("Similarity [",b[0],", ", b[1],"] =",end=" ")#we compare the line with 2 words in it
        print(sim(H, b[0], b[1]))
        print()
    print("Time: ",time.time()-start)
else:
    print("Wrong input, relaunch and try again.")
