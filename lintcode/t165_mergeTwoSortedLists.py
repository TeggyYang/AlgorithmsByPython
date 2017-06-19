# --*-- coding:utf-8 --*--
# leetcode_021:https://leetcode.com/problems/merge-two-sorted-lists/#/description
# lintcode_165:http://www.lintcode.com/zh-cn/problem/merge-two-sorted-lists/


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        res = ListNode(0)
        tmp = res
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        if l1 != None:
            tmp.next = l1
        else:
            tmp.next = l2
        return  res.next



if __name__ == '__main__':
    solution = Solution()
    print "over"
