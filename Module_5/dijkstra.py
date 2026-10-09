"""CSE464 | Dijkstra.
Algorithm: Relax outgoing edges using a min-priority heap.
Logic: Reject negative weights; return distances and parents.
"""

import heapq
def dijkstra(n,edges,start):
    adj=[[] for _ in range(n)]
    for u,v,w in edges:
        if w<0:raise ValueError('negative weight not supported')
        adj[u].append((v,w))
    dist=[float('inf')]*n;parent=[None]*n;dist[start]=0;pq=[(0,start)]
    while pq:
        d,u=heapq.heappop(pq)
        if d!=dist[u]:continue
        for v,w in adj[u]:
            if d+w<dist[v]:dist[v]=d+w;parent[v]=u;heapq.heappush(pq,(dist[v],v))
    return dist,parent

if __name__ == "__main__":
    print(dijkstra(4,[(0,1,1),(0,2,4),(1,2,2),(2,3,3)],0)[0])
