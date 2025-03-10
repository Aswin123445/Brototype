class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_node_begin(self,data):
        new_node = Node(data)
        if not self.head :
            self.head = new_node
            return 
        new_node.next = self.head
        self.head = new_node
    def print_node(self):
        if self.head is None :
            return None
        current = self.head 
        while current :
            print(current.data,end='->')
            current = current.next
        print()
    def merge_sorted_list(self,other_list):
        dummy = Node(0)
        first = self.head
        second = other_list.head
        tail =dummy
        while first and second :
            if first.data < second.data :
                tail.next = first
                first = first.next
            else :
                tail.next = second
                second = second.next
            tail = tail.next
        tail.next  = first if first else second
        self.head = dummy.next
    #Remove N'th node from the end of the List(fast,slow)
    def n_node_end(self,n):
        dummy = Node(0)
        dummy.next = self.head
        fast = slow = dummy
        for i in range(n+1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        self.head = dummy.next
        
def remove_char(string,char):
    print(string)
    if string == '':
        return ''
    if string[0] == char:
        return remove_char(string[1:],char)
    else :
        return string[0]+remove_char(string[1:],char)
    
def reverse_string(string):
    if string == '':
        return ''
    return reverse_string(string[1:])+string[0]

def second_largest_element(li):
    first = 0
    second = 0
    for i in li:
        if i > first :
            second = first
            first  = i
            print(first)
        elif i > second :
            second = i
        
    print(second)
    
    [10,1,30,20,100,40]


l = LinkedList()
l.insert_node_begin(100)
l.insert_node_begin(90)
l.insert_node_begin(80)
l.insert_node_begin(70)

r  = LinkedList()
r.insert_node_begin(50)
r.insert_node_begin(40)
r.insert_node_begin(30)
l.print_node()
l.merge_sorted_list(r)
l.print_node()
print(remove_char('malayalam','m'))
print(reverse_string('aswin'))
second_largest_element([-10,1,30,20,100,40])


def factorial(num):
    if num == 1 :
        return 1
    return factorial(num-1)*num
print(factorial(5))
