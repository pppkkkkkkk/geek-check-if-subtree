'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should print the left view of the binary tree
# Note: You aren't required to print a new line after every test case


class Solution:
    def isSubTree(self, T, S):
        # Code here
        def sameTree(A, B):
            if not A and not B:
                return True
            if (not A or not B) or A.data != B.data:
                return False
            return sameTree(A.left, B.left) and sameTree(A.right,B.right)
            
        def isSub(A, B):
            if not B:
                return True
            if not A: 
                return False
            if sameTree(A,B):
                return True
            return (isSub(A.left, B) or isSub(A.right, B))
        
        if isSub(T,S):
            return True
        return False
        
