class Graph:
    def __init__(self):
        self.graph = {}
        
    def insert_edge(self,u,v,directed = False):
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
    
    def is_cyclic_util(self,vertex,visited,parent):
        visited[vertex] = True 
        for neidhbor in self.graph[vertex] :
            if not visited[neidhbor] :
                if self.is_cyclic_util(neidhbor,visited,vertex):
                    return True 
            elif parent != neidhbor :
                return True 
        return False 
    
    def is_cyclic(self):
        visited = {node:False for node in self.graph}
        for node in self.graph :
            if not visited[node]:
                if self.is_cyclic_util(node,visited,-1):
                    return True 
        return False 
    
g = Graph()
g.insert_edge(0, 1)
g.insert_edge(1, 2)
g.insert_edge(2, 3)
g.insert_edge(3, 4)
g.insert_edge(4, 1)  # Cycle here

g.display()
print("Graph contains cycle" if g.is_cyclic() else "Graph does not contain cycle")