# --*-- coding:utf-8 --*--
# leetcode_009:https://leetcode.com/problems/palindrome-number/#/description
# lintcode_491:http://www.lintcode.com/zh-cn/problem/palindrome-number/
# 将数字倒序，与原数比较


class Solution(object):
    def isPalindrome(self, x):
        temp = x
        if x < 0:
            return False
        reverse = 0
        while temp > 0:
            reverse = reverse * 10 + temp % 10
            temp /= 10
        if x == reverse:
            return True
        return False

if __name__ == "__main__":
    solution = Solution()
    num = 121
    ans = solution.isPalindrome(num)
    print ans
    print "over"