#Cesar Lopez
#Lab 2 
#Node Functions

class Node(object):
    # Constructor
    def __init__(self, item, next=None):  
        self.item = item
        self.next = next 
        
def PrintNodes(N):
    if N != None:
        print(N.item, end=' ')
        PrintNodes(N.next)
        
def PrintNodesReverse(N):
    if N != None:
        PrintNodesReverse(N.next)
        print(N.item, end=' ')
        
#List Functions
class List(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None
        
def IsEmpty(L):  
    return L.head == None     
        
def Append(L,x): 
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next
        
def Print(L):
    # Prints list L's items in order using a loop
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line 

def PrintRec(L):
    # Prints list L's items in order using recursion
    PrintNodes(L.head)
    print() 
    
def Remove(L,x):
    # Removes x from list L
    # It does nothing if x is not in L
    if L.head==None:
        return
    if L.head.item == x:
        if L.head == L.tail: # x is the only element in list
            L.head = None
            L.tail = None
        else:
            L.head = L.head.next
    else:
         # Find x
         temp = L.head
         while temp.next != None and temp.next.item !=x:
             temp = temp.next
         if temp.next != None: # x was found
             if temp.next == L.tail: # x is the last node
                 L.tail = temp
                 L.tail.next = None
             else:
                 temp.next = temp.next.next
         
def PrintReverse(L):
    # Prints list L's items in reverse order
    PrintNodesReverse(L.head)
    print()     
       
def Median(L):
    #sets temp as head, then calls get element, whick returns the element at the length of temp/2, which is the middle
    temp = L.head
    return ElementAt(temp,GetLength(temp)//2)
    
#Gets the length of our nodes, if empty, returns 0
    # creates n, creates temp, and while temp is not equal to none, updates both n and temp, until None is reached.
def GetLength(L):
    if L is None:
        return 0
    else:
        n = 0
        temp = L.head
        while temp is not None:
            n +=1
            temp = temp.next
        return n
#uses while loop to find the location of the element at location n.
        #Checks if c is None, and if yes, returns None
def ElementAt(c, n):
    if(c is None):
        return None
    else:
        while(n > 0):
            c = c.next
            n-=1
    return c.item

#Splits list into 2 pieces, lower, and upper. 
    #creates I and J to hold length, and half the length.
    #uses n to get the first half, and uses n to get second half.
    #Appends left for all values less than half, and right for values bigger than half
    #returns the 2 new list
def Split(L):
    temp = L.head
    left = List()
    right = List()
    i = GetLength(L)
    j = GetLength(L)//2
    n = 0
    while n < j:
        Append(left, temp.item)
        n+=1
        temp = temp.next
    while n < i:
        Append(right, temp.item)
        n+=1
        temp = temp.next
    return left, right


def BubbleSort(L, n):
    unsorted = True 
    while unsorted:#Uses while loop to proceed until no longer able to
        temp = L.head 
        unsorted = False
        while temp.next is not None:
            n+=1
            if temp.item > temp.next.item:#Swaps if current item is greater than next item
                temp2 = temp.item
                temp.item = temp.next.item
                temp.next.item = temp2
                unsorted = True#Allows us to keep doing the while loop
            temp = temp.next
    return temp, n

def MergeSort(L, n):
    n +=1
    if L is None or GetLength(L) == 1:
        return L
    else:
        l1, l2 = Split(L)#splits list into 2
        MergeSort(l1, n)#calls recursive calls for left and right list(s)
        MergeSort(l2, n)
        merged = List()
        merged = Merge(l1, l2, n)#calls merge method, which merges the 2 list and compares
        return merged, n
        
def Merge(l, r, n):
    merge = List()
    left = l.head
    right = r.head
    while(left is not None and right is not None):
        if(left.item > right.item):#checks if left list is bigger than right, and appends right to new list if true
            n+=1
            Append(merge, right.item)
            right = right.next
        else:#else statement that appends left to the new list if the first case is false
            n+=1
            Append(merge, left.item)
            left = left.next
    while(left is not None):#appends leftover items
        n+=1
        Append(merge, left.item)
        left = left.next
    while(right is not None):#appends leftover items
        n+=1
        Append(merge, right.item)
        right = right.next
    return merge, n    
            
def QuickSort(L, n):#checks for empty list
    if(L is None or IsEmpty(L)):
        return L
    else:
        hold = Pivot(L)#gathers pivot (last node)
        temp = L.head
        high = List()
        low = List()
        i = GetLength(L)-1#allows us to stop before reaching the last node
        j = 0
        hic = 0#high counter
        loc = 0#low counter
        while(j<i):
            if(hold > temp.item):#checks if item is less than pivot, and is placed in lower list if true
                Append(low, temp.item)
                temp = temp.next
                j+=1
                n+=1
                loc+=1
            else:#if item is greater than pivot, it is placed in the higher list
                Append(high, temp.item)
                temp = temp.next
                j+=1
                n+=1
                hic+=1
        QuickSort(low, n)#recurses both new list
        QuickSort(high, n)
        if(loc < hic):#checks if pivot is going to left or right list
            Prepend(high, temp.item)
            n+=1
            merged = List()
            merged = Merge(low, high, n)
            return merged, n
        else:#if pivot did not go into high list, it goes here, to the low list
            Append(low, temp.item)
            n+=1
            merged = List()
            merged = Merge(low, high, n)
            return merged, n
        #prepend method, to add things at the fornt of a list
def Prepend(L,x):
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.head=Node(x,L.head)
            #gets us the last node item
def Pivot(L):
    n = GetLength(L)-1
    temp = L.head
    for i in range(n):
        temp = temp.next
    return temp.item

#incomplete, but tried following instructions
def Mod(L, n):
    p = Pivot(L)
    m = Median(L)
    e = List()
    for i in range(m):
        n+=1
        if(p > L.head.item):
            Append(e, L.head.item)
            L.head = L.head.next
        else:
            L.head = L.head.next
    Mod(e, n)
    return e, n

L = List()
print(IsEmpty(L))
for i in range(5):
    Append(L,i)
Print(L)
PrintRec(L)
PrintReverse(L)
BubbleSort(L, 0)
MergeSort(L, 0)
QuickSort(L, 0)
#Mod(L, 0)
