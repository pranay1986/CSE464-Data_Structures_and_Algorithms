"""CSE464 | Graph Representations.
Algorithm: Represent graph as adjacency list and 0/1 matrix.
Logic: Undirected graph with vertices 0..n-1.
"""

def represent(n,edges):
    adj=[[] for _ in range(n)];mat=[[0]*n for _ in range(n)]
    for u,v in edges:
        adj[u].append(v);adj[v].append(u);mat[u][v]=mat[v][u]=1
    for row in adj:row.sort()
    return adj,mat

if __name__ == "__main__":
    print(represent(3,[(0,1),(1,2)]))
