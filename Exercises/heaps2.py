"""

Binary Tree implementation

Michael Streyle
11/15/18

"""


class BinaryTree:
    """Binary Tree implementation as nodes and references"""

    def __init__(self, key):
        self._key = key
        self._child_left = None
        self._child_right = None

    def get_root_val(self):
        """Get root key value"""
        return self._key

    def set_root_val(self, new_key):
        """Set root key value"""
        self._key = new_key

    def get_child_left(self):
        """Get left child"""
        return self._child_left

    def set_child_left(self, new_child_left):
        """Set left child"""
        self._child_left = new_child_left

    def get_child_right(self):
        """Get right child"""
        return self._child_right

    def set_child_right(self, new_child_right):
        """Set right child"""
        self._child_right = new_child_right

    def is_leaf(self):
        """Check if a node is leaf"""
        return (not self._child_left) and (not self._child_right)

    def insert_left(self, new_node):
        """Insert left subtree"""
        new_subtree = BinaryTree(new_node)
        if self._child_left != None:
            new_subtree.set_child_left(self._child_left)
        self._child_left = new_subtree

    def insert_right(self, new_node):
        """Insert right subtree"""
        new_subtree = BinaryTree(new_node)
        if self._child_right != None:
            new_subtree.set_child_right(self._child_right)
        self._child_right = new_subtree

    def preorder(self):
        """Pre-order tree traversal"""
        print(self._key, end=" ")
        if self._child_left:
            self._child_left.preorder()
        if self._child_right:
            self._child_right.preorder()

    def inorder(self):
        """In-order tree traversal"""
        if self._child_left:
            self._child_left.inorder()
        print(self._key, end=" ")
        if self._child_right:
            self._child_right.inorder()

    def postorder(self):
        """Post-order tree traversal"""
        if self._child_left:
            self._child_left.postorder()
        if self._child_right:
            self._child_right.postorder()
        print(self._key, end=" ")

    def height(self):
        """Height of a tree"""
        if not self._key:
            return -1
        if self._child_left:
            height_left = self._child_left.height()
        else:
            height_left = -1

        if self._child_right:
            height_right = self._child_right.height()
        else:
            height_right = -1

        return 1 + max(height_left, height_right)

    def size(self):
        """Count nodes in a tree"""
        if not self._key:
            return 0
        if self._child_left:
            children_left = self._child_left.size()
        else:
            children_left = 0

        if self._child_right:
            children_right = self._child_right.size()
        else:
            children_right = 0

        return 1 + children_left + children_right