# Singly Linked Lists

class singly_node:
    def __init__(self, value, next = None):
        self.value = value 
        self.next = next 

    def __str__(self):
        return str(self.value)

# creating some nodes
head = singly_node(0)
a = singly_node(1)
b = singly_node(2)
c = singly_node(3)

# chaining
head.next = a 
a.next = b
b.next = c

# traverse the list - O(n)
curr = head 
while curr:
    print(curr)
    curr = curr.next

# display the list - O(n)
def display(head):
    elements = []
    curr = head 
    while curr:
        elements.append(str(curr))
        curr = curr.next
    print(' -> '.join(elements)) # displays 0 -> 1 -> 2 instead of [0, 1, 2]

display(head)

# check of linked list contains value - O(n)
def contains(head, value):
    curr = head 
    while curr:
        if curr.value == value:
            return True 
        curr = curr.next
    return False

print(contains(head, 0)) # True
print(contains(head, -1)) # False
