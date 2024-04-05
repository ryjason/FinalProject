class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.val:
            root.left = self.insert(root.left, key)
        elif key > root.val:
            root.right = self.insert(root.right, key)
        return root

    def delete(self, root, key):
        if root is None:
            return root
        if key < root.val:
            root.left = self.delete(root.left, key)
        elif key > root.val:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.min_value_node(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)
        return root

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, root, key):
        if root is None or root.val == key:
            return root
        if root.val < key:
            return self.search(root.right, key)
        return self.search(root.left, key)

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.val, end=' ')
            self.inorder_traversal(root.right)

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
