# --*-- coding:utf-8 --*--
# leetcode_024:https://leetcode.com/problems/swap-nodes-in-pairs/#/description
# lintcode_451:http://www.lintcode.com/zh-cn/problem/swap-nodes-in-pairs/


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while p.next and p.next.next:
            tmp = p.next.next
            p.next.next = tmp.next
            tmp.next = p.next
            p.next = tmp
            p = p.next.next
        return dummy.next


if __name__ == "__main__":
    solution = Solution()
    head = ListNode(0)
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    head.next = l1
    l1.next = l2
    l2.next = l3
    l3.next = l4
    # while head.next is not None:
    #     print " "+ str(head.next.val)
    #     head = head.next
    # print ""
    ans = solution.swapPairs(head.next)

    while ans is not None:
        print ans.val
        ans = ans.next
    print "over"