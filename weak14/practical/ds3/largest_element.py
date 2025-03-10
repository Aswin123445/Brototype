class Node :
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 
class BST:
    def __init__(self,value):
        self.root = Node(value)
    def insert(self,value):
        if self.root is None :
            self.root = Node(value)
        else :
            self._insert_recursively(self.root,value)
    def _insert_recursively(self,node,value):
        if value < node.data :
            if node.left is None :
                node.left = Node(value)
            else :
                self._insert_recursively(node.left,value)
        else :
            if node.right is None :
                node.right = Node(value)
            else :
                self._insert_recursively(node.right,value)
    def in_order(self,node):
        if node :
            self.in_order(node.left)
            print(node.data,end=' ')
            self.in_order(node.right)
        
    def search(self,value):
        return self._search_recusersively(self.root,value)
    def _search_recusersively(self,node,value):
        if node is None :
            return False 
        if node.data == value :
            return False 
        if value < node.data :
            return self._search_recusersively(node.left,value)
        return self._search_recusersively(node.right , value)
    def find_kth_element(self,k):
        self.count = 0 
        self.kthvalue = None 
        self.in_order_reverse(self.root,k)
        return self.kthvalue
    def in_order_reverse(self,node,k):
        if node is None or self.count >= k :
            return 
        
        self.in_order_reverse(node.right,k)
        
        self.count += 1 
        if self.count == k :
            self.kthvalue = node.data
            return 
        
        self.in_order_reverse(node.left,k)
    
b = BST(10)
b.insert(20)
b.insert(400)
b.insert(30)
b.in_order(b.root)
print()
print(b.find_kth_element(2))

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
            self._insert_recursively(self.root,value)
    def _insert_recursively(self,node,value):
        if value < node.data :
            if node.left is None :
                node.left = Node(value)
            else :
                self._insert_recursively(node.left,value)
        else :
            if node.right is None :
                node.right = Node(value)
            else :
                self._insert_recursively(node.right,value)
    def in_order(self,node):
        if node:
            self.in_order(node.left)
            print(node.data,end=' ')
            self.in_order(node.right)
    def kth_element(self,k):
        self.count = 0 
        self.amount = None 
        self._reverse_inorder(self.root,k)
        return self.amount
    def _reverse_inorder(self,node,k):
        if node is None or self.count >= k :
            return 
        self._reverse_inorder(node.right,k)
        
        self.count += 1 
        if self.count == k :
            self.amount = node.data 
        
        self._reverse_inorder(node.left,k)
        
    def find_closest_value(self,target):
        return self._closest_recurstion(self.root,target,float('inf'))
    def _closest_recurstion(self,node,target,closest):
        if node is None :
            return closest
        if abs(target - node.data)  < abs(target-closest):
            closest = node.data 
        if target < node.data :
            return self._closest_recurstion(node.left,target,closest)
        elif target > node.data :
            return self._closest_recurstion(node.right,target,closest)
        else :
            return closest
    
        
b = BST()
b.insert(50)
b.insert(40)
b.insert(55)
b.insert(100)
b.in_order(b.root)
print()
print(b.kth_element(4))
print(b.find_closest_value(101))