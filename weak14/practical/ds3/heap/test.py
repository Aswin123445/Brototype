class Node :
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 
class BST :
    def __init__(self):
        self.root = None 
    
    def insert(self,value):
        if self.root is None :
            self.root = Node(value)
        else :
            self.insert_recursively(self.root,value)
    def insert_recursively(self,node,value):
        if value < node.data :
            if node.left is None :
                node.left = Node(value)
            else :
                self.insert_recursively(node.left,value)
        else :
            if node.right is None :
                node.right = Node(value)
            else :
                self.insert_recursively(node.right,value)
                
    def in_order(self,node):
        if node :
            self.in_order(node.left)
            print(node.data,end=' ')
            self.in_order(node.right)
            
    def search(self,value):
        return self.search_recusievly(self.root,value)
    
    def search_recusievly(self,node,value):
        if node is None :
            return False 
        if node.data == value :
            return True  
        if value < node.data :
            return self.search_recusievly(node.left,value)
        return self.search_recusievly(node.right,value)
    
    def nth_largest_element(self,node,k):
        self.count = 0 
        self.value = None 
        self.reverse_in_order(node,k)
        return self.value 
    
    def reverse_in_order(self,node,k):
        if node is None or self.count >= k :
            return 
        
        self.reverse_in_order(node.right,k)
        
        self.count += 1 
        if self.count == k :
            self.value = node.data 
            return 
        
        self.reverse_in_order(node.left,k)
        
    def closest_value(self,value):
        return self.closest_recursion(self.root,value,float('inf'))
    
    def closest_recursion(self,node,target,closest):
        if node is None :
            return closest
        if abs(target-node.data) < abs(target - closest):
            closest = node.data 
        if target < node.data :
            return self.closest_recursion(node.left,target,closest)
        elif target > node.data :
            return self.closest_recursion(node.right,target,closest)
        else :
            return closest
        
def is_identical(root1,root2):
    if root1 is None and root2 is None :
        return True 
    if root1 is None or root2 is None :
        return False 
    return is_identical(root1.left,root2.left) and root1.data == root2.data and is_identical(root1.right,root2.right)

def is_bst(node,lowest = float('-inf'),largest = float('inf')):
    if node is None :
        return True 
    if not (lowest < node.data < largest):
        return False 
    return is_bst(node.left,lowest,node.data) and is_bst (node.right,node.data,largest)
    
b = BST()
b.insert(50)
b.insert(10)
b.insert(54)
b.in_order(b.root)
print()
print(b.search(11))

print(b.nth_largest_element(b.root,2))

node = Node(10)
node1 = Node(20)
node3 = Node(40)
node.left = node1
node.right = node3
print(b.nth_largest_element(node,1))

print(b.closest_value(1))