class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

def has_cycle(head):
    visited = []
    next = head.next
    while(next not in visited and next != None):
        visited.append(next)
        next = next.next
    if next == None:
        return False
    else:
        return True

def findMergeNode(head1, head2):
    first = [head1]
    second = [head2]
    next_first = head1.next
    next_second = head2.next
    while(next_first != None):
        first.append(next_first)
        next_first = next_first.next
    while(next_second != None):
        second.append(next_second)
        next_second = next_second.next
    for i in first:
        if i in second:
            return i.data