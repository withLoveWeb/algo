# Definition for a binary tree node.
from typing import List, Optional
import sys

# Установка максимального числа вызова рекурсии
# sys.setrecursionlimit(40)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def print_tree(node, level=0, prefix="Root: "):
            if node is not None:
                print(" " * (level * 4) + prefix + str(node.val))
                if node.left is not None or node.right is not None:
                    if node.left:
                        print_tree(node.left, level + 1, "L--- ")
                    else:
                        print(" " * ((level + 1) * 4) + "L--- None")
                    if node.right:
                        print_tree(node.right, level + 1, "R--- ")
                    else:
                        print(" " * ((level + 1) * 4) + "R--- None")
        def recursia(arr):
            if not arr:
                return None
            tree = TreeNode()
            tree.val = arr[len(arr)//2]
            left = arr[:len(arr)//2]
            right = arr[len(arr)//2+1:]
            if left:
                print(f"left {left}")
                tree.left = recursia(left)
            if right:
                print(f"right {right}")
                tree.right = recursia(right)
            if not left and not right:
                print( f"return {arr[len(arr)//2]}")
                return tree
            print(f"tree {tree.val}")
            return tree
        tree = recursia(nums)
        print_tree(tree)



nums = [0]
nums = [-12, -11, -10,-3,0,5,9, 10, 11]

s = Solution()
s.sortedArrayToBST(nums)