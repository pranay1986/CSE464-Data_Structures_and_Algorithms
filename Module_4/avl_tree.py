"""CSE464 | Avl Tree.
Algorithm: BST insert with height maintenance and LL/RR/LR/RL rotations.
Logic: Rebalance whenever absolute balance factor exceeds one.
"""

class Node:
    def __init__(self,x):self.x=x;self.left=self.right=None;self.h=1
def h(n):return n.h if n else 0
def update(n):n.h=1+max(h(n.left),h(n.right))
def right(y):
    x=y.left;y.left=x.right;x.right=y;update(y);update(x);return x
def left(x):
    y=x.right;x.right=y.left;y.left=x;update(x);update(y);return y
def insert(n,x):
    if not n:return Node(x)
    if x<n.x:n.left=insert(n.left,x)
    elif x>n.x:n.right=insert(n.right,x)
    else:return n
    update(n);b=h(n.left)-h(n.right)
    if b>1:
        if x>n.left.x:n.left=left(n.left)
        return right(n)
    if b<-1:
        if x<n.right.x:n.right=right(n.right)
        return left(n)
    return n
def inorder(n):return inorder(n.left)+[n.x]+inorder(n.right) if n else []

if __name__ == "__main__":
    r=None
    for v in (30,20,10,25,40,35):r=insert(r,v)
    print(r.x,inorder(r))
