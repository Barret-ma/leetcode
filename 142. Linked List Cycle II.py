# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

# Note: Do not modify the linked list.

 

# Example 1:

# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.


# Example 2:

# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the first node.


# Example 3:

# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.


 

# Follow up:
# Can you solve it without using extra space?

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        firstP = head
        secondP = head
        while secondP and secondP.next:
            firstP = firstP.next
            secondP = secondP.next.next
            if firstP == secondP:
                break
        if not secondP or not secondP.next:
            return None
        firstP = head
        # indexPos = 0
        while firstP != secondP:
            firstP = firstP.next
            secondP = secondP.next
        return secondP


n0 = ListNode(0)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(-4)

n3.next = n2
n2.next = n0
n0.next = n4
n4.next = n2
# n0.next = n2
# n2.next = n0

s = Solution()
print(s.detectCycle(n3))