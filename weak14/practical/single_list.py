class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
    def insert_at_begin(self,data):
        new_node=Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
    def print_list(self):
        if not self.head:
            print("the linked list is empty")
            return
        current = self.head
        while current:
            print(current.data,end="->")
            current= current.next
        print()
    #Convert array to a linked list
    def conver_array_list(self,array):
        if not array:
            print("give a valid array")
            return
        self.head = None
        new_node = Node(array[0])
        self.head = new_node
        current = self.head
        for value in array[1:]:
            new_node = Node(value)
            current.next = new_node
            current = current.next
    #delete a node with value specified
    def delete_with_value(self,value):
        if not self.head:
            print('list is empty')
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != value:
            current = current.next
        if not current.next:
            print("value is not found")
            return
        current.next = current.next.next
    #Insert a node after a node with x data
    def insert_node_after(self,data,pov):
        new_node = Node(data)
        if not self.head:
            self.head=new_node
        if pov == 1 :
            new_node.next = self.head.next
            self.head.next = new_node
            return
        count = 1
        current = self.head
        while current and count != pov:
            current=current.next
            count+=1
        if not current:
            print('invalid positon')
        new_node.next = current.next
        current.next = new_node
    def insert_node_before(self,pov,data):
        new_node  =Node(data)
        if not self.head:
            self.head = new_node
            return
        if pov == 1 :
            new_node.next = self.head
            self.head = new_node
            return
        count = 1
        current = self.head
        while current.next and count<pov-1:
            current  = current.next 
            count+= 1
        if not current:
            print('invalid pov')
            return
        new_node.next = current.next
        current.next = new_node
        
    #print elements in reverse order
    def reverse_order(self,node):
        if node is None:
            return 
        self.reverse_order(node.next)
        print(node.data,end='<-')
    #remove duplicate from sorted singly list 
    def sorted_list(self):
        if not self.head:
            return 
        current = self.head
        while current.next and current.next.data != current.data :
            current= current.next
        if not current.next:
            return 
        current.next = current.next.next
            
node = LinkedList()
node.insert_at_end(10)
node.insert_at_end(30)
node.insert_at_end(50)
node.insert_at_begin(9)
node.insert_at_begin(9)
node.print_list()
node.delete_with_value(100)
node.print_list()
# node.insert_node_after(76,4)
node.print_list()
# node.insert_node_before(5,32)
node.print_list()
node.reverse_order(node.head)
node.sorted_list()
print()
node.print_list()
