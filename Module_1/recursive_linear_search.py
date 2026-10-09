"""CSE464 | Recursive Linear Search.
Algorithm: Recursively inspect one item per call.
Logic: Advance the index; stop when found or exhausted.
"""

def search(a,key,i=0):
    if i==len(a):return -1
    if a[i]==key:return i
    return search(a,key,i+1)

if __name__ == "__main__":
    print(search([8,3,19,14,6,22],14))
