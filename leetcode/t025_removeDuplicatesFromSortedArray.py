# --*-- coding:utf-8 --*--
# leetcode_025:https://leetcode.com/problems/remove-duplicates-from-sorted-array/#/description
# lintcode_100:http://www.lintcode.com/zh-cn/problem/remove-duplicates-from-sorted-array/


class Solution(object):
    def removeDuplicates(self, nums):
        length = 0
        for i in range(0, len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            else:
                nums[length] = nums[i]
                length += 1
        return length


if __name__ == "__main__":
    solution = Solution()
    list = [1, 1, 2, 4, 4, 4, 4, 5]
    ans = solution.removeDuplicates(list)
    print ans
    print "over"