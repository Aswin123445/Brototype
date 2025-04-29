class Node :
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 
class Tree :
    def __init__(self,data):
        self.root = Node(data)
        
    def insert(self,value):
        if self.root is None :
            self.root = Node(value)
        else :
            self.isnert_recursively(self.root,value)
    def isnert_recursively(self,node,value):
        if value < node.data :
            if node.left is None :
                node.left = Node(value)
            else :
                self.isnert_recursively(node.left,value)
        else :
            if node.right is None:
                node.right = Node(value)
            else :
                self.isnert_recursively(node.right,value)
                
    def search(self,value):
        return self.search_recursively(self.root,value)
    def search_recursively(self,node,value):
        if node is None :
            return False 
        if node.data == value :
            return True 
        if value < node.data :
            return self.search_recursively(node.left,value)
        return self.search_recursively(node.right,value)
    
    
    def in_order(self,node):
        if node :
            self.in_order(node.left)
            print(node.data,end= ' ')
            self.in_order(node.right)
            
    def delete(self,value):
        self.root =  self._delete_recursively(self.root,value)
    
    def _delete_recursively(self,node,value):
        if node is None :
            return node 
        #finding the node to delete 
        if value < node.data :
            node.left = self._delete_recursively(node.left,value)
        elif value > node.data :
            node.right = self._delete_recursively(node.right,value)
        else :
            #node has no child leaf 
            if node.left is None and node.right is None :
                return None 
            
            if node.left is None :
                return node.right 
            elif node.right is None :
                return node.left
            
            #both has child 
            min_node = self._findmin_node(node.right)
            node.data = min_node.data 
            node.right = self._delete_recursively(node.right,min_node.data)
        return node
            
    def _findmin_node(self,node):
        while node.left :
            node = node.left
        return node
    
            
        