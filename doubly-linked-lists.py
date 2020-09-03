class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):

        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            # pointer
            cur = self.head
            
            # while there is a next node
            while cur.next:
                # move along the list
                cur = cur.next
            # create a new node once we found the last
            cur.next = new_node
            # set the prev pointer
            new_node.prev = cur
            # set the next pointer
            new_node.next = None
            
    def prepend(self, data):
        new_node = Node(data)

    def print_list(self):
        cur = self.head

        while cur:
            print(cur.data)
            cur = cur.next


dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)

dll.print_list()