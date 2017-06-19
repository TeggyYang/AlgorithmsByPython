# --*-- coding:utf-8 --*--
# leetcode_003: https://leetcode.com/problems/longest-substring-without-repeating-characters/#/description
# lintcode_384: https://leetcode.com/problems/longest-substring-without-repeating-characters/#/solutions


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        hash = {}
        max_ans = 0
        j = 0
        for i in range(0, len(s)):
            if s[i] in hash:
                j = max(j, hash[s[i]]+1)
            hash[s[i]] = i
            max_ans = max(max_ans, i - j + 1)
        return max_ans


if __name__ == "__main__":
    solution = Solution()
    s = "abcabcbb"
    ans = solution.lengthOfLongestSubstring(s)
    print ans
    print "over"


