class Node:
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None 
class Tree:
    def __init__(self,value):
        self.root = Node(value)
    def insert(self,value):
        if self.root is None :
            self.root = Node(value)
        else :
            self._insert_recursivly(self.root,value)
    def _insert_recursivly(self,node,value):
        if value < node.data :
            if node.left is None :
                node.left = Node(value)
            else :
                self._insert_recursivly(node.left,value)
        else :
            if node.right is None :
                node.right = Node(value)
            else :
                self._insert_recursivly(node.right,value)
    def in_order(self,node):
        if node:
            self.in_order(node.left)
            print(node.data,end=' ')
            self.in_order(node.right)
    def search(self,value):
       return self._search_recursively(self.root,value)
    def _search_recursively(self,node,value):
        if node is None :
            return False 
        if node.data == value :
            return True
        if value < node.data :
            return self._search_recursively(node.left,value)
        return self._search_recursively(node.right,value)
t = Tree(10)
t.insert(20)
t.insert(40)
t.insert(200)
t.in_order(t.root)
print(t.search(1))
