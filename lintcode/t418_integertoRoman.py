# --*-- coding:utf-8 --*--
# leetcode_012:https://leetcode.com/problems/integer-to-roman/#/description
# lintcode_418:http://www.lintcode.com/zh-cn/problem/integer-to-roman/


class Solution(object):
    def intToRoman(self, num):
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        list = ''
        for i in range(len(values)):
            while num >= values[i]:
                num -= values[i]
                list += roman[i]
        return list


if __name__ == "__main__":
    solution = Solution()
    temp = 2
    ans = solution.intToRoman(temp)
    print ans
    print "over"