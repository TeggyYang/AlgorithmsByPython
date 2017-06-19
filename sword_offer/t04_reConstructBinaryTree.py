# --*-- coding:utf-8 --*--
"""
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre and not tin:
            return None
        if set(pre) != set(tin):
            return None
        root = TreeNode(pre[0])  # 根节点
        i = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1: 1+i], tin[:i])
        root.right = self.reConstructBinaryTree(pre[i+1:], tin[i+1:])
        return root

    def pre_order(self, tree):
        if tree is None:
            return None
        print tree.val,
        self.pre_order(tree.left)
        self.pre_order(tree.right)

if __name__ == "__main__":
    pre = [10, 6, 4, 8, 14, 12, 16]
    tin = [4, 6, 8, 10, 12, 14, 16]
    # pre = [1, 2, 4, 7, 3, 5, 6, 8]
    # tin = [4, 7, 2, 1, 5, 3, 8, 6]
    solution = Solution()
    newTree = solution.reConstructBinaryTree(pre, tin)
    print solution.pre_order(newTree)
    print "over"



