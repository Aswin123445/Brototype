class Graph:
    def __init__(self):
        self.graph = {}
    def insert(self,u,v,directed = True):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        if not directed :
            self.graph[v].append(u)
        self.graph[u].append(v)
        
    def display(self):
        for node in self.graph:
            print(f'{node} -> {self.graph[node]}')
            

def cycle_undirected(graph):
    visited = set()
    for start in graph :
        if start not in visited :
            stack = [(start,None)]
            while stack :
                current,parent = stack.pop()
                if current in visited :
                    continue 
                visited.add(current)
                
                for neibhour in graph[current]:
                    if neibhour not in visited :
                        stack.append((neibhour,current))
                    elif neibhour != parent :
                        return True 
    return False 

import heapq
def shortest_path_weighted(graph,start,end):
    visited = set()
    heap = [(0,start,[start])]
    while heap :
        cost,current,path = heapq.heappop(heap)
        
        if current in visited :
            continue
        
        visited.add(current)
        
        if current == end :
            return path,cost
        
        for neibhour,weight in graph.get(current,[]):
            if neibhour not in visited:
                heapq.heappush(heap,(cost + weight ,neibhour , path + [neibhour]))
    return None  


def shortest_path_bfs(grpah,start,end):
    visited = set()
    queue = [(start,[start])]
    visited.add(start)
    while queue :
        current,path = queue.pop(0)
        if current == end :
            return path 
        for neibhouri in grpah[current]:
            if neibhouri not in visited:
                visited.add(neibhouri)
                queue.append((neibhouri,path+[neibhouri]))
                
                
def clonegraph(graph):
    if not graph:
        return {}
    clone = {}
    
    #bfs 
    first_node = next(iter(graph))
    clone[first_node] = graph[first_node]
    queue = [first_node]
    while queue :
        current = queue.pop(0)
        for neibhour in graph[current]:
            if neibhour not in clone:
                clone[neibhour] = graph[neibhour]
                queue.append(neibhour)
    return clone

#diksharj algoritm 
def short(graph,start,end):
    visited = set()
    heap = [(0,start,[start])]
    while heap :
        cost,current,path = heapq.heappop(heap)
        if current in visited:
            continue
        visited.add(current)
        
        if current == end :
            return path,cost 

        for neibhour,weight in graph.get(current,[]):
            if neibhour not in visited :
                heapq.heappush(heap,(cost+weight,neibhour,path + [neibhour]))
                

class Node:
    def __init__(self,val):
        self.val = val 
        self.left = None 
        self.right = None 
        
class BST:
    def __init__(self):
        self.root = None 
        
    def insert(self,val):
        new_node = Node(val)
        if not self.root :
            self.root = new_node 
            return 
        stack = [self.root]
        while stack :
            current = stack.pop()
            if val < current.val:
                if not current.left :
                    current.left = new_node
                    return 
                stack.append(current.left)
            else :
                if not current.right :
                    current.right = new_node
                    return 
                stack.append(current.right)
                
    def in_order(self):
        current = self.root 
        stack = []
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            print(current.val,end = " ")
            current = current.right
                
                
        
    #preorder       
    def search(self,val):
        stack = [self.root]
        while stack :
            current = stack.pop()
            if val == current.val:
                return True 
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
                
    def min_node(self,node):
        current = node
        while current:
            current = current.left 
        return current 
        
    def delete(self,val):
        def delete_node(node,val):
            if not node :
                return node 
            if val < node.val :
                node.left = delete_node(node.left,val)
            elif val > node.val :
                node.right = delete_node(node.right,val)
            else :
                if not node.left:
                    return node.right 
                elif not node.right:
                    return node.left
                
                temp_node = self.min_node(node.right)
                node.val = temp_node.val
                node.right = delete_node(node.right,temp_node.val)
            return node
                
        self.root = delete_node(self.root,val)
        
        
b = BST()
b.insert(10)
b.insert(4)
b.insert(20)
b.insert(40)
b.insert(60)

b.in_order()
print()
b.delete(20)
b.in_order()
        