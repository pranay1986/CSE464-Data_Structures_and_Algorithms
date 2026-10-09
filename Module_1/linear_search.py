"""CSE464 | Linear Search.
Algorithm: Inspect elements from left to right until the first match.
Logic: Return index or -1, counting probes.
"""

def linear_search(a,key):
    for i,v in enumerate(a):
        if v==key:return i
    return -1

if __name__ == "__main__":
    print(linear_search([8,3,19,14,6,22],14))
