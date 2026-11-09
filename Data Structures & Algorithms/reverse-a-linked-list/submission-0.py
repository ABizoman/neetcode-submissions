# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        front = head
        end_node = front
        if front:
            while end_node.next:
                val = end_node.next.val
                new_front = ListNode(val)
                new_front.next = front
                front = new_front
                end_node.next = end_node.next.next



        return front