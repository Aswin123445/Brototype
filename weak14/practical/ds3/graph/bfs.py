# class Node :
#     def __init__(self,data):
#         self.data = data 
#         self.left = None 
#         self.right = None 
        
        
# class BST:
#     def __init__(self):
#         self.root = None 
        
#     def insert(self,data):
#         if self.root is None :
#             self.root  = Node(data)
#         else :
#             self.insert_recurively(self.root,data)
            
#     def insert_recurively(self,node,data):
#         if data < node.data :
#             if node.left is None :
#                 node.left = Node(data)
#             else :
#                 self.insert_recurively(node.left,data)
#         else :
#             if node.right is None :
#                 node.right = Node(data)
#             else :
#                 self.insert_recurively(node.right,data)
                
#     def search(self,value):
#         return self.search_recusively(self.root,value)
    
#     def search_recusively(self,node,value):
#         if node is None :
#             return False 
#         if node.data == value :
#             return True 
#         if value < node.data :
#             return self.search_recusively(node.left,value)
#         return self.search_recusively(node.right,value)
    
#     def in_order(self,node):
#         if node:
#             self.in_order(node.left)
#             print(node.data,end = " ")
#             self.in_order(node.right)
            

#     #go to the node 
#     #break the connection
#     #destructure tree
#     def delete(self,value):
#         self.delete_recursively(self.root,value)
        
#     def delete_recursively(self,node,value):
#         if node.left.data  == value :
#             node.left = node.left.left
#             return 
#         if node.right.data == value :
#             node.right = node.right.right
#             return 
#         if value < node.data:
#             self.delete_recursively(node.left,value)
#         else :
#             self.delete_recursively(node.right,value)
            
        
            
            
            
            
# bst = BST()
# bst.insert(10)
# bst.insert(30)
# print(bst.search(10))
# bst.in_order(bst.root)
# bst.delete(10)

class Heap:
    def __init__(self):
        self.heap = []
        
    #inserting data to the heap
    def push(self,data):
        self.heap.append(data)
        self.heapify_up(len(self.heap)-1)
    def heapify_up(self,index):
        parent = (index-1)//2 
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index],self.heap[parent]  = self.heap[parent] ,self.heap[index] 
            index = parent 
            parent = (index - 1)/2
            
    def pop(self):
        if not self.heap:
            return 
        if len(self.heap) == 1 :
            return self.heap.pop()
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return min_value
    
    def heapify_down(self,index):
        n= len(self.heap)
        small = index
        left = index*2 + 1 
        right = index*2 + 2 
        if left < n  and self.heap[left] < self.heap[small]:
            small = left
        if right < n  and self.heap[right] < self.heap[small]:
            small = right 
        if small != index :
            self.heap[small] ,self.heap[index]  = self.heap[index] ,self.heap[small] 
            self.heapify_down(small)
            
    def display(self):
        print(self.heap)
        
h = Heap()
h.push(10)
h.push(1)
h.push(15)
h.pop()
h.display()
        
        
        


