# --*-- coding:utf-8 --*--
# leetcode_011:https://leetcode.com/problems/container-with-most-water/#/description
# lintcode_383:http://www.lintcode.com/zh-cn/problem/container-with-most-water/


class Solution(object):
    def maxArea(self, height):
        ans = 0
        area = 0
        i = 0
        j = len(height)-1
        while i < j:
            if height[i] < height[j]:
                area = height[i] * (j - i)
                i += 1
            else:
                area = height[j] * (j - i)
                j -= 1
            ans = max(area, ans)
        return ans

if __name__ == "__main__":
    solution = Solution()
    list = []
    list.append(1)
    list.append(2)
    list.append(3)
    print list
    ans = solution.maxArea(list)
    print ans
    print "over"