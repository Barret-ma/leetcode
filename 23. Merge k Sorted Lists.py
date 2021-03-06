# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def merge(l1, l2):
            dummy = pt = ListNode(-1)
            while l1 and l2:
                if l1.val < l2.val:
                    pt.next = l1
                    l1 = l1.next
                else:
                    pt.next = l2
                    l2 = l2.next
                pt = pt.next
            pt.next = l1 if not l2 else l2
            return dummy.next

        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        mid = len(lists) / 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return merge(left, right)


            