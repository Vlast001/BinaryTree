from TreeNode import Node
from enum import Enum


class Traversal(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3
    REVERSE = 4


class BinaryTree(object):
    count = 0

    def __init__(self, root=None):
        self.root = root

    def get_root(self):
        return self.root

    def set_root(self, root):
        self.root = root

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            self.count += 1
        else:
            self.add_node(self.root, key)
            self.count += 1

    def add_to_tree(self, node, key):
        if self.root is None:
            self.root = Node(key)
            self.count += 1
        else:
            if node.key == key:
                return
            if node.key > key:
                if node.left is None:
                    node.left = Node(key)
                else:
                    self.add_to_tree(node.left, key)
            else:
                if node.right is None:
                    node.right = Node(key)
                else:
                    self.add_to_tree(node.right, key)
            self.count += 1

    def add(self, key):
        node = self.root
        if self.root is None:
            self.root = Node(key)
            self.count += 1
        else:
            if node.key == key:
                return
            if node.key > key:
                if node.left is None:
                    node.left = Node(key)
                else:
                    self.add_to_tree(node.left, key)
            else:
                if node.right is None:
                    node.right = Node(key)
                else:
                    self.add_to_tree(node.right, key)
            self.count += 1

    def add_node(self, node, key):
        if node.key == key:
            return
        if node.key > key:
            if node.left is None:
                node.left = Node(key)
            else:
                self.add_node(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self.add_node(node.right, key)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, ', ', end=' ')
            self.inorder(node.right)

    def reverse_inorder(self, node):
        if node:
            self.reverse_inorder(node.right)
            print(node.key, ', ', end=' ')
            self.reverse_inorder(node.left)

    def preorder(self, this_node):
        if this_node:
            print(this_node.key, ', ', end=' ')
            self.preorder(this_node.left)
            self.preorder(this_node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key, ', ', end='')

    def print(self, traversal_type=Traversal.INORDER):
        if self.root is None:
            print("\nTree is empty")
        else:
            if traversal_type == Traversal.INORDER:
                print("\nInorder Traversal :")
                self.inorder(self.root)
            elif traversal_type == Traversal.PREORDER:
                print("\nPreorder Traversal :")
                self.preorder(self.root)
            elif traversal_type == Traversal.POSTORDER:
                print("\nPostorder Traversal :")
                self.postorder(self.root)
            elif traversal_type == Traversal.REVERSE:
                print("\nReverse inorder Traversal :")
                self.reverse_inorder(self.root)
            # print(self.count)

    @staticmethod
    def __find_deleted_node(node):
        ptr = node
        while ptr.left is not None:
            ptr = ptr.left
        return ptr

    def delete(self, key):
        self.set_root(self.delete_node(self.get_root(), key))

    def delete_node(self, node, key):
        if node is None:
            # self.count -= 1
            return node
        if key < node.key:
            node.left = self.delete_node(node.left, key)
        elif key > node.key:
            node.right = self.delete_node(node.right, key)
        else:
            if node.left is None:
                temp = node.right
                self.count -= 1
                return temp
            elif node.right is None:
                temp = node.left
                self.count -= 1
                return temp
            temp = self.__find_deleted_node(node.right)
            node.key = temp.key
            node.right = self.delete_node(node.right, temp.key)
        self.count -= 1
        return node

    def clear(self):
        self.root = None
        self.count = 0

    def clear_all_roots(self, node):
        while self.count > 0:
            self.set_root(self.delete_node(self.get_root(), node.key))
            # self.count -= 1
        # self.set_root(self.delete_node(self.get_root(), node.key))
        # self.set_root(self.delete_node(self.get_root(), node.key))
