# Reverse a singly linked list.

# Example:

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:

# A linked list can be reversed either iteratively or recursively.
# Could you implement both?


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        dummyHead = ListNode(None)
        dummyHead1 = head
        dummyHead.next = head
        pointer1 = head.next
        pointer2 = None
        while pointer1.next != None:
            # pointer1 = pointer1.next
            pointer2 = pointer1.next
            pointer1.next = dummyHead.next
            dummyHead.next = pointer1
            pointer1 = pointer2
        pointer1.next = dummyHead.next
        dummyHead1.next = None
        return pointer1

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

s = Solution()
s.reverseList(n1)
