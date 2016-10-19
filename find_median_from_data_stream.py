class RedBlackBST(object):
    _RED = True
    _BLACK = False

    def __init__(self):
        self.root = None

    def put(self, val):

    def select(self, rank):
        pass

    @property
    def size(self)
        if self.root is None:
            return 0
        return self.root.size

    @staticmethod
    def _put_to(root, val):
        if root is None:
            root = RedBlackTreeNode(val)

        if val > root.val:
            root.right = self._put_to(root.right, val)

        

    def _rotate_left(node):
        pass

    def _rotate_right(node):
        pass

    def _flip_colors(node):
        pass

    class RedBlackTreeNode(object):
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
            self.size = 1
            # True: red, False: black
            self.color = True


class MedianFinder(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()