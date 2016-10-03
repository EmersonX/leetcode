# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class EmptyStackError(Exception):
    pass

class Stack(object):
    def __init__(self):
        self.stack = []
        self.top = 0

    def push(self, item):
        self.stack.append(item)
        self.top += 1

    def pop(self):
        if self.top == 0:
            raise EmptyStackError()

        item = self.stack.pop()
        self.top -= 1
        return item

    def is_emtpy(self):
        if self.top:
            return False
        return True


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        # 用栈记录遍历的路径节点
        self.iter_node_stack = Stack()
        self._iter(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.iter_node_stack.is_emtpy():
            return False
        return True

    def next(self):
        """
        :rtype: int
        """
        node = self.iter_node_stack.pop()
        if node.right:
            self._iter(node.right)
        return node.val

    def _iter(self, node):
        """
        把遍历左子树的路径记录下来
        """
        while node:
            self.iter_node_stack.push(node)
            node = node.left


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())