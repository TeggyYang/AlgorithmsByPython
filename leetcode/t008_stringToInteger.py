# --*-- coding:utf-8 --*--
# leetcode_008:https://leetcode.com/problems/string-to-integer-atoi/#/description
# lintcode_54:http://www.lintcode.com/zh-cn/problem/string-to-integer-ii/

# int的上边界和下边界


class Solution(object):
    def myAtoi(self, str):
        index = 0
        # INT_MAX = 2147483647
        INT_MAX = (1<<31)-1
        INT_MIN = -(1<<31)
        # INT_MIN = -2147483648
        while index < len(str) and str[index] == ' ':
            index += 1
        flag = 1
        if index < len(str) and str[index] == '+':
            index += 1
        elif index < len(str) and str[index] == '-':
            flag = -1
            index += 1
        ans=0
        while index < len(str):
            if str[index] < '0' or str[index] > '9':
                return ans*flag
            temp =ord(str[index])-ord('0')
            if flag == 1 and ans*10+temp > INT_MAX:
                return INT_MAX
            if flag == -1 and flag*(ans*10+temp) < INT_MIN:
                return INT_MIN
            ans = ans*10+temp
            index += 1
        return flag*ans

if __name__ == "__main__":
    solution = Solution()
    s = "-2147483649"
    ans = solution.myAtoi(s)
    print ans
    print "over"