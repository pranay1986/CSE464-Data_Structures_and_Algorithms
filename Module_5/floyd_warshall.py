"""CSE464 | Floyd Warshall.
Algorithm: All-pairs shortest paths using every vertex as intermediary.
Logic: Detect negative cycles via diagonal.
"""

def floyd(n,edges):
    d=[[0 if i==j else float('inf') for j in range(n)] for i in range(n)]
    for u,v,w in edges:d[u][v]=min(d[u][v],w)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k]+d[k][j]<d[i][j]:d[i][j]=d[i][k]+d[k][j]
    if any(d[i][i]<0 for i in range(n)):raise ValueError('negative cycle')
    return d

if __name__ == "__main__":
    print(floyd(3,[(0,1,2),(1,2,3)])[0])
