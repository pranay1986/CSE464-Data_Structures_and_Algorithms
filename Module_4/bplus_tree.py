"""CSE464 | Bplus Tree.
Algorithm: Insert keys into linked leaves and split up to the root.
Logic: Max_keys keys/leaf, internal separators equal first keys of right subtrees; no duplicates.
"""

class Node:
    def __init__(self,leaf=False):self.leaf=leaf;self.keys=[];self.children=[];self.next=None
class BPlusTree:
    def __init__(self,max_keys=3):
        if max_keys<2:raise ValueError('max_keys>=2')
        self.max_keys=max_keys;self.root=Node(True)
    def _leaf(self,key):
        n=self.root
        while not n.leaf:
            i=0
            while i<len(n.keys) and key>=n.keys[i]:i+=1
            n=n.children[i]
        return n
    def search(self,key):return key in self._leaf(key).keys
    def _insert(self,n,key):
        if n.leaf:
            i=0
            while i<len(n.keys) and n.keys[i]<key:i+=1
            n.keys.insert(i,key)
            if len(n.keys)<=self.max_keys:return None
            mid=(len(n.keys)+1)//2;right=Node(True);right.keys=n.keys[mid:];n.keys=n.keys[:mid];right.next=n.next;n.next=right
            return right.keys[0],right
        i=0
        while i<len(n.keys) and key>=n.keys[i]:i+=1
        split=self._insert(n.children[i],key)
        if split is None:return None
        sep,right=split;n.keys.insert(i,sep);n.children.insert(i+1,right)
        if len(n.keys)<=self.max_keys:return None
        mid=len(n.keys)//2;promote=n.keys[mid];new=Node();new.keys=n.keys[mid+1:];new.children=n.children[mid+1:];n.keys=n.keys[:mid];n.children=n.children[:mid+1]
        return promote,new
    def insert(self,key):
        if self.search(key):return
        split=self._insert(self.root,key)
        if split:
            sep,right=split;r=Node();r.keys=[sep];r.children=[self.root,right];self.root=r
    def range_search(self,lo,hi):
        if lo>hi:return []
        n=self._leaf(lo);res=[]
        while n:
            for x in n.keys:
                if x>hi:return res
                if x>=lo:res.append(x)
            n=n.next
        return res

if __name__ == "__main__":
    t=BPlusTree()
    for x in (10,20,5,6,12,30,7,17):t.insert(x)
    print(t.range_search(6,20),t.search(12))
