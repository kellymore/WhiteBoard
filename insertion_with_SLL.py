# to create a node
class Node:
    # constructor
    # every node will consist of .next and data
    def __init__(self, data):
        # defining obj of this class
        self.data = data
        # something we will set as we make use of the Node
        # but initially we can set this to None
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    # This prints the data of each node on the list
    def print_list(self):
        cur_node = self.head
        
        # while that current node is not None
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next  

    # This adds a node to the end of a list
    def append(self, data):
        # create node
        new_node = Node(data)

        # what if the list is empty?
        if self.head is None:
            # we can set the head pointer to the node
            # the we just created
            self.head = new_node
            return
        # What if the list is NOT empty?
        # And we need to get to the place where the new
        # node needs to be inserted?
        if self.head:
            # pointer will start at the head,
            # until it points to None
            pointer = self.head
            # and then when we get to None, we go ahead
            # and input the new node into the list
            # so while pointer.next is not None
            # or while there is a pointer.next
            while pointer.next:
                # This basically just moves the pointer to the righ
                # while we continue the while loop
                pointer = pointer.next
            # then when we break the while loop.
            # when we hit pointer.next is None
            # we append to the list
            pointer.next = new_node

    # This adds a node in the begining of a list
    def prepend(self, data):
        # create a node
        new_node = Node(data)

        # head is the next node of the new node
        new_node.next = self.head
        # and the new node becomes the head
        self.head = new_node






# Define a LinkedList object
llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.prepend("E")
llist.print_list()


