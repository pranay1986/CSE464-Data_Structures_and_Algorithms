"""CSE464 | B Tree.
Algorithm: Implement minimum-degree B-tree insertion with splitting and search.
Logic: Minimum degree t means max 2t-1 keys; duplicates ignored.
"""

class Node:
    def __init__(self,leaf=True):self.keys=[];self.child=[];self.leaf=leaf
class BTree:
    def __init__(self,t=2):
        if t<2:raise ValueError('t>=2')
        self.t=t;self.root=Node()
    def search(self,k,node=None):
        n=node or self.root;i=0
        while i<len(n.keys) and k>n.keys[i]:i+=1
        if i<len(n.keys) and n.keys[i]==k:return True
        return False if n.leaf else self.search(k,n.child[i])
    def split(self,p,i):
        t=self.t;y=p.child[i];z=Node(y.leaf);median=y.keys[t-1]
        z.keys=y.keys[t:];y.keys=y.keys[:t-1]
        if not y.leaf:z.child=y.child[t:];y.child=y.child[:t]
        p.keys.insert(i,median);p.child.insert(i+1,z)
    def nonfull(self,n,k):
        i=len(n.keys)-1
        if n.leaf:
            n.keys.append(k)
            while i>=0 and k<n.keys[i]:n.keys[i+1]=n.keys[i];i-=1
            n.keys[i+1]=k
        else:
            while i>=0 and k<n.keys[i]:i-=1
            i+=1
            if len(n.child[i].keys)==2*self.t-1:
                self.split(n,i)
                if k>n.keys[i]:i+=1
            self.nonfull(n.child[i],k)
    def insert(self,k):
        if self.search(k):return
        r=self.root
        if len(r.keys)==2*self.t-1:
            s=Node(False);s.child=[r];self.root=s;self.split(s,0);self.nonfull(s,k)
        else:self.nonfull(r,k)
    def traverse(self,n=None):
        n=n or self.root;out=[]
        for i,k in enumerate(n.keys):
            if not n.leaf:out+=self.traverse(n.child[i])
            out.append(k)
        if not n.leaf:out+=self.traverse(n.child[-1])
        return out

if __name__ == "__main__":
    b=BTree(2)
    for x in (10,20,5,6,12,30,7,17):b.insert(x)
    print(b.traverse(),b.search(12))
