# Code to implement a B-tree 
# Programmed by Cesar lopez
# Last modified March 16, 2019

class BTree(object):
    # Constructor
    def __init__(self,item=[],child=[],isLeaf=True,max_items=5):  
        self.item = item
        self.child = child 
        self.isLeaf = isLeaf
        if max_items <3: #max_items must be odd and greater or equal to 3
            max_items = 3
        if max_items%2 == 0: #max_items must be odd and greater or equal to 3
            max_items +=1
        self.max_items = max_items

def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree    
    for i in range(len(T.item)):
        if k < T.item[i]:
            return i
    return len(T.item)
             
def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.item.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
            
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_items//2
    if T.isLeaf:
        leftChild = BTree(T.item[:mid]) 
        rightChild = BTree(T.item[mid+1:]) 
    else:
        leftChild = BTree(T.item[:mid],T.child[:mid+1],T.isLeaf) 
        rightChild = BTree(T.item[mid+1:],T.child[mid+1:],T.isLeaf) 
    return T.item[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    T.item.append(i)  
    T.item.sort()

def IsFull(T):
    return len(T.item) >= T.max_items

def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.item =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
        
        
def height(T):
    if T.isLeaf:
        return 0
    return 1 + height(T.child[0])
        
        
def Search(T,k):
    # Returns node where k is, or None if k is not in the tree
    if k in T.item:
        return T
    if T.isLeaf:
        return None
    return Search(T.child[FindChild(T,k)],k)
                  
def Print(T):
    # Prints items in tree in ascending order
    if T.isLeaf:
        for t in T.item:
            print(t,end=' ')
    else:
        for i in range(len(T.item)):
            Print(T.child[i])
            print(T.item[i],end=' ')
        Print(T.child[len(T.item)])    
 
def PrintD(T,space):
    # Prints items and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
    else:
        PrintD(T.child[len(T.item)],space+'   ')  
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
            PrintD(T.child[i],space+'   ')
    
def SearchAndPrint(T,k):
    node = Search(T,k)
    if node is None:
        print(k,'not found')
    else:
        print(k,'found',end=' ')
        print('node contents:',node.item)
        
def FindDepth(T, k):
    for a in T.item:
        if a == k:
            return 0
    if T.isLeaf:
        return -1
    depth = 0
    for i in range(len(T.child)):
        depth+=1
        depth + FindDepth(T.child[i],k)
        if FindDepth(T.child[i], k) == -1:
            return -1
    return depth
    
#1
def HeightOfTree(T):
    #this serves as our base case, if it is a leaf, we return 1
    if T.isLeaf:
        return 1
    #we create a variable count to store the length of the height we are at
    count = 1
    #we return our height + a recursive call that will add 1 more if the base case is met, or more if we keep recursing
    #we checked only our left side because it is just the height, we would not need to check more than that.
    return count + HeightOfTree(T.child[0])

#2
def IntoSort(T, s):
    #if we reach this case, that means that we append our shorted values first to be ordered.
    if T.isLeaf:
        for x in range(len(T.item)):
            s.append(T.item[x])
        #no need to return our list here because it was updated in here either way
        return
    #this for loop allows us to go through our t.item and append those items after we reach the base case of the lower numbers.
    for i in range(len(T.item)):
        IntoSort(T.child[i], s)
        s.append(T.item[i])
    #this call here allows us to add our left side into the list.
    IntoSort(T.child[-1], s)
    return s

#3
def MinAtD(T, d):
    #if d == 0 that means we found our location, and we return t.item[0] because thats our lowest number
    if d == 0:
        return T.item[0]
    #we return our lowest number because that means we if we reach a leaf because that means there isn't anything lower
    if T.isLeaf:
        return T.item[0]
    #we recurse to our left because that is where our lowest number is
    return MinAtD(T.child[0], d-1)

#4
def MaxAtD(T, d):
    #if d == 0 that means we found which level our number will be at, and we return .item[-1] because that returns the last number in the list
    if d == 0:
        return T.item[-1]
    #we return our highest number on t.item because we reached a leaf and there is nothing bigger
    if T.isLeaf:
        return T.item[-1]
    #we recurse to the right because that is where our largest number is at
    return MaxAtD(T.child[-1], d-1)

#5
def NumOfNodes(T, d):
    #we create count to hold the nodes that we count
    count = 0
    #if we find the given length, we update count for the length of T.item
    if d == 0:
        for i in range(len(T.item)):
            count+=1
        return count
    #if we reach a leaf, we return 0 because that means there was nothing in the length we searched for
    if T.isLeaf:
        return 0
    #this updates count for all the children
    for x in range(len(T.child)):
        count +=NumOfNodes(T.child[x], d-1)
    return count

#6
def printNodes(T, d):
    #if we reach the length that we are given, we print all our items in the length given.
    if d == 0:
        for i in range(len(T.item)):
            print(T.item[i])
    #we iterate to get to the length we were given.if we dont, nothing happens
    for x in range(len(T.child)):
        printNodes(T.child[x], d-1)

#7
def FullNodes(T):
    #this base case checks if we have max items in our node that we are on, we return 1
    if len(T.item) == T.max_items:
        return 1
    #if we reach this case, that means that there is no full nodes, we return 0
    if T.isLeaf:
        return 0
    full = 0
    #full holds the amount of nodes that we have full when we return 1 and we add all full nodes, if nothing, we returned 0, and full is 0
    for i in range(len(T.child)):
        full+=FullNodes(T.child[i])
    return full

#8
def FullLeafs(T):
    #we have have 2 cases, we return 1 only when we have a leaf, and it is full.
    if T.isLeaf:
        if len(T.item) == T.max_items:
            return 1
    full = 0
    #we use this loop to iterate and we update full if we have any leaf with full nodes.
    for i in range(len(T.child)):
        full += FullLeafs(T.child[i])
    return full
      
#9
def Kdepth(T, k):
    #here we iterate through our current node and checks if we have k in it.
    for x in range(len(T.item)):
        if T.item[x] == k:
            return 0
        #if we find a leaf, that means we didnt find k and we return -1
    if T.isLeaf:
        return -1
    #we use this to iterate to the left if k is on the left side, checks if we found -1 to return it, or if not.
    if k >T.item[-1]:
        depth = Kdepth(T.child[-1],k)
        if depth == -1:
            return -1
        return 1+depth  
    #we use this to iterate through our items and if we find that k is lower than where we are, we iterate recursively.
    for i in range(len(T.item)):
        if k <T.item[i]:
            depth = Kdepth(T.child[i],k)
            if depth == 0:
                return depth+1
        #this checks if we have -1 to return it, or we return the depth where found.
    if depth<0:
        return -1
    return depth+1

L = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80, 110, 120, 1, 11 , 3, 4, 5,105, 115, 200, 2, 45, 6]
T = BTree()    
for i in L:
    print('Inserting',i)
    Insert(T,i)
    PrintD(T,'') 
    #Print(T)
    print('\n####################################')
    
SearchAndPrint(T,60)
SearchAndPrint(T,200)
SearchAndPrint(T,25)
SearchAndPrint(T,20)
li = []
print(height(T))
print()
print("1. Height of the tree")
print("#########################")
print(HeightOfTree(T))
print()
print("2. Sorted list")
print("############################")
li = IntoSort(T, li)
print(li)
print()
print("3. min")
print("#######################")
print(MinAtD(T, 2))
print()
print("4. max")
print("#######################")
print(MaxAtD(T, 2))
print()
print("5. Num of Nodes")
print("#######################")
print(NumOfNodes(T, 0))
print()
print("6. print nodes at d")
print("#######################")
printNodes(T, 1)
print()
print("7. Number of full nodes")
print("#######################")
print(FullNodes(T))
print()
print("8. Number of full leafs")
print("#######################")
print(FullLeafs(T))
print()
print("9. depth found at")
print("#######################")
print(Kdepth(T, 58))
print()
print(T.child[0].item[0])
print(T.child[1].item[0])
