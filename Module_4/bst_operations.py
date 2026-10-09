"""CSE464 | Bst Operations.
Algorithm: Maintain left smaller, right larger; delete using inorder successor.
Logic: Duplicates ignored.
"""

class Node:
    def __init__(self,x):self.x=x;self.left=self.right=None
def insert(root,x):
    if not root:return Node(x)
    if x<root.x:root.left=insert(root.left,x)
    elif x>root.x:root.right=insert(root.right,x)
    return root
def search(root,x):
    while root:
        if x==root.x:return True
        root=root.left if x<root.x else root.right
    return False
def delete(root,x):
    if not root:return None
    if x<root.x:root.left=delete(root.left,x)
    elif x>root.x:root.right=delete(root.right,x)
    else:
        if not root.left:return root.right
        if not root.right:return root.left
        p=root.right
        while p.left:p=p.left
        root.x=p.x;root.right=delete(root.right,p.x)
    return root
def inorder(root):return inorder(root.left)+[root.x]+inorder(root.right) if root else []

if __name__ == "__main__":
    t=None
    for x in (5,3,7,2,4,6,8):t=insert(t,x)
    t=delete(t,5);print(inorder(t),search(t,6))
