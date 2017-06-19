# --*-- coding:utf-8 --*--
# leetcode_022:https://leetcode.com/problems/generate-parentheses/#/description
# lintcode_451:http://www.lintcode.com/zh-cn/problem/swap-nodes-in-pairs/


class Solution:
    # @param an integer
    # @return a list of string
    # @draw a decision tree when n == 2, and you can understand it!
    def helpler(self, l, r, item, res):
        if r < l:
            return
        if l == 0 and r == 0:
            res.append(item)
        if l > 0:
            self.helpler(l - 1, r, item + '(', res)
        if r > 0:
            self.helpler(l, r - 1, item + ')', res)

    def generateParenthesis(self, n):
        if n == 0:
            return []
        res = []
        self.helpler(n, n, '', res)
        return res


if __name__ == "__main__":
    solution = Solution()
    ans = solution.generateParenthesis(3)
    print ans
    print "over"