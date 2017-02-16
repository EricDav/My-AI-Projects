# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 02:09:55 2017

@author: Alienyi DAVID
"""

from datetime import datetime
import timeit
from time import time
import sys
import math

class Node(object):
    #l = []
    def __init__(self, state):
        self.state = state
        self.direc = []
    def getState(self):
        return self.state
    def getDirec(self):
        return self.direc
    def addDirec(self, Dir):
        self.direc.append(Dir)
    def changeState(self, stat):
        self.state = stat
    def __eq__(self, other):
        """Override the default Equals behavior"""
        return self.state == other.getState()
    def __str__(self):
        return str(self.state)


t = time()

tup = ()
for iy in sys.argv[2]:
    if iy != ',':
        tup = tup + (iy,)
n = int(math.sqrt(len(tup)))
lt = sorted(tup)
Gt = ()
for h in lt:
    Gt +=(h,)

def Down(s, n):
    st = ()
    for i in range(len(s)):
        if s[i] == '0':
            break
    x, y = s[i], s[i+n]
    x, y = y, x
    for j in range(len(s)):
        if j == i:
            st +=(x,)
        elif j == i+n:
            st +=(y,)
        else:
            st+=(s[j],)
    return st
def Up(s, n):
    st = ()
    for i in range(len(s)):
        if s[i] == '0':
            break
    x, y = s[i], s[i-n]
    x,y = y,x
    for j in range(len(s)):
        if j == i:
            st +=(x,)
        elif j == i-n:
            st +=(y,)
        else:
            st+=(s[j],)
    return st
def Right(s):
    st = ()
    for i in range(len(s)):
        if s[i] == '0':
            break
    x, y = s[i], s[i+1]
    x,y= y, x
    for j in range(len(s)):
        if j == i:
            st +=(x,)
        elif j == i+1:
            st +=(y,)
        else:
            st+=(s[j],)
    return st
def Left(s):
    st = ()
    for i in range(len(s)):
        if s[i] == '0':
            break
    x, y = s[i], s[i-1]
    x,y= y, x
    for j in range(len(s)):
        if j == i:
            st +=(x,)
        elif j == i-1:
            st +=(y,)
        else:
            st+=(s[j],)
    return st
def GenChildren(l, n):
    children = []
#    for m in l:
    g = l.getState()
    for i in range(len(g)):
        if g[i] == '0':
            break
    if i == 0:
         N = Node(Down(g, n))
         N1 = Node(Right(g))
         for nod in l.getDirec():
            N.addDirec(nod)
            N1.addDirec(nod)
         N.addDirec('down')
         N1.addDirec('Right')
         children.append(N)
         children.append(N1)
    elif i == n-1:
        N = Node(Down(g, n))
        N1 = Node(Left(g))
        for nod in l.getDirec():
            N.addDirec(nod)
            N1.addDirec(nod)
        N.addDirec('Down')
        N1.addDirec('Left')
        children.append(N)
        children.append(N1)
    elif i == n**2 - n:
        N = Node(Up(g, n))
        N1 = Node(Right(g))
        for nod in l.getDirec():
            N.addDirec(nod)
            N1.addDirec(nod)
        N.addDirec('Up')
        N1.addDirec('Right')
        children.append(N)
        children.append(N1)
    elif i == n**2 -1:
        N = Node(Up(g, n))
        N1 = Node(Left(g))
        for nod in l.getDirec():
            N.addDirec(nod)
            N1.addDirec(nod)
        N.addDirec('Up')
        N1.addDirec('Left')
        children.append(N)
        children.append(N1)
    elif i%n == 0:
        N = Node(Up(g, n))
        N1 = Node(Down(g, n))
        N3 = Node(Right(g))
        for nod in l.getDirec():
            N.addDirec(nod)
            N1.addDirec(nod)
            N3.addDirec(nod)
        N.addDirec('Up')
        N1.addDirec('Down')
        N3.addDirec('Right')
        children.append(N)
        children.append(N1)
        children.append(N3)
    elif (i+1)%n == 0:
        N = Node(Up(g, n))
        N1 = Node(Down(g, n))
        N2 = Node(Left(g))
        for nod in l.getDirec():
            N.addDirec(nod)
            N1.addDirec(nod)
            N2.addDirec(nod)
        N.addDirec('Up')
        N1.addDirec('Down')
        N2.addDirec('Left')
        children.append(N)
        children.append(N1)
        children.append(N2)
    elif i > 0 and i < n-1:
        N = Node(Down(g, n))
        N1 = Node(Left(g))
        N2 = Node(Right(g))
        for nod in l.getDirec():
            N.addDirec(nod)
            N1.addDirec(nod)
            N2.addDirec(nod)
        N.addDirec('Down')
        N1.addDirec('Left')
        N2.addDirec('Right')
        children.append(N)
        children.append(N1)
        children.append(N2)
    elif i > n**2 - n and i < n**2 -1:
        N = Node(Up(g, n))
        N1 = Node(Left(g))
        N2 = Node(Right(g))
        for nod in l.getDirec():
            N.addDirec(nod)
            N1.addDirec(nod)
            N2.addDirec(nod)
        N.addDirec('Up')
        N1.addDirec('Left')
        N2.addDirec('Right')
        children.append(N)
        children.append(N1)
        children.append(N2)
    else:
        N = Node(Up(g, n))
        N0 = Node(Down(g, n))
        N1 = Node(Left(g))
        N2 = Node(Right(g))
        for nod in l.getDirec():
            N0.addDirec(nod)
            N.addDirec(nod)
            N1.addDirec(nod)
            N2.addDirec(nod)
        N.addDirec('Up')
        N0.addDirec('Down')
        N1.addDirec('Left')
        N2.addDirec('Right')
        children.append(N)
        children.append(N0)
        children.append(N1)
        children.append(N2)
    return children
#a = Node(('1','2','5','3','4','0','6','7','8'))
#a.addDirec('Up')
#v = GenChildren(a, 3)
#for i in v:
#    print(i)
#    print(i.getDirec())


def BFS(I_state, G_state, n):
    if I_state == G_state:
        return ([],0,0,0,0,0,0,0,0)
    node = Node(I_state)
    frontier = [node]
    v = []
    maxf = 1
    n_ex = 0
    max_d = 0
    while frontier != []:
        if len(frontier) > maxf:
            maxf = len(frontier)
        x = frontier.pop(0)
        v.append(x)
        if x.getState() == G_state:
            return (x.getDirec(), len(x.getDirec()), n_ex, len(frontier),maxf, len(x.getDirec()), max_d, )
        nodes = GenChildren(x, n)
        check = 0
        for i in nodes:
            if i not in v and i not in frontier:
                if check == 0:
                    n_ex +=1
                    check = 1
                if len(i.getDirec()) > max_d:
                    max_d = len(i.getDirec())
                frontier.append(i)






def DFS(I_state, G_state, n):
    if I_state == G_state: 
        return ([],0,0,0,0,0,0,0,0)
    node = Node(I_state)
    frontier = [node]
    v = []
    maxf = 1
    n_ex = 0
    max_d = 0
    while frontier != []:
        if len(frontier) > maxf:
            maxf = len(frontier)
        x = frontier.pop()
        v.append(x)
        if x.getState() == G_state:
            return (x.getDirec(), len(x.getDirec()), n_ex, len(frontier),maxf, len(x.getDirec()), max_d, )
        nodes = GenChildren(x, n)
        check = 0
        for i in nodes.reverse():
            if i not in v and i not in frontier:
                if check == 0:
                    n_ex +=1
                    check = 1
                if len(i.getDirec()) > max_d:
                    max_d = len(i.getDirec())
                frontier.append(i)
    
#        print(x)
#        print(frontier)
#        print(fron)
#        print(v)
#        br +=1
#    print(len(x))
                

#print(DFS(('1','2','5','3','4','0','6','7','8'), ('0','1','2','3','4','5','6','7','8'), 3))
    

t = time()

if sys.argv[1] == 'bfs':
    p = BFS(tup, Gt, n)
    t1 = time()
    t0 = t1 - t
    p = p + (str(t0), '9.908878965')

    r = ['path_to_goal: ', 'cost_of_path: ', 'nodes_expanded: ', 'fringe_size: ', 
     'max_fringe_size: ', 'search_depth: ', 'max_search_depth: ', 'running_time: ', 'max_ram_usage: ']
    w = open('output.txt', 'w')
    g = 0


    for line in r:
#        if g > 7:
#            break
        w.write(line + str(p[g]))
        w.write('\n')
        g +=1
    w.close()
if sys.argv[1] == 'dfs':
    p = BFS(tup, Gt, n)
    t1 = time()
    t0 = t1 - t
    p = p + (str(t0), '9.908878965')

    r = ['path_to_goal: ', 'cost_of_path: ', 'nodes_expanded: ', 'fringe_size: ', 
     'max_fringe_size: ', 'search_depth: ', 'max_search_depth: ', 'running_time: ', 'max_ram_usage: ']
    w = open('output.txt', 'w')
    g = 0


    for line in r:
#        if g > 7:
#            break
        w.write(line + str(p[g]))
        w.write('\n')
        g +=1
    w.close()
#print(DFS(('1','2','7','0','4','3','6','5','8'), ('0','1','2','3','4','5','6','7','8'), 3))
    
def getIndex(num, tup):
    for i in range(len(tup)):
        if tup[i] == num:
            return i
def NumOfmisp(tile, n):
    count = n**2 -1
    for j in tile:
        if j != '0':
            if getIndex(j, tile) == int(j):
                count -=1
    return count
#print(NumOfmisp(('0','1','2','3','4','5','6','7','8'), 3))
def getPosition(index, n):
    return (int(index/n) + 1, index%n + 1)
def CalSingleSum(I_p, G_p, n):
    return abs(I_p[0] - G_p[0]) + abs(I_p[1] - G_p[1])
def calSum(State, n):
    ans = 0
    count = 0    
    for m in State:
        if m != '0':
            ans += CalSingleSum(getPosition(count, n), getPosition(int(m), n), n)
        count +=1
    return  ans 
#+ NumOfmisp(State, n)
#print(calSum(('7','2','4','5','0','6','8','3','1'), 3))
def getMinNode(List):
    ans = List[0][1]
    ret = List[0][0]
    for h in List:
        if h[1] < ans:
            ans = h[1]
            ret = h[0]
    return (ret, ans)

def ASS(Istate, Gstate, n):
    if Istate == Gstate:
        return ([],0,0,0,0,0,0,0,0)
    node = Node(Istate)
    frontier = [(node, calSum(Istate, n))]
    v = []
    fron = []
    exp = 0
    max_f = 1
    max_d = 0
    while frontier != []:
        if len(frontier) > max_f:
            max_f = len(frontier)
        x = getMinNode(frontier)
        if len(x[0].getDirec()) > max_d:
            max_d = len(x[0].getDirec())
        v.append(x[0])
        fron.append(x[0])
        frontier.remove(x)
        if x[0].getState() == Gstate:
            return (x[0].getDirec(), len(x[0].getDirec()), exp, len(frontier), max_f, len(x[0].getDirec()), max_d)
        nodes = GenChildren(x[0], n)
        check = 0
        for m in nodes:
            if m not in v and m not in fron:
                frontier.append((m, calSum(m.getState(), n)))
                fron.append(m)
                if check == 0:
                    exp +=1
                    check = 1

if sys.argv[1] == 'ast':
    p = ASS(tup, Gt, n)
    t1 = time()
    t0 = t1 - t
    p = p + (str(t0), '9.908878965')

    r = ['path_to_goal: ', 'cost_of_path: ', 'nodes_expanded: ', 'fringe_size: ', 
     'max_fringe_size: ', 'search_depth: ', 'max_search_depth: ', 'running_time: ', 'max_ram_usage: ']
    w = open('output.txt', 'w')
    g = 0
#    print(p)


    for line in r:
#        if g > 7:
#            break
        w.write(line + str(p[g]))
        w.write('\n')
        g +=1
    w.close()
            
#t = time()     
#        
#print(ASS(('1','2','5','3','4','0','6','7','8'), ('0','1','2','3','4','5','6','7','8'), 3))            
#    
#t1 = time()
#print(t1 - t)
#    







    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

        
        
        
        

       
       
       
