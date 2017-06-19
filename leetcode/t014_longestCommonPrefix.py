# --*-- coding:utf-8 --*--
# leetcode_014:https://leetcode.com/problems/longest-common-prefix/#/description
# lintcode_78：http://www.lintcode.com/zh-cn/problem/longest-common-prefix/
# 最长公共前缀


class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) <= 1:
            return strs[0] if len(strs) == 1 else ""
        index = 0
        min_len = 0
        min_len = min(len(s) for s in strs)
        while index < min_len:  # 最小的字符串长度
            for i in range(1, len(strs)):  # 每个字符串依次比较相同的索引值的字符
                if strs[i][index] != strs[i-1][index]:
                    return strs[0][:index]
            index += 1
        return strs[0][:index]



if __name__ == "__main__":
    solution = Solution()
    list = []
    list.append("ABCD")
    list.append("ABEF")
    list.append("ACEF")
    ans = solution.longestCommonPrefix(list)
    print ans
    print "over"
