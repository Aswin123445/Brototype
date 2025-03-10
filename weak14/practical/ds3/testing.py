class Node:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None  
class BST :
    def __init__(self):
        self.root = None 
    def insert(self,data):
        if self.root is None :
            self.root = Node(data)
        else :
            self._insert_recursively(self.root,data)
    def _insert_recursively(self,node,data):
        if data < node.data :
            if node.left is None :
                node.left = Node(data)
            else :
                self._insert_recursively(node.left,data)
        else :
            if node.right is None :
                node.right = Node(data)
            else :
                self._insert_recursively(node.right,data)
    def in_order(self,node):
        if node :
            self.in_order(node.left)
            print(node.data,end=" ")
            self.in_order(node.right)
    def search(self,value):
        return self._find_recursively(self.root,value)
    def _find_recursively(self,node,value):
        if node is None :
            return False 
        if node.data == value :
            return True 
        if value < node.data :
            return self._find_recursively(node.left,value)
        return self._find_recursively(node.right,value)
    def kth_largest(self,k):
        self.count = 0 
        self.kth_element = None 
        self._kth_recursively(self.root,k)
        return self.kth_element
    def _kth_recursively(self,node,k):
        if node is None  or self.count >= k:
            return 
        self._kth_recursively(node.right,k) 
        
        self.count += 1 
        if self.count == k :
            self.kth_element = node.data 
        
        self._kth_recursively(node.left,k)
    def find_the_closest_value(self,value):
        return self._closest_recursion(self.root,value,float('inf'))
    def _closest_recursion(self,node,target,closest):
        if node is None :
            return closest
        if abs(target - node.data) < abs(target - closest):
            closest = node.data
        if target < node.data :
            return self._closest_recursion(node.left,target,closest)
        elif target > node.data :
            return self._closest_recursion(node.right,target,closest)
        else :
            return closest
    def count_single_child(self, node):
        if node is None:
            return 0  # Base case
        count = 0
        # Check if the node has only one child
        if (node.left is None and node.right is not None) or (node.left is not None and node.right is None):
            count = 1

        # Recursive call for left and right children
        count += self.count_single_child(node.left)
        count += self.count_single_child(node.right)

        return count
        
#identical 
def two_trees_identical(root1,root2):
    if root1 is None and root2 is None :
        return True 
    if root1 is None or root2 is None :
        return False 
    return (two_trees_identical(root1.left,root2.left) and two_trees_identical(root1.right,root2.right))
    
    
    
b = BST()
b.insert(50)
b.insert(45)
b.insert(60)
b1 = BST()
b1.insert(50)
b1.insert(45)
b.in_order(b.root)
print()
print(b.search(46))
print(b.kth_largest(3))
print(b.find_the_closest_value(46))
print(two_trees_identical(b.root,b1.root))