class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def findMiddle(self,head):
        slow_ptr = head
        fast_ptr = head
        
        while fast_ptr is not None and fast_ptr.next is not None  :
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        return slow_ptr.data
        
        

if __name__ == '__main__':
    llist = LinkedList()
    head = Node('my')
    head.next = Node('name')
    head.next.next = Node('is')
    head.next.next.next = Node('tapan')
    head.next.next.next.next = Node('yawalkar')

    llist = LinkedList()
    print(llist.findMiddle(head))