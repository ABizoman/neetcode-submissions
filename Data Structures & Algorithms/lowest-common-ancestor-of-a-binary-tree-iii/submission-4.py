"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        p_anc = []
        def construct_up(node):
            while node:
                p_anc.append(node.val)
                node = node.parent

        construct_up(p)
        while q != None:
            if q.val in p_anc:
                return q
            else: q = q.parent
            
        