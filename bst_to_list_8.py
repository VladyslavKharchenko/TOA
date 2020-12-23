class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


class BinarySearchTree:

    def __init__(self, lst=None):
        if lst is None:
            lst = []
        for elem in lst:
            self.add(elem)

    root = None
    max_depth_value = None
    current_depth = 0  # for storing recursive function value

    def clear(self):
        self.root = None
        self.max_depth_value = 0
        self.current_depth = 0

    def add(self, value, node=None, flag=False):
        if flag:
            if value > node.value:
                if node.right is None:
                    node.right = Node(value)
                    return
                else:
                    self.add(value, node=node.right, flag=True)
                    return
            else:
                if node.left is None:
                    node.left = Node(value)
                    return
                else:
                    self.add(value, node=node.left, flag=True)
                    return
        try:
            if self.root is None:
                self.root = Node(value)
                self.max_depth_value = None
            else:
                self.add(value, node=self.root, flag=True)
                self.max_depth_value = None
        except TypeError as e:
            raise TypeError('Only integers and floats are allowed for storing Node values') from e

    def make_sorted_list(self, node, a=None):
        """Make sorted list from the Tree using In-order Traversal

            Args:
                :param a: initial list
                :param node: Node, root

            Returns:
                list (asc sorted)
        """
        if a is None:
            a = []
        if node is not None:
            self.make_sorted_list(node.left, a)
            a += [node.value]
            self.make_sorted_list(node.right, a)
        return a

    def max_depth(self, node=None, recursive=None):
        if recursive is None:
            if self.root is None:
                print('Tree is empty')
                self.max_depth_value = 0
                return self.max_depth_value
            if self.max_depth_value is not None:
                print('Tree has not been changed')
                return self.max_depth_value
            else:
                print('Tree has been changed')
        if node is None:
            node = self.root
        if node is self.root:
            self.current_depth = 1
        if node.right is not None:
            self.current_depth = self.current_depth + 1
            self.max_depth(node.right, recursive=True)
            self.current_depth = self.current_depth - 1
        if node.left is not None:
            self.current_depth = self.current_depth + 1
            self.max_depth(node.left, recursive=True)
            self.current_depth = self.current_depth - 1
        if (node.left is None) and (node.right is None):  # leaf reached
            if self.max_depth_value is None:
                self.max_depth_value = 0  # because '>' (at the next line) is not supported between 'int' and 'None'
            if self.current_depth > self.max_depth_value:
                self.max_depth_value = self.current_depth
        return self.max_depth_value
