class Node:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None  
class BST:
    def __init__(self,data):
        self.root = Node(data)
    def insert(self,value):
        if self.root is None :
            self.root = Node(value)
        else :
            self._insert_recurisvely(self.root,value)
    def _insert_recurisvely(self,node,value):
        if value < node.data :
            if node.left is None :
                node.left = Node(value)
            else :
                self._insert_recurisvely(self.left,value)
        else :
            if node.right is None :
                node.right = Node(value)
            else :
                self._insert_recurisvely(self.right,value)
    def in_order(self,node):
        if node:
            self.in_order(node.left)
            print(node.data,end=" ")
            self.in_order(node.right)
            
    def pre_order(self,node):
        if node:
            print(node.data,end=" ")
            self.in_order(node.left)
            self.in_order(node.right)
    def post_order(self,node):
        if node:
            self.in_order(node.left)
            self.in_order(node.right)
            print(node.data,end=" ")
    def search(self,value):
        return self._search_recursive(self.root,value)
    def _search_recursive(self,node,value):
        if node is None :
            return False 
        if node.data == value :
            return True 
        if value < node.data :
            return self._search_recursive(node.left,value)
        return self._search_recursive(node.right,value)
    
def is_identical(root1,root2):
    if root1 is None and root2 is None :
        return True 
    if root1 is None or root2 is None :
        return False 
    return (root1.data == root2.data and is_identical(root1.left,root2.left) and is_identical(root1.right,root2.right))

t = BST(10)
t.insert(20)
t.insert(4)
t.in_order(t.root)
print()
t1= BST(10)
t1.insert(20)
t1.in_order(t1.root)
print()
print(is_identical(t.root,t1.root))
print(t1.search(30))