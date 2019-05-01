#Lab7 modify maze
# Programmed by Olac Fuentes
# Last modified April 29, 2019
#Cesar Lopez
#10:30 - 12:00

import matplotlib.pyplot as plt
import numpy as np
import random

def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0  
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols   
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off') 
    ax.set_aspect(1.0)

def wall_list(maze_rows, maze_cols):
    # Creates a list with all the walls in the maze
    w =[]
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w

from scipy import interpolate 

def DisjointSetForest(size):
    return np.zeros(size,dtype=np.int)-1
        
def dsfToSetList(S):
    #Returns aa list containing the sets encoded in S
    sets = [ [] for i in range(len(S)) ]
    for i in range(len(S)):
        sets[find(S,i)].append(i)
    sets = [x for x in sets if x != []]
    return sets

def find(S,i):
    # Returns root of tree that i belongs to
    if S[i]<0:
        return i
    return find(S,S[i])

def find_c(S,i): #Find with path compression 
    if S[i]<0: 
        return i
    r = find_c(S,S[i]) 
    S[i] = r 
    return r
    
def union(S,i,j):
    # Joins i's tree and j's tree, if they are different
    ri = find(S,i) 
    rj = find(S,j)
    if ri!=rj:
        S[rj] = ri

def union_c(S,i,j):
    # Joins i's tree and j's tree, if they are different
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj:
        S[rj] = ri
         
def union_by_size(S,i,j):
    # if i is a root, S[i] = -number of elements in tree (set)
    # Makes root of smaller tree point to root of larger tree 
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj:
        if S[ri]>S[rj]: # j's tree is larger
            S[rj] += S[ri]
            S[ri] = rj
        else:
            S[ri] += S[rj]
            S[rj] = ri

        
def draw_dsf(S):
    scale = 30
    fig, ax = plt.subplots()
    for i in range(len(S)):
        if S[i]<0: # i is a root
            ax.plot([i*scale,i*scale],[0,scale],linewidth=1,color='k')
            ax.plot([i*scale-1,i*scale,i*scale+1],[scale-2,scale,scale-2],linewidth=1,color='k')
        else:
            x = np.linspace(i*scale,S[i]*scale)
            x0 = np.linspace(i*scale,S[i]*scale,num=5)
            diff = np.abs(S[i]-i)
            if diff == 1: #i and S[i] are neighbors; draw straight line
                y0 = [0,0,0,0,0]
            else:      #i and S[i] are not neighbors; draw arc
                y0 = [0,-6*diff,-8*diff,-6*diff,0]
            f = interpolate.interp1d(x0, y0, kind='cubic')
            y = f(x)
            ax.plot(x,y,linewidth=1,color='k')
            ax.plot([x0[2]+2*np.sign(i-S[i]),x0[2],x0[2]+2*np.sign(i-S[i])],[y0[2]-1,y0[2],y0[2]+1],linewidth=1,color='k')
        ax.text(i*scale,0, str(i), size=20,ha="center", va="center",
         bbox=dict(facecolor='w',boxstyle="circle"))
    ax.axis('off') 
    ax.set_aspect(1.0)

#created to display message based on amount of walls wanted to remove
def message(m, n):
    if m < n-1:
        print("A path from source to destination is not guaranteed to exist when: walls removed (your input) < (cells/walls-1)")
    if m == n-1:
        print("There is a unique path from source to destination when: walls removed (your input) = (cells/walls-1)")
    if m > n-1:
        print("There is at least one path from source to destination when: walls removed (your input) > (cells/walls-1)")

#creates adjacent list, takes in original walls, new walls, and number of cells
def AdLi(ow, w, cells):
    adj = [[]for i in range(cells)]#creates 3d list that holds walls as vertices instead of cells
    for j in ow:
        if j not in w:#when a wall is not found in the new walls, they are inserted as an edge
            adj[j[0]].append(j[1])
            adj[j[1]].append(j[0])
    return adj
        
#used pseudocode given in class
def BFS(g, v):
    visited = len(g)*[False]
    prev = len(g)*[-1]
    q = queue.Queue()
    q.put(v)
    visited[v] = True
    while not q.empty():
        u = q.get()
        for t in g[u]:
            if not visited[t]:
                visited[t] = True
                prev[t] = u
                q.put(t)
    return prev

#used pseudocode given in class
def dfsS(g, v):
    s = []#a list in python works like a stack
    visited = len(g)*[False]
    prev = len(g)*[-1]
    s.append(v)
    visited[v] = True
    while len(s) is not 0:
        u = s.pop()
        for t in g[u]:
            if not visited[t]:
                visited[t] = True
                prev[t] = u
                s.append(t)
    return prev

#used pseudocode given in class
def dfsR(g, v, visited, prev):
    visited[v] = True
    for t in g[v]:
        if not visited[t]:
            prev[t] = v
            dfsR(g, t, visited, prev)
    return prev
#######################################
import queue
plt.close("all") 
maze_rows = 10
maze_cols = 5

walls = wall_list(maze_rows,maze_cols)
S = DisjointSetForest(maze_rows*maze_cols)
draw_maze(walls,maze_rows,maze_cols,cell_nums=True) 
d = random.randint(0, len(walls)-1)
OrigW = walls.copy()

print("There is:",maze_rows*maze_cols,"cells/walls")
m = (int)(input("How many walls would you like to remove?"))
print(m, "walls will be removed")
message(m, (maze_rows*maze_cols))

while(m>0):
    d = random.randint(0,len(walls)-1)
    hold = walls[d]
    if find(S, hold[0]) != find(S, hold[1]):
        walls.pop(d)
        union(S, hold[0], hold[1])
        m -= 1
#hold of adjacent list
adj = AdLi(OrigW, walls, maze_rows*maze_cols)
print(adj)
print("breadth",BFS(adj, 0))
#declared here instead of creating global variables, used for recursive method
#v = visited, and p = previous
v = len(adj)*[False]
p = len(adj)*[-1]
print("stack", dfsS(adj, 0))
print("recursive", dfsR(adj, 0, v, p))
draw_maze(walls,maze_rows,maze_cols) 
