# --*-- coding:utf-8 --*--
# leetcode_020:https://leetcode.com/problems/valid-parentheses/#/description
# lintcode_423:http://www.lintcode.com/zh-cn/problem/valid-parentheses/


class Solution(object):
    def isValid(self, s):
        stack = []  # 模拟栈
        for ch in s:
            if ch == '{' or ch == '[' or ch == '(':
                stack.append(ch)
            else:
                if not stack:  # 栈必须非空
                    return False
                if ch == ')' and stack[-1] != '(' or ch == ']' and stack[-1] != '[' or ch == '}' and stack[-1] != '{':
                    return False
                stack.pop()
        return True


if __name__ == "__main__":
    solution = Solution()
    str = "{}[]{)"
    ans = solution.isValid(str)
    print ans
    print "over"
