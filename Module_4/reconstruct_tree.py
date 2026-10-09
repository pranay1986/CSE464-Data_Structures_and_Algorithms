"""CSE464 | Reconstruct Tree.
Algorithm: Build tree from preorder and inorder of distinct values.
Logic: Track inorder indices and consume preorder.
"""

class Node:
    def __init__(self,x):self.x=x;self.left=self.right=None
def build(preorder,inorder):
    if len(preorder)!=len(inorder) or len(set(inorder))!=len(inorder) or set(preorder)!=set(inorder):raise ValueError('distinct matching keys required')
    index={v:i for i,v in enumerate(inorder)};it=iter(preorder)
    def rec(lo,hi):
        if lo>hi:return None
        v=next(it);mid=index[v]
        if not lo<=mid<=hi:raise ValueError('inconsistent traversals')
        n=Node(v);n.left=rec(lo,mid-1);n.right=rec(mid+1,hi);return n
    return rec(0,len(inorder)-1)
def postorder(t):return postorder(t.left)+postorder(t.right)+[t.x] if t else []

if __name__ == "__main__":
    t=build([2,1,3],[1,2,3]);print(postorder(t))
