# class Node :
#     def __init__(self,data):
#         self.data = data 
#         self.left = None  
#         self.right = None  
# def is_valid_bst(root,min_value = float('-inf'),mix_value = float('inf')):
#     if root is None :
#         return True 
#     if not min_value < root.data < mix_value :
#         return False 
#     return (is_valid_bst(root.left,min_value,root.data) and  
#             is_valid_bst(root.right,root.data,mix_value)
#         )

# root = Node(10)
# root.left = Node(9)
# root.right = Node (40)

# print(is_valid_bst(root))

class Node:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None 
        
def is_bst(root,min_value=float('-inf'),max_value = float('inf')):
    if root is None :
        return True 
    if not (min_value < root.data < max_value) :
        return False 
    return (
          is_bst(root.left,min_value,root.data) and 
          is_bst(root.right,root.data,max_value)
        )
    
r = Node(10)
r.left = Node(4)
r.right = Node(3)
print(is_bst(r))
