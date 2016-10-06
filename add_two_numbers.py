# Definition for singly-linked list.
#class ListNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.next = None


class Solution(object):
    def __init__(self):
        self.result = self.cur_node = None

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        while l1 and l2:
            val = l1.val + l2.val + carry

            if val >= 10:
        	    node = ListNode(val % 10)
        	    carry = 1
            else:
                node = ListNode(val)
                carry = 0

            if self.cur_node is None:
        	   self.result = self.cur_node = node
            else:
        	   self.cur_node.next = node
        	   self.cur_node = self.cur_node.next

            l1, l2 = l1.next, l2.next

        l = l1 if l1 else l2
        while l:
            val = l.val + carry
            if val >= 10:
        	    node = ListNode(val % 10)
        	    carry = 1
            else:
                node = ListNode(val % 10)
                carry = 0   

            self.cur_node.next = node
            self.cur_node = self.cur_node.next
            l = l.next

        if carry:
            node = ListNode(1)
            self.cur_node.next = node

        return self.result
