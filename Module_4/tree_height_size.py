"""CSE464 | Tree Height Size.
Algorithm: Recursively count nodes and maximal edge-depth.
Logic: Empty height -1, singleton height 0.
"""

class Node:
    def __init__(self,x,l=None,r=None):self.x=x;self.left=l;self.right=r
def size(t):return 0 if t is None else 1+size(t.left)+size(t.right)
def height(t):return -1 if t is None else 1+max(height(t.left),height(t.right))

if __name__ == "__main__":
    t=Node(1,Node(2,Node(4)),Node(3));print(size(t),height(t))
