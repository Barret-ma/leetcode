# Sort a linked list in O(n log n) time using constant space complexity.

# Example 1:

# Input: 4->2->1->3
# Output: 1->2->3->4
# Example 2:

# Input: -1->5->3->4->0
# Output: -1->0->3->4->5

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        slow = head
        fast = head
        pre = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        pre.next = None
        return self.merge(self.sortList(head), self.sortList(slow))

    def merge(self, l1, l2):
        dummy = ListNode(-1)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)

n4.next = n2
n2.next = n1
n1.next = n3

s = Solution()

s.sortList(n4)