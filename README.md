# WhiteBoard
This repo is a collection of WhiteBoard challenges for technical interview preparation, currently only in Python. Code is commented to better promote understanding for students.


## Table of Contents
* [Singly Linked Lists](#singly-linked-lists)
* [Binary Search Trees](#binary-search-trees)
* [Circular Linked Lists](#circular-linked-lists)


## Singly Linked Lists
The singly_linked_lists.py file consists of the following methods:

```
append()
Adds a node to the end of a list

prepend()
Adds a node to the begining of a list

insert_after_given_node()
Adds a node after a certain node on the list

swap_nodes()
Swaps 2 nodes in a list

```
## Binary Search Trees
The binary_search_trees.py file consists of the following methods:

```
insert()
Creates a node at the root if there isn't one, and uses the _insert() helper method if there is

_insert()
Moves along the BST inserting node values in a sorted manner from left to right

find()
Checks to see if there is a root node and uses the _find() helper method. 
If the Node exists, it prints True, if it does not, it prints False.

_find()
Elimintes half of the tree when searching for a given node

```
## Circular Linked Lists
The cicular_linked_lists.py fil consists of the following methods:

```
prepend()
Creates a head node and points it to itself if no head node exists. Adds a node before another.

append()
Creates a head node and points it to itself if no head node exists. Adds a node after another.

print_list()
Prints all data values in the list and breaks upon returning to the head to prevent an infinite loop.

```


## Available Guides

[How to Insert a Node at a Specific Position in a Linked List](https://levelup.gitconnected.com/how-to-insert-a-node-at-a-specific-position-in-a-linked-list-2abc783a578b)

[How to Find The Merge Point of Two Linked Lists](https://levelup.gitconnected.com/how-to-find-the-merge-point-of-two-linked-lists-ba55a129caa2)



