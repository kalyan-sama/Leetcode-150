'''
Difficulty: Medium

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

'''

#Method-1:
'''
User 2-pointer method to find the node to delete
The distance between the 2 pointers is n.
When R moves to the end of list, L will be at the node to delete.

To delete a node, we need to have the previous node. So, we create a dummy node at head and start L from dummy node
This way, the left pointer will be at previous node. Update the pointers accordingly and remove dummy node at last.
'''

#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        left, right = dummy, head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        deleted_node = left.next
        left.next = deleted_node.next
        deleted_node.next = None

        return dummy.next
        
#Time: O(n)
#Space: O(1)
