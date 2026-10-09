"""CSE464 | Binary Tree Traversals.
Algorithm: Visit root recursively in pre/in/post order.
Logic: Use standard node objects.
"""

class Node:
    def __init__(self,x,left=None,right=None):self.x=x;self.left=left;self.right=right
def preorder(t):return [] if not t else [t.x]+preorder(t.left)+preorder(t.right)
def inorder(t):return [] if not t else inorder(t.left)+[t.x]+inorder(t.right)
def postorder(t):return [] if not t else postorder(t.left)+postorder(t.right)+[t.x]

if __name__ == "__main__":
    t=Node(2,Node(1),Node(3));print(preorder(t),inorder(t),postorder(t))
