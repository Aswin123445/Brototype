class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyList:
    def __init__(self):
        self.head = None
    def insert_begin(self,data):
        new_node = Node(data)
        if not self.head :
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
    def insert_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        if not self.head.next :
            new_node.prev= self.head
            self.head.next= new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        new_node.prev=current
        current.next = new_node
    def travrse_list(self):
        if not self.head:
            return None
        current = self.head
        while current:
            print(current.data,end="->")
            current = current.next
        print()
    #traverse list reversely
    def travere_list_reverse(self):
        if self.head is None:
            return None
        #traverse the list till end
        current = self.head
        while current.next is not None:
            current=current.next
        #traverse from the end
        while current is not None:
            print(current.data,end='->')
            current= current.prev
    #insert at the specific position befor
    def insert_pov_before(self,data,pov):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        if pov == 1 :
            new_node.next= self.head
            self.head.prev = new_node
            self.head = new_node
            return 
        #traversal 
        count = 1
        current = self.head
        while count <pov-1 and current.next :
            count +=1
            current =current.next
        if not current.next:
            return None
        new_node.next = current.next
        new_node.prev = current
        current.next.prev = new_node
        current.next = new_node
            
        
def binary_search(arr,data):
    if not arr:
        print('invalid array')   
        return 
    left = 0
    right = len(arr)-1    
    mid = int((left+right) /2)
    while left < right  and arr[mid] != data:
        if arr[mid]<data:
            left = mid + 1
        else :
            right = mid - 1
        mid = int((left + right)/2)
    if arr[mid] == data:
        return mid+1
    return -1

#binary search with recursion
def binary_search_recursion(arr,left,right,data):
    if left>right :
        print('no match found')
        return
    mid = int((left + right)/2)
    if arr[mid] == data :
        return mid + 1
    if data < arr[mid]:
        return binary_search_recursion(arr,left,mid-1,data)
    return binary_search_recursion(arr,mid+1,right,data)

        
        
d = DoublyList()
d.insert_begin(10)
d.insert_begin(20)
d.insert_end(100)
d.travrse_list()
d.travere_list_reverse()
print()
d.insert_pov_before(1200,2)
d.travrse_list()
data = binary_search([20,30,40,64],1)
print(data)

da = binary_search_recursion([10,20,30,40,50],0,5,10)
print(da)
