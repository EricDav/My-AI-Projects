# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 10:03:43 2017

@author: DAVID
"""
from random import randint
from random import choice
from BaseAI_3 import BaseAI

class Child(object):
    def __init__(self, grid):
        self.grid = grid
        self.direc = []
    def addDirec(self, direc):
        self.direc.append(direc)
    def getDirec(self):
        return self.direc
    def getGrid(self):
        return self.grid
    def addDP(self, l):
        self.direc + l

    
        




def GenSingleChildrenForMax(grid, Dir):
    if Dir == 0:
        v0, v1, v2, v3 = [], [], [], []
        for i in range(1, 4):
            for j in range(4):
                if grid.map[i][j] != 0:
                   # b = True
                    m = i
                    n = j
                    while grid.crossBound((m-1, n)) == False:
                        a = grid.getCellValue((m-1,j)) == grid.getCellValue((m,j))
                        #v.append(j)
                       # print(v)
                        if j == 0:
                            if a == True and (m in v0 or m-1 in v0):
                                a = False
                        elif j == 1:
                            if a == True and (m in v1 or m-1 in v1):
                                a = False
                        elif j == 2:
                            if a == True and (m in v2 or m-1 in v2):
                                a = False
                        else:
                            if a == True and (m in v3 or m-1 in v3):
                                a = False
                        if grid.canInsert((m-1, n)):
                            grid.insertTile((m-1,n), grid.map[m][n])
                            grid.insertTile((m,n), 0)
                            #print(grid.map)
                        elif a:
                            grid.insertTile((m-1,j), grid.map[m][n]*2)
                            grid.insertTile((m,n), 0)
                            if j == 0:
                                v0.append(m-1)
                            elif j == 1:
                                v1.append(m-1)
                            elif j == 2:
                                v2.append(m-1)
                            else:
                                v3.append(m-1)
                        #print(v3)
                        m -=1
        return Child(grid.clone())
    elif Dir == 1:
        v0, v1, v2, v3 = [], [], [], []
        for i in [2,1,0]:
            for j in range(4):
                if grid.map[i][j] != 0:
#                    if j not in v:
#                       b = True
                    m , n = i, j
                    while grid.crossBound((m+1, n)) == False:
                        a = grid.getCellValue((m+1,j)) == grid.getCellValue((m,j))
                        if j == 0:
                            if a == True and (m in v0 or m+1 in v0):
                                a = False
                        elif j == 1:
                            if a == True and (m in v1 or m+1 in v1):
                                a = False
                        elif j == 2:
                            if a == True and (m in v2 or m+1 in v2):
                                a = False
                        else:
                            if a == True and (m in v3 or m+1 in v3):
                                a = False
                        if grid.canInsert((m+1, n)):
                               grid.insertTile((m+1,n), grid.map[m][n])
                               grid.insertTile((m,n), 0)
                               #print(grid.map)
                        elif a:
                               grid.insertTile((m+1,j), grid.map[m][n]*2)
                               grid.insertTile((m,n), 0)
                               #b = False
                               if j == 0:
                                   v0.append(m+1)
                               elif j == 1:
                                   v1.append(m+1)
                               elif j == 2:
                                   v2.append(m+1)
                               else:
                                   v3.append(m+1)
                        m +=1
        return Child(grid.clone())
    elif Dir == 2:
       # v = []
        for i in range(4):
            v = []
            for j in range(1, 4):
                #v = []
                if grid.map[i][j] != 0:
                       m , n = i, j
                       while grid.crossBound((m,n-1)) == False:
                           a = grid.getCellValue((m,n-1)) == grid.getCellValue((m,n))
                          # print(grid.getCellValue((m,n)))
                           if a and (n-1 in v or n in v):
                               a = False
                           if grid.canInsert((m, n-1)):
                               grid.insertTile((m,n-1), grid.map[m][n])
                               grid.insertTile((m,n), 0)
                               #print(grid.map)
                           elif a:
                               grid.insertTile((m,n-1), grid.map[m][n]*2)
                               v.append(n-1)
                               grid.insertTile((m,n), 0)
            
                
                          # print(v)
                           n -=1
        return Child(grid.clone())
    elif Dir == 3:
       # v = []
        for i in range(4):
            v = []
            for j in [2,1,0]:
                if grid.map[i][j] != 0:
                       m , n = i, j
                       while grid.crossBound((m,n+1)) == False:
                           a = grid.getCellValue((m,n+1)) == grid.getCellValue((m,n))
                           if a and (n+1 in v or n in v):
                               a = False
                           if grid.canInsert((m, n+1)):
                               grid.insertTile((m,n+1), grid.map[m][n])
                               grid.insertTile((m,n), 0)
                         
                           elif a:
                               grid.insertTile((m,n+1), grid.map[m][n]*2)
                               grid.insertTile((m,n), 0)
                               v.append(n+1)
                           n +=1
        return Child(grid.clone())
def GenChildrenForMin(child):
    l, m, ans = [2,2,2,2,2,2,2,2,2,4], child.getGrid().getAvailableCells(), []
          
    for i in m:
       x = Child(child.getGrid().clone())
       x.getGrid().insertTile(i, choice(l))
       ans.append(x)
    return ans

def GenChildrenForMax(child):
    ans = []
    for i in child.getGrid().getAvailableMoves():
        x = Child(child.getGrid().clone())
        a = GenSingleChildrenForMax(x.getGrid(), i)
        for m in child.getDirec():
            a.addDirec(m)
        a.addDirec(i)
        ans.append(a)
    return ans

def GetMerge(l):
    ans = 0
    if l[0] == l[3] and l[2] + l[1] == 0:
        ans = l[0]
    elif l[0] == l[1]:
        ans = l[0]
    elif l[2] == l[3]:
        ans = l[2]
    elif l[1] == l[2]:
        ans = l[1]
    if l[0] == l[1] and l[2] == l[3]:
        ans = l[0] + l[2]
    return ans
def getMergeForColomn(grid):
    l = [grid.map[0][0],grid.map[1][0],grid.map[2][0],grid.map[3][0]]
    l1 = [grid.map[0][1],grid.map[1][1],grid.map[2][1],grid.map[3][1]] 
    l2 = [grid.map[0][2],grid.map[1][2],grid.map[2][2],grid.map[3][2]]           
    l3 = [grid.map[0][3],grid.map[1][3],grid.map[2][3],grid.map[3][3]]   
    return sum((GetMerge(l), GetMerge(l1), GetMerge(l2), GetMerge(l3)))  
def getMergeForRoll(grid):
    ans = 0
    for i in grid.map:
        ans +=GetMerge(i)
    return ans

def NumOfSpace(grid):
    return 25*len(grid.getAvailableCells())
#def AverageTiles(grid):
#    ans = 0
#    for i in grid.map:
#        ans +=max(i)
#    return ans/20
def m(i):
    ans = 0
    if i[0] > i[1]  and i[1] > i[2] and i[2] > i[3]:
            ans = ans + sum(i)
#    elif i[0] < i[1]  and i[1] < i[2] and i[2] < i[3]:
#            ans = ans + sum(i)
    return ans
    
def Mono(grid):
    ans = 0
    for i in grid.map:
        if i[0] > i[1]  and i[1] > i[2] and i[2] > i[3]:
            ans = ans + sum(i)
#        elif i[0] < i[1]  and i[1] < i[2] and i[2] < i[3]:
#            ans = ans + sum(i)
    return ans
def Mono1(grid):
    l = [grid.map[0][0],grid.map[1][0],grid.map[2][0],grid.map[3][0]]
    l1 = [grid.map[0][1],grid.map[1][1],grid.map[2][1],grid.map[3][1]] 
    l2 = [grid.map[0][2],grid.map[1][2],grid.map[2][2],grid.map[3][2]]           
    l3 = [grid.map[0][3],grid.map[1][3],grid.map[2][3],grid.map[3][3]]
    return m(l) + m(l1) + m(l2) + m(l3)
def Monotocity(grid):
    return (Mono1(grid) + Mono(grid))/10
def Difference(grid):
    ans = 0
    for i in range(4):
        for j in range(4):
            if j == 0 and i == 0:
                ans = grid.map[i][j] + grid.map[i][j+1]
                ans = grid.map[i][j] + grid.map[i+1][j]
            elif i == 0 and j == 3:
                ans = grid.map[i][j] + grid.map[i+1][j]
                ans = grid.map[i][j] + grid.map[i][j-1]
            elif i == 3 and j == 0:
                ans = grid.map[i][j] + grid.map[i-1][j+1]
                ans = grid.map[i][j] + grid.map[i][j+1]
            elif i == 3 and j == 3:
                ans = grid.map[i][j] + grid.map[i-1][j]
                ans = grid.map[i][j] + grid.map[i][j-1]
            elif (i == 1 or i == 2) and j == 0:
                ans = grid.map[i][j] + grid.map[i+1][j]
                ans = grid.map[i][j] + grid.map[i-1][j]
                ans = grid.map[i][j] + grid.map[i][j+1]
            elif (i == 1 or i == 2) and j == 3:
                ans = grid.map[i][j] + grid.map[i+1][j]
                ans = grid.map[i][j] + grid.map[i-1][j]
                ans = grid.map[i][j] + grid.map[i][j-1]
            elif (j == 1 or j == 2) and i == 0:
                ans = grid.map[i][j] + grid.map[i][j-1]
                ans = grid.map[i][j] + grid.map[i][j+1]
                ans = grid.map[i][j] + grid.map[i+1][j]
            elif (j == 1 or j == 2) and i == 3:
                ans = grid.map[i][j] + grid.map[i][j-1]
                ans = grid.map[i][j] + grid.map[i][j+1]
                ans = grid.map[i][j] + grid.map[i-1][j]
            else:
                ans = grid.map[i][j] - grid.map[i][j-1]
                ans = grid.map[i][j] - grid.map[i][j+1]
                ans = grid.map[i][j] - grid.map[i+1][j]
                ans = grid.map[i][j] - grid.map[i-1][j]
    return ans/50
            
    
def PosibleMerge(grid):
    return (getMergeForRoll(grid) + getMergeForColomn(grid))
def Corner(grid):
    return (grid.map[0][0] + grid.map[0][3] + grid.map[3][0] + grid.map[3][3]  + grid.map[1][0] + grid.map[1][3] + grid.map[2][0] + grid.map[2][3])

#def Max(grid):
#    for i in grid.map:
#        


def Eval(child):
    return NumOfSpace(child.getGrid())  + PosibleMerge(child.getGrid()) + Corner(child.getGrid())  + Difference(child.getGrid()) + Monotocity(child.getGrid())
def GetDirectionFromGrid(gridP, gridC):
    for i in gridP.getAvailableMoves():
        x = gridP.clone()
        #print(GenSingleChildrenForMax(gridP, i).map, i)
        a = GenSingleChildrenForMax(x, i)
        if a.getGrid().map == gridC.map:
            return i

#def isTerminalState()
def Minimise(child, a,b):
    if len(child.getDirec()) == 1:
        return (None, Eval(child))
    (minChild, minUtility) = (None, 100000000)
    for chil in GenChildrenForMin(child):
        (_, utility) = Maximum(chil,a,b)
        if utility < minUtility:
             (minChild, minUtility) = (chil, utility)
        if minUtility <= a:
            break
        if minUtility < b:
            b = minUtility
    return (minChild, minUtility)   

def Maximum(child,a,b):
    if len(child.getDirec()) == 4:
        return (None, Eval(child))
    (maxChild, maxUtility) = (None, -100000000)
    for chil in GenChildrenForMax(child):
        (_, utility) = Minimise(chil,a,b)
        if utility > maxUtility:
            (maxChild, maxUtility) = (chil, utility)
        if maxUtility >= b:
            break
        if maxUtility > a:
            a = maxUtility
    return (maxChild, maxUtility)
    


def Decision(child):
    ans  = Maximum(child, -1000000000, 1000000000)
    return GetDirectionFromGrid(child.getGrid(),ans[0].getGrid())

    





                  
                        
class PlayerAI(BaseAI):
    def getMove(self, grid):
        move = Child(grid)
        return Decision(move)