# Doubly Linked Lists

class doubly_node:
    def __init__(self, value, next = None, prev = None):
        self.value = value 
        self.next = next 
        self.prev = prev

    def __str__(self):
        return str(self.value)

# create nodes
head = tail = doubly_node(0)

# display list - O(n)
def display(head):
    curr = head 
    elements = []
    while curr:
        elements.append(str(curr.value))
        curr = curr.next
    print(" <-> ".join(elements))

display(head)

# insert at beginning - O(1)
def insert_at_beginning(head, tail, value):
    new_node = doubly_node(value)
    new_node.next = head 
    head.prev = new_node
    return new_node, tail

head, tail = insert_at_beginning(head, tail, -1)
display(head)

# insert at end - O(1)
def insert_at_end(head, tail, value):
    new_node = doubly_node(value)
    tail.next = new_node
    new_node.prev = tail
    return head, new_node

head, tail = insert_at_end(head, tail, 1)
display(head)
