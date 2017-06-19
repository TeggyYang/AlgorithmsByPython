# --*-- coding:utf-8 --*--
# leetcode_001:https://leetcode.com/problems/two-sum/#/description
# lintcode_56:http://www.lintcode.com/zh-cn/problem/two-sum/
# 字典的使用


class Solution(object):
    def twoSum(self, nums, target):
        hash = {}  # 数值到下标的映射
        for i in range(len(nums)):
            # print i
            if target - nums[i] in hash:
                return [hash[target - nums[i]], i]
            hash[nums[i]] = i

        return [-1, -1]

if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    ans = solution.twoSum(nums, target)
    print ans
    print "over"