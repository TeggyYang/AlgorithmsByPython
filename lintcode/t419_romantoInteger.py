# --*-- coding:utf-8 --*--
# leetcode_013:https://leetcode.com/problems/roman-to-integer/#/description
# lintcode_419:http://www.lintcode.com/zh-cn/problem/roman-to-integer/


class Solution(object):
    def romanToInt(self, s):
        ROMAN = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        if s == "":
            return 0
        index = len(s)-2
        sum = ROMAN[s[-1]]
        while index >= 0:
            if ROMAN[s[index]] < ROMAN[s[index+1]]:
                sum -= ROMAN[s[index]]
            else:
                sum += ROMAN[s[index]]
            index -= 1
        return sum

if __name__ == "__main__":
    solution = Solution()
    s = "IV"
    ans = solution.romanToInt(s)
    print ans
    print "over"