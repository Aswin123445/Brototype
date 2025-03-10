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
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")
            
    def is_cyclic_util(self,vertex,visited,stack_rec):
        visited[vertex] = True
        stack_rec[vertex] = True 
        for neibhour in self.graph[vertex] :
            if not visited[neibhour] :
                if self.is_cyclic_util(neibhour,visited,stack_rec):
                    return True 
            elif stack_rec[neibhour] :
                return True
        stack_rec[vertex] = False 
        return False 
    
    def is_cyclic(self):
        visited = {node:False for node in self.graph}
        rec_stack = {node: False for node in self.graph}
        for node in self.graph :
            if not visited[node]:
                if self.is_cyclic_util(node,visited,rec_stack):
                    return True 
        return False 