# 3. Tree

## Introduction:
Trees stand as majestic hierarchical structures, branching out into a myriad of possibilities. As we embark on this journey, we'll uncover the essence of trees, exploring their fundamental concepts and diverse applications.

## Definition of a Tree (Hierarchical structure with nodes):
A tree is a hierarchical data structure composed of nodes connected by edges. At the pinnacle of this hierarchy lies the root node, branching out into various child nodes, forming a branching structure reminiscent of natural trees.

![](/Picture%20Files/Weixin%20Image_20240404220019.jpg)
## Terminology (Root, Parent, Child, Sibling):
To navigate the intricacies of trees, it's essential to grasp key terminology:

- Root: The topmost node of the tree, serving as the entry point for traversal.
- Parent: A node that has child nodes stemming from it.
- Child: Nodes directly connected to a parent node.
- Sibling: Nodes that share the same parent node.

## Different types of Trees (Binary Tree, Binary Search Tree)
Trees come in various forms, each tailored to specific requirements. Two notable types include:

Binary Tree: A tree in which each node has at most two child nodes, commonly referred to as the left child and right child.
Binary Search Tree (BST): A specialized binary tree that adheres to a specific ordering property, where the left child of a node contains values smaller than the node's value, and the right child contains values greater than the node's value.
Binary Tree:
In the realm of binary trees, we unravel the essence of simplicity intertwined with versatility. Basic operations serve as the cornerstone of binary tree manipulation, allowing us to navigate, manipulate, and extract information seamlessly.

## Binary Search Tree (BST):
A shining beacon of order amidst the chaos of data, the Binary Search Tree (BST) embodies precision and efficiency. Defined by its strict ordering property, the BST facilitates rapid search, insertion, and deletion operations.

Definition and properties:
A Binary Search Tree (BST) is a binary tree in which the value of each node follows a specific ordering property: the value of nodes in the left subtree is less than the node's value, and the value of nodes in the right subtree is greater than the node's value.

## Operations (Insertion, Deletion, Search):

1. Insertion: Adding a new node to the BST while maintaining the ordering property. 
- Time Complexity: O(log n) on average for a balanced BST, O(n) in the worst case.
- Explanation: When inserting a new node into a BST, we need to find the correct position in the tree based on the value of the node. In a balanced BST, each comparison reduces the search space by approximately half, leading to a time complexity of O(log n). However, in the worst case scenario, if the BST becomes unbalanced, insertion can take O(n) time when the tree degenerates into a linked list.
2. Deletion: Removing a node from the BST while preserving the ordering property.
- Time Complexity: O(log n) on average for a balanced BST, O(n) in the worst case.
- Explanation: Deletion in a BST involves finding the node to be deleted and then rearranging the tree structure while preserving the ordering property. Similar to insertion, deletion requires traversing the tree to find the node to delete, which has a time complexity of O(log n) on average in a balanced tree. However, in the worst case, deletion may take O(n) time if the tree is highly unbalanced.
3. Search: Locating a specific value within the BST with optimal efficiency, leveraging its ordered structure.
- Time Complexity: O(log n) on average for a balanced BST, O(n) in the worst case.
- Explanation: Searching in a BST exploits its ordered structure. At each step of the search, we compare the target value with the value of the current node and choose the appropriate subtree to continue the search. In a balanced BST, this reduces the search space by approximately half at each step, leading to a time complexity of O(log n). However, in the worst case, if the tree is unbalanced, searching may take O(n) time, as it requires traversing all nodes in one branch of the tree.

## Real-world examples of BST:

Below is an example of Python code demonstrating the implementation of insertion, deletion, and search operations in a binary search tree (BST):

```python
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_helper(self.root, key)

    def _insert_helper(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.key:
            root.left = self._insert_helper(root.left, key)
        else:
            root.right = self._insert_helper(root.right, key)
        return root

    def search(self, key):
        return self._search_helper(self.root, key)

    def _search_helper(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search_helper(root.left, key)
        else:
            return self._search_helper(root.right, key)

    def delete(self, key):
        self.root = self._delete_helper(self.root, key)

    def _delete_helper(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._delete_helper(root.left, key)
        elif key > root.key:
            root.right = self._delete_helper(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.key = self._min_value_node(root.right).key
            root.right = self._delete_helper(root.right, root.key)
        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.key, end=" ")
            self.inorder_traversal(root.right)

# Example usage:
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print("Inorder traversal of the constructed BST:")
bst.inorder_traversal(bst.root)

print("Search for key 40:", bst.search(40).key if bst.search(40) else "Not found")
print("Search for key 100:", bst.search(100).key if bst.search(100) else "Not found")

bst.delete(30)
print("Inorder traversal after deletion of key 30:")
bst.inorder_traversal(bst.root)
```

This code defines a TreeNode class to represent nodes in the binary search tree and a BST class that implements insertion, search, and deletion operations. The inorder_traversal method is used to perform an inorder traversal of the tree. Finally, an example usage demonstrates how to create a BST, insert elements, search for elements, and delete elements.

Here is the out-put of the code:
```python
Inorder traversal of the constructed BST:
20 30 40 50 60 70 80 #What's on the tree
Search for key 40: 40
Search for key 100: Not found
Inorder traversal after deletion of key 30:
20 40 50 60 70 80
```

## Problem to Solve:
Given an unsorted array of integers, write a Python function to create a Binary Search Tree (BST) from the array. Then, implement the following operations on the BST:

1. Insert an element into the BST.
2. Delete an element from the BST.
3. Search for an element in the BST.
4. Perform an inorder traversal of the BST.

Starter code:
```python
class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        # Implement insertion operation here
        pass

    def delete(self, root, key):
        # Implement deletion operation here
        pass

    def search(self, root, key):
        # Implement search operation here
        pass

    def inorder_traversal(self, root):
        # Implement inorder traversal operation here
        pass

# Function to create a BST from an unsorted array
def create_bst(arr):
    bst = BST()
    for key in arr:
        bst.root = bst.insert(bst.root, key)
    return bst

# Test the BST operations
def test_bst_operations():
    arr = [50, 30, 20, 40, 70, 60, 80]
    bst = create_bst(arr)

    print("Inorder traversal of the BST:")
    bst.inorder_traversal(bst.root)
    print()

    print("\nSearching for key 60:")
    result = bst.search(bst.root, 60)
    if result:
        print("Key 60 found in the BST.")
    else:
        print("Key 60 not found in the BST.")

    print("\nDeleting key 30:")
    bst.delete(bst.root, 30)
    print("Inorder traversal after deletion:")
    bst.inorder_traversal(bst.root)

test_bst_operations()

```
[Answer](Python%20Files/BSTanswer.py)

[Back](./README.md)