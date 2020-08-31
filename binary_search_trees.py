class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None



    # insert

    def insert(self, data):
        # create a node in the root if it is None
        if self.root is None:
            self.root = Node(data)
        else: 
            self._insert(data, self.root)


    def _insert(self, data, cur_node):
        if data < cur_node.data:
            # check if its None, and create a Node if it is
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        
        elif data > cur_node.data:
            # check if its None and create a node if it is
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)

        else:
            print("Value already present in tree.")




    # find

    def find(self, data):
        # if there is a root
        if self.root:
            # _find eliminates half
            is_found = self._find(data, self.root)
            if is_found:
                return True
            return False
        else:
            return None

    def _find(self, data, cur_node):
        if data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        if data == cur_node.data:
            return True


bst = BST()

# insert
bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)
# uncomment already present value
# bst.insert(5)


# print find
print(bst.find(2))


