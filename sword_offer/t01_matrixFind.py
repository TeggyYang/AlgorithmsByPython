# --*-- coding:utf-8 --*--

"""
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
测试用例：(1)二维数组中包含查找的数字（最大值，最小值，最大和最小之间）
(2)二维数组中没有查找的数字(大于最大值，小于最小值，最大和最小之间但不存在)
(3)特殊输入测试
"""


class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if array is None or len(array) == 0:
            return False
        rowNum = len(array)
        colNum = len(array[0])
        row = 0
        col = colNum - 1
        while row < rowNum and col >= 0:
            if array[row][col] > target:
                col -= 1
            elif array[row][col] < target:
                row += 1
            else:
                return True
        return False


if __name__ == '__main__':
    solution = Solution()
    array = [[1, 2, 8, 9],
             [2, 4, 9, 12],
             [4, 7, 10, 13],
             [6, 8, 11, 15]]
    target = 14
    array1 = []
    target1 = 0
    print solution.Find(target, array)
    print solution.Find(target1, array1)
    print "over"