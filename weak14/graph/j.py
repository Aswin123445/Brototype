class Node:
    def __init__(self,val):
        self.val = val 
        self.left = None 
        self.right =None 
        
class BST:
    def __init__(self):
        self.root = None 
        
    def insert(self,val):
        new_node = Node(val)
        if not self.root :
            self.root = new_node 
            return 
        
        stack = [self.root]
        while stack :
            current = stack.pop()
            if val < current.val:
                if not current.left :
                    current.left = new_node 
                    return 
                stack.append(current.left)
            else :
                if not current.right :
                    current.right = new_node
                    return 
                stack.append(current.right)
                
    def search(self,val):
        current = self.root
        while current :
            if current.val == val :
                return True 
            elif val< current.val:
                current = current.left 
            else :
                current = current.right 
        return False 
        
        
    def in_order(self):
        stack = []
        current = self.root 
        while stack or current :
            while current :
                stack.append(current)
                current = current.left 
            current = stack.pop()
            print(current.val,end= " ")
            current = current.right 
            
    def min_node(self,node):
        current = node
        while current.left :
            current = current.left 
        return current
        
    def delete(self,val):
        def delete_node(node,val):
            if not node :
                return node 
            if val < node.val:
                node.left = delete_node(node.left,val)
            elif val > node.val:
                node.right = delete_node(node.right,val)
            else :
                if not node.left:
                    return node.right 
                elif not node.right:
                    return node.left
                
                temp = self.min_node(node.right)
                node.val = temp.val
                node.right = delete_node(node.right,temp.val)
            return node 
            
        self.root = delete_node(self.root,val)
        
#check given tree is binary tree 
#in order traversal traversal 
def is_bst(root):
    stack = []
    pre = float('-inf')
    current = root
    while stack or current:
        while current :
            stack.append(current)
            current = current.left 
        current =stack.pop()
        if current.val <= pre :
            return False
        pre = current.val
        current = current.right
    return True

#counting the total number of right nodes in a binary search tree

        
            
        
        
        
        
#checking two binary trees are identical 
def identical(b1,b2):
    stack = [(b1,b2)]
    while stack:
        node1,node2 = stack.pop()
        if not node1 and not node2:
            continue
        if not node1 or not node2 or node1.val != node2.val:
            return False 
        stack.append((node1.right,node2.right))
        stack.append((node2.left,node2.left))
        
    return False
    
    
#finding the nth largest element in a binary tree
def nthlargest(root,val):
    #inordertraversal
    current = root
    stack = []
    count = 0
    while stack or current:
        while current:
            stack.append(current)
            current = current.right
        current = stack.pop()
        count += 1 
        if count == val:
            return current.val
        current = current.left
        
#finding the closest value in binary tree
def closest(root,val):
    #inorder searching will do
    stack = []
    current = root 
    while stack or current:
        while current :
            stack.append(current)
            current = current.right
        current = stack.pop()
        if current.val <= val:
            return current.val
        current = current.left
        
        
       
b = BST()
b.insert(20)
b.insert(10)
b.insert(40)
b.insert(8)
b.insert(43)
b.in_order()
b.delete(43)
print()
b.in_order()
print()
print(nthlargest(b.root,1))
print(closest(b.root,12))
print(is_bst(b.root))