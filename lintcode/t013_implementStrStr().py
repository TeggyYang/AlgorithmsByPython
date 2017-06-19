# --*-- coding:utf-8 --*--
# leetcode_028:https://leetcode.com/problems/implement-strstr/#/description
# lintcode_013:http://www.lintcode.com/zh-cn/problem/strstr/


class Solution(object):
    def strStr(self, haystack, needle):
        if source is None or target is None:
            return -1
        len_s = len(source)
        len_t = len(target)
        for i in range(len_s - len_t + 1):
            j = 0
            while (j < len_t):
                if source[i + j] != target[j]:
                    break
                j += 1
            if j == len_t:
                return i
        return -1


if __name__ == "__main__":
    solution = Solution()
    source = ""
    target = ""
    ans = solution.strStr(source, target)
    print ans
    print "over"