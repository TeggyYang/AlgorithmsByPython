# --*-- coding:utf-8 --*--
"""
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""

"""
字符串转数组
str = '1,2,3'
arr = str.split(',')

数组转字符串
arr = ['a','b']
str = ','.join(arr)

arr = [1,2,3]
str = ','.join(str(i) for i in b)
"""


class Solution:
    # s 源字符串
    def replaceSpace1(self, s):
        # write code here
        if type(s) != str:
            return
        return s.replace(" ", "%20")

    def replaceSpace2(self, s):
        temp = ""
        if type(s) != str:
            return
        for t in s:
            if t == " ":
                temp += "%20"
            else:
                temp += t
        return temp

    def replaceSpace3(self, s):
        if not isinstance(s, str) or len(s) <= 0 or s is None:
            return
        spaceNum = 0
        for i in s:
            if i == " ":
                spaceNum += 1
        newStrLen = len(s) + spaceNum * 2
        newStr = newStrLen * [None]
        indexOfOriginal = len(s) - 1
        indexOfNew = newStrLen - 1
        while indexOfNew >= 0:
            if s[indexOfOriginal] != " ":
                newStr[indexOfNew] = s[indexOfOriginal]
                indexOfNew -= 1
                indexOfOriginal -= 1
            else:
                indexOfOriginal -= 1
                newStr[indexOfNew] = "0"
                newStr[indexOfNew-1] = "2"
                newStr[indexOfNew-2] = "%"
                indexOfNew -= 3
        return "".join(newStr)


if __name__ == '__main__':
    solution = Solution()
    s = "We Are Happy"
    print solution.replaceSpace1(s)
    print solution.replaceSpace2(s)
    print solution.replaceSpace3(s)