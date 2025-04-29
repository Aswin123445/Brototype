
# class Graph:
#     def __init__(self):
#         self.graph = {}
#     def insert(self,u,v,directed = False):
#         if u not in self.graph:
#             self.graph[u] = []
#         if v not in self.graph:
#             self.graph[v] = []
#         if not directed :
#             self.graph[v].append(u)
#         self.graph[u].append(v)
    
#     def display(self):
#         for node in self.graph:
#             print(f'{node}->{self.graph[node]}')
            

# def dfs(graph,vertex):
#     visited = set()
#     stack = [vertex]
#     while stack:
#         current = stack.pop()
#         if current not in visited :
#             print(current)
#             visited.add(current)
#             stack.extend(reversed([node for node in graph[current] if node not in visited]))
            
# def bfs(graph,vertex):
#     visited = set()
#     queue = [vertex]
#     visited.add(vertex)
#     while queue :
#         current = queue.pop(0)
#         print(current)
#         for neibhour in graph[current]:
#             if neibhour not in visited :
#                 visited.add(neibhour)
#                 queue.append(neibhour)
                
# def has_path_dfs(graph,start,end):
#     visited = set()
#     stack = [(start,[start])]
#     while stack:
#         current,path = stack.pop()
#         if current == end :
#             return path 
#         if current not in visited :
#             visited.add(current)
#             stack.extend(reversed([(node,path + [node]) for node in graph[current]]))
            
# def has_path_bfs(graph,start,end):
#     visited = set()
#     queue = [(start,[start])]
#     visited.add(start)
#     while queue :
#         current,path = queue.pop(0) 
#         if current == end :
#             return path 
#         for neibhour in graph[current]:
#             if neibhour not in visited:
#                 visited.add(neibhour)
#                 queue.append((neibhour,path + [neibhour]))
                
# def cycle_undirected(graph):
#     visited = set()
#     for node in graph:
#         if node not in visited :
#             stack = [(node,None)]
#             while stack :
#                 current,parent = stack.pop()
#                 if current in visited :
#                     continue
#                 visited.add(current)
#                 for neigbhour in graph[current] :
#                     if neigbhour not in visited :
#                         stack.append((neigbhour,current))
#                     elif neigbhour != parent :
#                         return True 
#     return False 


# def short_path_unweighted(graph,start,end):
#     visited = set()
#     queue = [(start,[start])]
#     visited.add(start)
#     while queue :
#         current,path = queue.pop(0)
#         if current == end :
#             return path 
#         for neibhour in graph[current]:
#             if neibhour not in visited :
#                 visited.add(neibhour)
#                 queue.append((neibhour,path + [neibhour]))
                
# import heapq
# def short_path_weighted(graph,start,end):
#     visited = set()
#     heap = [(0,start,[start])]
#     while heap :
#         cost,current,path = heapq.heappop(heap)
        
#         if current in visited :
#             continue 
        
#         visited.add(current)
        
#         if current == end :
#             return path,cost 
        
#         for neibhour,weight in graph.get(current,[]):
#             if neibhour not in visited:
#                 heapq.heappush(heap,(cost + weight,neibhour,path + [neibhour]))
#     return None 
        
            
# g = Graph()
# g.insert(1,2)
# g.insert(2,3)
# g.insert(3,4)
# g.insert(4,1)
# print(has_path_bfs(g.graph,1,4))
# print(cycle_undirected(g.graph))
# print(short_path_unweighted(g.graph,1,3))

class Graph :
    def __init__(self):
        self.graph = {}
        
    def insert(self,u,v,directed = False):
        if u not in self.graph :
            self.graph[u] = []
        if v not in self.graph :
            self.graph[v] = [] 
        
        if not directed :
            self.graph[v].append(u)
        self.graph[u].append(v)
        
    def weighted_insert(self,u,v,weight = 1 ,directed = False):
        if u not in self.graph :
            self.graph[u] = []
        if v not in self.graph :
            self.graph[v] = [] 
        
        if not directed :
            self.graph[v].append((u,weight))
        self.graph[u].append((v,weight))
        
    def display(self):
        for node in self.graph :
            print(f'{node} -> {self.graph[node]}')
            
    
#dfs algoritm 
def dfs(graph,vertex):
    visited = set()
    stack = [vertex]
    while stack :
        current = stack.pop()
        if current not in visited :
            print(current,end = ' ')
            visited.add(current)
            stack.extend(reversed([node for node in graph[current] if node not in visited]))
            
            
def bfs(graph,vertex):
    visited = set()
    queue = [vertex]
    visited.add(vertex)
    while queue :
        current = queue.pop(0)
        print(current,end=' ')
        for neibhour in graph[current]:
            if neibhour not in visited :
                visited.add(neibhour)
                queue.append(neibhour)
                


#shortest path problem unweighted bfs
def short_path(graph,start,end):
    visited = set()
    queue = [(start,[start])]
    visited.add(start)
    while start :
        current,path = queue.pop(0)
        
        if current == end :
            return path 
        
        for neibhour in graph[current]:
            if neibhour not in visited :
                visited.add(neibhour)
                queue.append((neibhour,path + [neibhour]))
                
import heapq
def shortest_path_weighted(graph,start,end):
    visited = set()
    heap  = [(0,start,[start])]
    while heap:
        cost,current,path = heapq.heappop(heap)
        if current in visited:
            continue
        visited.add(current)
        
        if current == end :
            return path,cost 
        
        for neibhours,weight in graph.get(current,[]):
            if neibhours not in visited:
                heapq.heappush(heap,(cost+weight,neibhours,path + [neibhours]))  
    return None

def cycle_detect(graph):
    visited = set ()
    for start in graph :
        if start not in visited:
            stack = [(start,None)]
            while stack :
                current,parent = stack.pop()
                if current  in visited:
                    continue
                
                visited.add(current)
                for neibhour in graph[current]:
                    if neibhour not in visited :
                        stack.append((neibhour,current))
                    elif neibhour != parent :
                        return True 
    return False 
               

g = Graph()
g.insert(1,2)
g.insert(1,3)
g.insert(3,4)
g.insert(3,1)
g.insert(2,5)
g.insert(2,1)
g.insert(2,6)
g.insert(6,1)
g.display()
dfs(g.graph,6)
print()
bfs(g.graph,3)
print()
print(cycle_detect(g.graph))