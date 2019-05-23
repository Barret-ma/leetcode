# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from Queue import Queue
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head
        if k == 1:
            return head
        pt = head
        dummy = head
        counter = 1
        roundNum = 0
        dummyHead = ListNode(-1)
        preHead = Queue()
        while pt:
            if counter == 1:
                preHead.put(pt)
            pt = pt.next
            if pt:
                counter += 1
            if counter % k == 0:
                roundNum += 1
                dummyCopy = dummy.next
                pt = pt.next
                while counter > 1:
                    counter -= 1
                    dummy.next = pt
                    pt = dummy
                    dummy = dummyCopy
                    dummyCopy = dummy.next
                if roundNum > 1:
                    dummyPreHead = preHead.get()
                    dummy.next = pt
                    dummyPreHead.next = dummy
                if not dummyHead.next:
                    dummyHead.next = dummy
                    dummy.next = pt
                pt = dummyCopy
                dummy = dummyCopy
        if not dummyHead.next:
            return head
        return dummyHead.next

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n7 = ListNode(7)
n8 = ListNode(8)

# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = n6


test = Solution()
testHead = test.reverseKGroup(n1, 2)
while testHead:
    print testHead.val
    testHead = testHead.next
