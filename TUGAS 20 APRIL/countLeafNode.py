# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 11:00:50 2020

@author: Salsabila Laily Rahma
"""

###MENGHITUNG BANYAK LEAF

class Node: 
     
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None
  

def getLeafCount(node): 
    if node is None: 
        return 0 
    if(node.left is None and node.right is None): 
        return 1 
    else: 
        return getLeafCount(node.left) + getLeafCount(node.right) 
  
  

root = Node(15) 
root.left = Node(6) 
root.right = Node(18) 
root.left.left = Node(3) 
root.left.right = Node(7)
root.left.left.left = Node(2)
root.left.left.right = Node (4)
root.left.right.right = Node (13)
root.left.right.right.left = Node (9)
root.left.right.right.right = Node (14)
root.right.left = Node (17)
root.right.right = Node (20)
  
print ("Leaf count of the tree is %d" %(getLeafCount(root))) 
