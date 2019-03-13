# Code to implement a binary search tree 
# Programmed by Cesar Lopez
# Last modified February 27, 2019
import matplotlib.pyplot as plt

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

def Find(T,k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item == k:
        return T
    if T.item<k:
        return Find(T.right,k)
    return Find(T.left,k)

def FindIter(T, k):
    if T is None or T.item == k:
        return T
    while T is not None:
        if T.item==k:
            return T
        if T.item < k:
            T = T.right
        else:
            T = T.left
    return None
    
def FindAndPrint(T,k):
    f = Find(T,k)
    if f is not None:
        print(f.item,'found')
    else:
        print(k,'not found')
        
def Drawing(ax, x, y, T, r):
    #makes sure to iterate only when our node is not none
    if T is not None:
        c= plt.Circle([x,y], .5, color='k', fill=False)#Creates a circle which we use for out tree
        ax.add_artist(c)#adds the circle into the figure
        ax.text(x-.2, y+.2, T.item, size=10) #we use this to place our text into the image
        if T.left is not None:
            #with this line of code, we plot our left side of the tree
            ax.plot((x, x-r),(y,y-2),color='k')
            #checks our right side, to plot it.
            if T.right is not None:
                #with this line of code, we plot our right side of the tree
                ax.plot((x, x+r),(y,y-2),color='k')
                #this is our first recursive case, which recurses to the right side of the binary tree
                Drawing(ax, x+r, y-2, T.right, r/2)
                #this is our second recursive case, which recurses to the left side of the binary tree
                Drawing(ax, x-r, y-2, T.left, r/2)
            #draws our left side
        #if right side is none, we use this to plot left side
        if T.left is not None:
            #with this line of code, we plot our left side of the tree
            Drawing(ax, x-r, y-2, T.left, r/2)
        
def Balance(a, z):
    #only allows us to work on the list if the list is greater than 0
    if(len(a) > 0):
        #creates mid to help us get our pivot which is the middle value of the list
        mid = (len(a)//2)
        #checks len if it is 1 because then we will only have 1 value in the list
        if len(a) == 1:
            z = BST(a[mid])
            return z
        #checks if len is 2 because we will have 2 values, we append the last value first, and then the 1st value to left because it is less than the first in the list.
        if len(a) == 2:
            z = BST(a[mid])
            z.left = BST(a[0])
            return z
        #we append our middle value to our balance tree, and next we iterate recursively to the left and the right with z.left, z.right
        #we also use list splicing to split our list, we make sure to avoid using the middle value again to make sure we do not add it twice to the node
        z = BST(a[mid])
        z.left = Balance(a[0:mid], z.left)
        z.right = Balance(a[mid+1:], z.right)
        return z
    
def LFT(T, a):
    #checks if our node is none, if it is, we return our list
    if T is None:
        return a
    #this allows us to operate on the list as long as it is not none.
    #we recursively go to the left side first and append our left most item first because it is the smalles and we build up from there
    #next we append our item value that we have to get our middle
    #and last we iterate to the right to get the values that our to the right
    if T is not None:
        LFT(T.left, a)
        a.append(T.item)
        LFT(T.right, a)
        return a

            
def KeysAtDepths(T, i):
    if T is not None:
        print("Keys at depth ",i,": ",T.item)
        KeysAtDepths(T.right,i+1)
        KeysAtDepths(T.left,i+1)
    
    
# Code to test the functions above
T = None
A = [70, 50, 90, 130, 150, 40, 10, 30, 100, 180, 45, 60, 140, 42]
for a in A:
    T = Insert(T,a)
    
InOrder(T)
print()
InOrderD(T,'')
print()

print(SmallestL(T).item)
print(Smallest(T).item)

FindAndPrint(T,40)
FindAndPrint(T,110)

n=60
print('Delete',n,'Case 1, deleted node is a leaf')
T = Delete(T,n) #Case 1, deleted node is a leaf
InOrderD(T,'')
print('####################################')

n=90      
print('Delete',n,'Case 2, deleted node has one child')      
T = Delete(T,n) #Case 2, deleted node has one child
InOrderD(T,'')
print('####################################')

n=70      
print('Delete',n,'Case 3, deleted node has two children') 
T = Delete(T,n) #Case 3, deleted node has two children
InOrderD(T,'')

n=40      
print('Delete',n,'Case 3, deleted node has two children') 
T = Delete(T,n) #Case 3, deleted node has two children
InOrderD(T,'')
print("search in iterator way ###############")
print(FindIter(T, 50))
print("print D ##############")
D = None
ne = [10, 4, 15, 2, 3, 8, 5, 7, 9, 1, 12, 18]
for NE in ne:
    D = Insert(D, NE)
InOrderD(D,'')
print("tree of D #############")
plt.close("all")
fig, ax = plt.subplots()
x = 5
Drawing(ax, x, 10, D, x/2)
print("B tree ##############")
order = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
z = BST
z = Balance(order, z)
InOrder(z)
print("")
InOrderD(z,'')
print("List from Tree ###########")
empty = []
empty = LFT(T, empty)
print(empty)
print("Keys at depth ##############")
KeysAtDepths(T, 0)
