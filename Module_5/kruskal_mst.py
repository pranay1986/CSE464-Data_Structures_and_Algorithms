"""CSE464 | Kruskal Mst.
Algorithm: Sort edges and accept those joining disjoint components.
Logic: Union-find with path compression/rank; reject disconnected graphs.
"""

def mst(n,edges):
    parent=list(range(n));rank=[0]*n
    def find(x):
        while x!=parent[x]:parent[x]=parent[parent[x]];x=parent[x]
        return x
    result=[];total=0
    for w,u,v in sorted(edges):
        a,b=find(u),find(v)
        if a==b:continue
        if rank[a]<rank[b]:a,b=b,a
        parent[b]=a
        if rank[a]==rank[b]:rank[a]+=1
        result.append((u,v,w));total+=w
        if len(result)==n-1:break
    if len(result)!=n-1:raise ValueError('disconnected graph')
    return total,result

if __name__ == "__main__":
    print(mst(4,[(1,0,1),(4,0,2),(2,1,2),(5,1,3),(3,2,3)])[0])
