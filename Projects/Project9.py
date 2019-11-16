"""

Morse code encoding and decoding

Michael Streyle
11/13/18

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




class Coder:
    """Morse Code Encoder/Decoder"""

    def __init__(self, file_in: str):
        """Constructor"""
        code_dict = {}
        with open("morse.txt") as file:
            for line in file:
                (key, val) = line.split()
                code_dict[key] = val

        self.morse_tree = BinaryTree(None)
        self.codes = code_dict.values()
        self.letters = code_dict.keys()
        self.current_node = self.morse_tree
        for (i,j) in zip(self.codes, self.letters):
            self.follow_and_insert(i, j)
        
        
        
    def follow_and_insert(self, code_str: str, letter: str):
        """Follow the tree and insert a letter"""
        self.current_node = self.morse_tree
        for char in code_str:
            if char == '.' and self.current_node.get_child_left() == None:
                self.current_node.insert_left(' ')
                self.current_node = self.current_node.get_child_left()
            elif char == '.' and self.current_node.get_child_left() != None:
                self.current_node = self.current_node.get_child_left()
            elif char == '-' and self.current_node.get_child_right() == None:
                self.current_node.insert_right(' ')
                self.current_node = self.current_node.get_child_right()
            elif char == '-' and self.current_node.get_child_right() != None:
                self.current_node = self.current_node.get_child_right()
        self.current_node.set_root_val(letter)


    def follow_and_retrieve(self, code_str: str):
        """Follow the tree and retrieve a letter"""
        try:
            current_node = self.morse_tree
            for char in code_str:
                if char == '.':
                    current_node = current_node.get_child_left()
                if char == '-':
                    current_node = current_node.get_child_right()
            if current_node != None:
                return current_node.get_root_val()
        except:
            pass
    
        
    def find_path(self, tree: object, letter: str, path: str):
        """Find a key"""
        if tree:
            if tree.get_root_val() == letter:
                return path
            else:
                return self.find_path(tree.get_child_left(), letter, path + '.') or self.find_path(tree.get_child_right(), letter, path + '-')
        else:
            return False
        
        
        

    

    def encode(self, msg: str):
        """Encode a message"""
        try:
            message = []
            mi = ''
            for c in msg.strip(' '):
                if c == ' ':
                    message.append(' ')
                else:
                    if c not in self.letters:
                        raise ValueError()
                    else:
                        p = self.find_path(self.morse_tree, c, mi)
                        message.append(str(p))
                        message.append(' ')
            return ''.join(message).replace('  ', ' ')
        except:
            raise ValueError("Could not encode {}: {} is not in the tree".format(msg, c))




    def decode(self, code: str):
        """Decode a message"""
        try:
            decoded = ''
            li = code.split()
            for i in li:
                d = self.follow_and_retrieve(i)
                decoded = decoded + d
            return decoded
        except:
            raise ValueError("Could not decode {}: {} is not in the tree".format(code, code))


def main():
    morse_coder = Coder("morse.txt")
    print("Encoding 'sos'")
    print("Expected: ... --- ...")
    print("Encoded : {}".format(morse_coder.encode("sos")))
    print("---")
    print("Encoding 'data structures'")
    print("Expected: -.. .- - .- ... - .-. ..- -.-. - ..- .-. . ... ")
    print("Encoded : {}".format(morse_coder.encode("data structures")))
    print("---")
    print("Encoding '$$'")
    print("Expected: Error message")
    try:
        print("Encoded : {}".format(morse_coder.encode("$$")))
    except ValueError as ve:
        print("ERROR: {}".format(ve))
    print("---")
    print("Decoding '.... . .-.. .-.. --- --..-- -.-. ... .---- -.... -----'")
    print("Expected: hello,cs160")
    test_str = ".... . .-.. .-.. --- --..-- -.-. ... .---- -.... -----"
    print("Decoded : {}".format(morse_coder.decode(test_str)))


if __name__ == "__main__":
    main()