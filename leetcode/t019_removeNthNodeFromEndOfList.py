# --*-- coding:utf-8 --*--
# leetcode_019:https://leetcode.com/problems/remove-nth-node-from-end-of-list/#/description
# lintcode_174:http://www.lintcode.com/zh-cn/problem/remove-nth-node-from-end-of-list/


class ListNode(object):  # Definition of ListNode
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        res = ListNode(0)
        res.next = head
        tmp = res
        for i in range(0, n):
            head = head.next
        while head is not None:
            head = head.next
            tmp = tmp.next
        tmp.next = tmp.next.next
        return res.next

if __name__ == '__main__':
    solution = Solution()
    head = ListNode(0)
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    head.next = l1
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    # while head.next != None:
    #     print head.next.val
    #     head = head.next
    n = 2
    ans = solution.removeNthFromEnd(head.next, n)
    while ans is not None:
        print ans.val
        ans = ans.next
    print "over"
