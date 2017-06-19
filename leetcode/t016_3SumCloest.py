# --*-- coding:utf-8 --*--
# leetcode_016:https://leetcode.com/problems/3sum-closest/#/description
# lintcode_059:http://www.lintcode.com/zh-cn/problem/3sum-closest/


class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        tsum = 0
        length = len(nums)
        for i in range(length):
            left = i + 1
            right = length - 1
            while left < right:
                tsum = nums[i] + nums[left] + nums[right]
                if abs(tsum - target) < abs(ans -target):
                    ans = tsum
                if tsum <= target:
                    left += 1
                else:
                    right -= 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    list = [-1, 2, 1, -4]
    target = 1
    ans = solution.threeSumClosest(list, target)
    print ans
    print "over"