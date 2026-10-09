"""CSE464 | Bfs.
Algorithm: FIFO graph traversal with visited-on-enqueue.
Logic: Vertices 0..n-1 in adjacency lists.
"""

from collections import deque
def bfs(graph,start):
    seen={start};q=deque([start]);order=[]
    while q:
        u=q.popleft();order.append(u)
        for v in graph[u]:
            if v not in seen:seen.add(v);q.append(v)
    return order

if __name__ == "__main__":
    print(bfs([[1,2],[0,3],[0],[1]],0))
