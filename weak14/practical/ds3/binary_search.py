class Node:
    def __init__(self,data):
        self.data = data
        self.left = None 
        self.right = None 
class BST:
    def __init__(self,value):
        self.root =Node(value)
    def insert(self,value):
        if self.root is None :
            self.root = Node(20)
        else :
            self._insert_recurisvely(self.root,value)
    def _insert_recurisvely(self,node,value):
        if value < node.data :
            if node.left is None :
                node.left = Node(value)
            else :
                self._insert_recurisvely(node.left,value)
        else :
            if node.right is None :
                node.right = Node(value)
            else :
                self._insert_recurisvely(node.right,value)
    def search(self,value):
        return self._search_recursive(self.root,value)
    def _search_recursive(self,node,value):
        if node is None :
            return False 
        if node.data == value :
            return True 
        if value < node.data :
            return self._search_recursive(node.right,value)
        return self._search_recursive(node.right,value)
    def in_order(self,node):
        if node:
            self.in_order(node.left)
            print(node.data,end=' ')
            self.in_order(node.right)
            
s = BST(10)
s.insert(100)
s.insert(2)
s.insert(40)
s.in_order(s.root)
