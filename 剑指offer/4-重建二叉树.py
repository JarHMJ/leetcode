# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre and not tin:
            return None

        root = TreeNode(pre[0])
        if set(pre) != set(tin):
            return None
        i = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:i+1],tin[0:i])
        root.right = self.reConstructBinaryTree(pre[i+1:],tin[i+1:])
        return root

if __name__ == '__main__':
    test = Solution()
    print(test.reConstructBinaryTree([1,2,3,4,5,6,7],[3,2,4,1,6,5,7]))