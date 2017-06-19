# --*-- coding:utf-8 --*--
# leetcode_015:https://leetcode.com/problems/3sum/#/description
# lintcode_57:http://www.lintcode.com/zh-cn/problem/3sum/


class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        ans = []  # 结果
        for i in range(0, len(nums) - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            target = -1 * nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:  # 避免结果重复
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                    # while left < right and nums[left] == nums[left+1]:
                    #     left += 1
                else:
                    right -= 1
                    # while left < right and nums[right] == nums[right-1]:
                    #     right -= 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    list = [-2,0,1,1,2]
    # print list
    ans = solution.threeSum(list)
    print ans
    print "over"