# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            temp = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i + 1 < len(lists) else None
                temp.append(self.mergeTwo(l1, l2))
            #this terminates while loop, list length becomes 1 
            lists = temp
        return lists[0]
    
    def mergeTwo(self, l1, l2):
        if not l1: return l2
        elif not l2: return l1
        
        elif l1.val < l2.val:
            l1.next = self.mergeTwo(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwo(l2.next, l1)
            return l2
        