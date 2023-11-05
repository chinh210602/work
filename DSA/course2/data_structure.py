class Node():
    def __init__(self, value = None):
        self.value = value
        self.next = None


class SLinkedList():
    def __int__ (self):
        self.head = None

    def insert(self, node, next_node):
        pass

    def push_front(self, node):
        node.next = self.head.next
        self.head.next = node

    def pop_front(self):
        top_node = self.head.next
        self.head.next = top_node.next
        top_node.next = None

        return top_node

    def push_back(self, node):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        
        current_node.next = node

    