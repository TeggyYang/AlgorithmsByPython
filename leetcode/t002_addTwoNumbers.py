# --*-- coding:utf-8 --*--
# leetcode_002:https://leetcode.com/problems/add-two-numbers/#/description
# lintcode_167：http://www.lintcode.com/zh-cn/problem/add-two-numbers/


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        ptr = head
        carry = 0
        if l1 == None and l2 == None:
            return None
        while l1 != None and l2 != None:
            sum = 0
            sum = carry + l1.val + l2.val
            ptr.next = ListNode(sum % 10)
            carry = sum / 10
            l1 = l1.next
            l2 = l2.next
            ptr = ptr.next
        while l1 != None:
            sum = 0
            sum = carry + l1.val
            ptr.next = ListNode(sum % 10)
            carry = sum / 10
            l1 = l1.next
            ptr = ptr.next
        while l2 != None:
            sum = 0
            sum = carry + l2.val
            ptr.next = ListNode(sum % 10)
            carry = sum / 10
            l2 = l2.next
            ptr = ptr.next
        if carry != 0:
            ptr.next = ListNode(carry)
        return head.next


# 如何测试
if __name__ == "__main__":
    solution = Solution()
    print "over"