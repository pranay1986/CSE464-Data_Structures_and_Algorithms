"""CSE464 | Binary Tree Level Order.
Algorithm: Use FIFO queue for breadth-first tree traversal.
Logic: Append children in left-to-right order.
"""

from collections import deque
class Node:
    def __init__(self,x,left=None,right=None):self.x=x;self.left=left;self.right=right
def levels(root):
    if not root:return []
    q=deque([root]);result=[]
    while q:
        node=q.popleft();result.append(node.x)
        if node.left:q.append(node.left)
        if node.right:q.append(node.right)
    return result

if __name__ == "__main__":
    print(levels(Node(1,Node(2),Node(3))))
