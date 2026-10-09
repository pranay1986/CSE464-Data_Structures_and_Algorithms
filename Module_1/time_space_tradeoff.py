"""CSE464 | Time Space Tradeoff.
Algorithm: Compare direct repeated computation with a precomputed lookup table.
Logic: Cache squares in O(n) extra memory.
"""

def uncached(queries):return [x*x for x in queries]
def cached(queries):
    table={x:x*x for x in set(queries)}
    return [table[x] for x in queries]

if __name__ == "__main__":
    q=[3,5,3,5];print(uncached(q)==cached(q),cached(q))
