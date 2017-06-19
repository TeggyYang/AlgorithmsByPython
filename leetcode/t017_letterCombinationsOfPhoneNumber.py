# --*-- coding:utf-8 --*--
# leetcode_017:https://leetcode.com/problems/letter-combinations-of-a-phone-number/#/description
# lintcode_425:http://www.lintcode.com/zh-cn/problem/letter-combinations-of-a-phone-number/

import copy
class Solution(object):
    def letterCombinations(self, digits):
        chr = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []
        for i in range(0, len(digits)):
            num = int(digits[i])
            tmp = []
            for j in range(0, len(chr[num])):
                if len(res):
                    for k in range(0, len(res)):
                        tmp.append(res[k] + chr[num][j])
                else:
                    tmp.append(chr[num][j])
            res = copy.copy(tmp)
        return res


if __name__ == "__main__":
    solution = Solution()
    str = "23"
    ans = solution.letterCombinations(str)
    print ans
    print "over"
