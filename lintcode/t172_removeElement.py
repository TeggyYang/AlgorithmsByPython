# --*-- coding:utf-8 --*--
# leetcode_027:https://leetcode.com/problems/remove-element/#/description
# lintcode_172:http://www.lintcode.com/zh-cn/problem/remove-element/


class Solution(object):
    def removeElement(self, nums, val):
        ans = 0
        for i in range(0, len(nums)):
            if nums[i] == val:
                continue
            nums[ans] = nums[i]
            ans += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    list = [0, 4, 4, 0, 0, 2, 4, 4, 4]
    val = 4
    ans = solution.removeElement(list, val)
    print ans
    print "over"