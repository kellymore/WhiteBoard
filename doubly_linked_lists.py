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
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else: 
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def print_list(self):
        cur = self.head

        while cur:
            print(cur.data)
            cur = cur.next

    def add_after_node(self, key, data):
        # pointer
        cur = self.head
        # move the pointer
        while cur:
            # checking if there is only a head
            # and if the head has the key value
            if cur.next is None and cur.data == key:
                self.append(data)
                return
            elif cur.next is not None and cur.data == key:
                # create new node
                new_node = Node(data)
                # pointer
                nxt = cur.next
                # update pointer to point to new node
                cur.next = new_node
                # the next pointer of the new node
                new_node.next = nxt
                # updating prev pointers
                new_node.prev = cur
                nxt.prev = new_node
            cur = cur.next

    def add_before_node(self, key, data):
        # pointer
        cur = self.head
        # move pointer
        while cur:
            # checking if there is only a head
            # and if the head has the key value
            if cur.prev is None and cur.data == key:
                # prepend
                self.prepend(data)
                return
            elif cur.prev is not None and cur.data == key:
                # create a new node
                new_node = Node(data)
                # pointer
                prv = cur.prev
                # update pointer to point to the new node
                prv.next = new_node
                cur.prev = new_node
                new_node.next = cur
                new_node.prev = prv
            cur = cur.next






dll = DoublyLinkedList()
dll.prepend(0)
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.prepend(5)

# uncomment to test
# dll.add_after_node(1, 11)
# dll.add_after_node(5, 12)

dll.add_before_node(0, 555)
dll.add_before_node(5, 222)

dll.print_list()