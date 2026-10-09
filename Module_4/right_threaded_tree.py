"""CSE464 | Right Threaded Tree.
Algorithm: Thread null right links to inorder successor.
Logic: Build a static threaded representation from BST and traverse without stack.
"""

class Node:
    def __init__(self,x):self.x=x;self.left=self.right=None;self.thread=False
def insert(root,x):
    if not root:return Node(x)
    p=root
    while True:
        if x<p.x:
            if p.left:p=p.left
            else:p.left=Node(x);return root
        else:
            if p.right:p=p.right
            else:p.right=Node(x);return root
def thread_tree(root):
    prev=[None]
    def walk(n):
        if not n:return
        walk(n.left)
        if prev[0] and prev[0].right is None:prev[0].right=n;prev[0].thread=True
        prev[0]=n;walk(n.right)
    walk(root)
def traverse(root):
    def leftmost(n):
        while n and n.left:n=n.left
        return n
    p=leftmost(root);out=[]
    while p:
        out.append(p.x)
        p=p.right if p.thread else leftmost(p.right)
    return out

if __name__ == "__main__":
    r=None
    for v in (4,2,6,1,3,5,7):r=insert(r,v)
    thread_tree(r);print(traverse(r))
