class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self,node):
        while node is not None:
            print(f" {node.data}", end="")
            node = node.next
        print()

    def getKthFromLast(self, head, k):
        curr = head
        prev = None
        i = 1
        l = 0
        while curr is not None:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
            l += 1
        
        last = prev
        if (k > l) or k <= 0:
            return -1 
        else:
            while i < k :
                last = last.next 
                i += 1

        
        return last.data
        

if __name__ == '__main__':
    llist = LinkedList()
    head = Node('10')
    head.next = Node('5')
    head.next.next = Node('100')
    head.next.next.next = Node('5')
    #head.next.next.next.next = Node('yawalkar')

    #print("Given Linked list:",end="")
    #llist.printList(head)

    x = llist.getKthFromLast(head,0)

    #print("Reversed Linked List:", end="")
    #llist.printList(head)

    print(x)
   
    