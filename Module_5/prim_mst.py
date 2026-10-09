"""CSE464 | Prim Mst.
Algorithm: Grow MST from vertex 0 via cheapest crossing edge.
Logic: Heap-based adjacency list, nonnegative or negative weights allowed.
"""

import heapq
def mst(n,edges):
    if n==0:return 0,[]
    adj=[[] for _ in range(n)]
    for w,u,v in edges:adj[u].append((w,v));adj[v].append((w,u))
    seen=set();heap=[(0,0,-1)];total=0;chosen=[]
    while heap:
        w,u,p=heapq.heappop(heap)
        if u in seen:continue
        seen.add(u);total+=w
        if p!=-1:chosen.append((p,u,w))
        for nw,v in adj[u]:
            if v not in seen:heapq.heappush(heap,(nw,v,u))
    if len(seen)!=n:raise ValueError('disconnected graph')
    return total,chosen

if __name__ == "__main__":
    print(mst(4,[(1,0,1),(4,0,2),(2,1,2),(5,1,3),(3,2,3)])[0])
