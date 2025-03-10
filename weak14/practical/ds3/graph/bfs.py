from collections import deque 
def bfs(graph,vertex):
    visited = set()
    queue = deque([vertex])
    visited.add(vertex)
    while queue :
        nodes = queue.popleft()
        print(nodes,end=" ")
        for node in graph[nodes] :
            if node not in visited :
                queue.append(node)
                visited.add(node)
                
def bfs_unweight_short_path(graph,vertex,target):
    visited = set()
    queue = [(vertex,0)]
    visited.add(vertex)
    while queue :
        node,dist = queue.pop(0)
        if node == target :
            return dist
        
        for neibhor in graph[node]:
            if neibhor not in visited :
                queue.append((neibhor,dist+1))
                visited.add(neibhor)
                
graph= {
    1 : [2,3],
    2 : [3,4,1],
    3 : [1,2],
    4 : [2]
}
print(bfs_unweight_short_path(graph,3,4))
bfs(graph,3)

                