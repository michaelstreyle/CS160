"""

Tree building exercise

Michael Streyle

NODES AND REFERENCES IMPLEMENTATION

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

    def clockwise(self):
        """Clockwise tree traversal"""
        print(self._key, end=" ")
        if self._child_right:
            self._child_right.clockwise()
        if self._child_left:
            self._child_left.clockwise()



def build_tree_oop() -> object:
    """Build a tree and return it"""
    tree = BinaryTree('a')
    tree.insert_left('b')
    tree.insert_right('c')
    tree.get_child_left().insert_right('d')
    tree.get_child_right().insert_left('e')
    tree.get_child_right().insert_right('f')
    return tree








