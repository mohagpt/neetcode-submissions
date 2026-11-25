"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        copies = {node: Node(node.val)}   # original -> copy; also the visited set
        stack = [node]
        while stack:
            current = stack.pop()
            for nxt in current.neighbors:
                if nxt not in copies:
                    copies[nxt] = Node(nxt.val)
                    stack.append(nxt)
                copies[current].neighbors.append(copies[nxt])
        return copies[node]