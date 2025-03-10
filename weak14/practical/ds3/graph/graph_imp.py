class Graph:
    def __init__(self):
        self.graph = {}
        
    def add_edges(self,u,v,directed = False):
        if u not in self.graph :
            self.graph[u] = [] 
        if v not in self.graph :
            self.graph[v] = []
        if not directed :
            self.graph[v].append(u)
        self.graph[u].append(v)
        
    def display(self):
        for node in self.graph :
            print(f'{node} -> {self.graph[node]}')
            
def bfs(graph,vertex):
    visisted = set()
    queue = [vertex]
    visisted.add(vertex)
    while queue :
        node = queue.pop(0)
        print(node,end=" ")
        for neighbour in graph[node]:
            if neighbour  not in visisted :
                queue.append(neighbour)
                visisted.add(neighbour)
                
def dfs(graph,vertex):
    visited = set()
    stack = [vertex]
    while stack :
        node = stack.pop()
        if node not in visited :
            print(node,end=' ')
            visited.add(node)
            stack.extend(reversed(graph[node]))
                
g = Graph()
g.add_edges(0,1)
g.add_edges(1,2)
g.add_edges(0,2)

g.display()
bfs(g.graph,0)