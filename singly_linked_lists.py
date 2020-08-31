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

    # This inserts after a given node
    def insert_after_given_node(self, given_node, data):

        if not given_node:
            print("Given node not on the list")
            return

        # create new node
        new_node = Node(data)
        
        # new_node.next points to given_node.next
        new_node.next = given_node.next
        # given_node.next is now the new_node
        given_node.next = new_node

    
    def swap_nodes(self, key_1, key_2):
        # we need to disqualify the keys if they are the
        # same, since swapping the same exact keys in a SLL
        # is useless
        if key_1 == key_2:
            return

        # The first pointer:
        # we start at the head when looking for both keys
        # since nothing comes before the head, we can set that 
        # to None
        prev_1 = None
        cur_1 = self.head
        # while we do have a self.head and its current
        # data value does not equal to key_1
        while cur_1 and cur_1.data != key_1:
            # move along the list
            prev_1 = cur_1
            cur_1 = cur_1.next


        # The second pointer:
        # we start at the head when looking for both keys
        # since nothing comes before the head, we can set that 
        # to None
        prev_2 = None
        cur_2 = self.head
        # while we do have a self.head and its data value
        # is not equal to key_2
        while cur_2 and cur_2.data != key_2:
            # move along the list
            prev_2 = cur_2
            cur_2 = cur_2.next


        # if neither cur_1 or cur_2 are not on the list
        # then return
        if not cur_1 or not cur_2:
            return

        # in the case where a previous node exists
        # and a node we're swapping, is not a head node
        if prev_1:
            # change the pointer to point to cur_2
            prev_1.next = cur_2
        # if it is a head node
        else:
            # make head cur_2
            self.head = cur_2
        
        if prev_2:
            # change the pointer to point to cur_1
            prev_2.next = cur_1
        else:
            self.head = cur_1

        # swap
        cur_1.next, cur_2.next = cur_2.next, cur_1.next



# Define a LinkedList object
llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
# uncomment to print
# llist.print_list()

# uncomment to insert a node after "B"
# our given node here is "B" which is head.next
# llist.insert_after_given_node(llist.head.next, "X")

# uncomment to prepend
# llist.prepend("E")


# Swap Nodes
# uncomment to swap if none are head
# llist.swap_nodes("B", "C")

# uncomment to swap if 1 is head
# llist.swap_nodes("A", "C")

# uncomment to swap if the other is head
# llist.swap_nodes("C", "A")

# uncomment to "swap" if both nodes are the same
# llist.swap_nodes("A", "A")

llist.print_list()


