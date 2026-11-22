# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # Find the kth node from group_prev
            kth = self.getKth(group_prev, k)
            if not kth:
                break  # fewer than k nodes left, leave as is

            group_next = kth.next

            # Reverse the group
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # Reconnect the reversed group
            tmp = group_prev.next      # old first node, now the group's tail
            group_prev.next = kth      # kth is the new head of the group
            group_prev = tmp           # move to the end of the reversed group

        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
        