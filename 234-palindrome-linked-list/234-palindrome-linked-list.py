# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #can use array and two pointers for O(n) space
        fast = head
        slow = head
        
        #find middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        #reverse second half
        prev = None
        
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        #palindrome check, prev should be at last
        
        left, right = head, prev
        #right will end at middle because we pointed middle next to None
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True