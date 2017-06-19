# --*-- coding:utf-8 --*--
# leetcode_005: https://leetcode.com/problems/longest-palindromic-substring/#/description leetcode 超时
# lintcode_200：http://www.lintcode.com/zh-cn/problem/longest-palindromic-substring/

# 动态规划解法
# python中for循环需要在循环体里确定循环条件
# Python中二维数组的运用


class Solution(object):
    def longestPalindrome(self, s):
        length = len(s)
        max = 1
        ans_i = 0
        ans_j = 0
        flag = [[True for col in range(length)]for row in range(length)]
        for i in range(length):
            for j in range(length):
                if i >= j:
                    flag[i][j] = True
                else:
                    flag[i][j] = False
        for y in range(1, length):
            for x in range(0, length):
                if x < y:
                    # break
                    if s[x] == s[y]:
                        flag[x][y] = flag[x+1][y-1]
                        if y-x+1 > max:
                            max = y-x+1
                            ans_i = 0
                            ans_i = x
                            ans_j = 0
                            ans_j = y
                    else:
                        flag[x][y] = False
                x += 1
            y += 1
        # print ans_i, ans_j
        return s[ans_i:ans_j+1]


# 如何测试
if __name__ == "__main__":
    solution = Solution()
    s = "babad"
    # print s[0]
    ans = solution.longestPalindrome(s)
    print ans
    print "over"


