"""CSE464 | Dfs.
Algorithm: DFS graph traversal using recursion.
Logic: Mark before traversing neighbors.
"""

def dfs(graph,start):
    seen=set();order=[]
    def visit(u):
        seen.add(u);order.append(u)
        for v in graph[u]:
            if v not in seen:visit(v)
    visit(start);return order

if __name__ == "__main__":
    print(dfs([[1,2],[0,3],[0],[1]],0))
