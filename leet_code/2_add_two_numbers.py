# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2, carry=0):
        value = l1.val + l2.val + carry
        current_Node = ListNode(value % 10)
        l1, l2, carry = l1.next, l2.next, value // 10
        if l1 or l2 or carry:
            l1 = l1 if l1 else ListNode()
            l2 = l2 if l2 else ListNode()
            current_Node.next = self.addTwoNumbers(l1, l2, carry)
        return current_Node


l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
ans = Solution().addTwoNumbers(l1, l2)
while ans:
    print(ans.val)
    ans = ans.next
