class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        # create a new node
        new_node = Node(data)

        # pointer
        cur = self.head

        # head is the next node of the new node
        # (prepending)
        new_node.next = self.head

        if not self.head:
            # cicles in on itself
            # see if not self.not logic in append for another
            # way to do this
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node
        

    def append(self, data):
        # if there is no head
        if not self.head:
            # create one by nreating a node
            self.head = Node(data)
            # since this is a circular list,
            # we need the pointer of head to
            # point to itself
            self.head.next = self.head
        else:
            # create a new node
            new_node = Node(data)
            # start at the head (pointer)
            cur = self.head
            # while the self.head pointer does not point to itself
            while cur.next != self.head:
                # move along the list
                cur = cur.next
            # create a new node right before cur.next points to self.head
            cur.next = new_node
            # now the new node should point to the head
            new_node.next = self.head

            

    def print_list(self):
        # pointer
        cur_node = self.head

        # while we have a self.head or a node to point to
        while cur_node:
            print(cur_node.data)
            # move along
            cur_node = cur_node.next
            # because this is a circular linked list 
            # and the pointer will never point to None
            # it will just keep going around in circles
            # we need to put in a break point
            # or this while loop will become an infinte loop
            if cur_node == self.head:
                break



cllist = CircularLinkedList()
cllist.append("C")
cllist.append("D")
cllist.prepend("B")
cllist.prepend("A")
cllist.print_list()
