class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def list_nodes():
    first = Node(100)
    second = Node(200)
    third = Node("tapan")

    head = first
    first.next = second
    second.next = third
    tail = insert_at_end(head,'yawalkar')
    third.next = tail
    tail.next = insert_at_end(head,1000)
    head = insert_at_beginning(head,20)
    printLinkedList(head)

def printLinkedList(head):
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next

def insert_at_beginning(head, data):
    new_node = Node(data)
    curr = head
    head = new_node
    new_node.next = curr
    return head

def insert_at_end(head,data):
    tail_node = Node(data)
    curr = head
    while curr:
        if curr.next == None:
            break
        curr = curr.next
    curr.next = tail_node
    return tail_node

if __name__ == "__main__":
    list_nodes()