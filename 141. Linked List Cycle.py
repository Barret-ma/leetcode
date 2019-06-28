
# Given a linked list, determine if it has a cycle in it.

# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

 

# Example 1:

# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the second node.


# Example 2:

# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the first node.


# Example 3:

# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.


 

# Follow up:

# Can you solve it using O(1) (i.e. constant) memory?

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        if not head.next:
            return False
        pointer1 = head
        pointer2 = head

        while pointer2 and pointer2.next != None:
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next
            if pointer1 == pointer2:
                return True
        return False


# n0 = ListNode(0)
# n2 = ListNode(2)
# n3 = ListNode(3)
# n4 = ListNode(4)

# n3.next = n2
# n2.next = n0
# n0.next = n4
# n4.next = n2


n1 = ListNode(1)
n2 = ListNode(2)
# n2.next = n1
n1.next = n2


s = Solution()
print(s.hasCycle(n1))