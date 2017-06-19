# --*-- coding:utf-8 --*--
# leetcode_007:https://leetcode.com/problems/reverse-integer/#/description
# lintcode_413:http://www.lintcode.com/zh-cn/problem/reverse-integer/


class Solution(object):
    def reverse(self, x):
        if x == 0:
            return 0
        symbol = 1
        if x < 0:
            symbol = -1
            x = -x
        # print x
        ans = 0
        while x > 0:
            ans = ans * 10 + x % 10
            x /= 10
        ans *= symbol
        if ans < -(1 << 31) or ans > (1 << 31)+1:  # 越界返回0
            return 0
        return ans


if __name__ == "__main__":
    solution = Solution()
    num = -123
    ans = solution.reverse(num)
    print ans
    print "over"