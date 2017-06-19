# --*-- coding:utf-8 --*--
# leetcode_006:https://leetcode.com/problems/zigzag-conversion/#/description
# lintcode_None


class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        i = 0
        j = 0
        ans = ""
        while i < numRows:
            j = i
            flag = True
            while j < len(s):
                ans += s[j]
                if i == 0 or i == numRows-1:
                    j += 2 * (numRows - 1)
                else:
                    if flag:
                        j += 2 * (numRows - 1 - i)
                        flag = False
                    else:
                        j += 2*i
                        flag = True
            i += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    s = "PAYPALISHIRING"
    ans = solution.convert(s, 3)
    print ans
    print "over"