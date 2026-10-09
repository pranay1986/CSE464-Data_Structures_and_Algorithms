"""CSE464 | Recursive Binary Search.
Algorithm: Recursively halve sorted range.
Logic: Avoid slicing so only logarithmic call frames are used.
"""

def search(a,x,lo=0,hi=None):
    if hi is None:hi=len(a)-1
    if lo>hi:return -1
    mid=(lo+hi)//2
    if a[mid]==x:return mid
    if a[mid]<x:return search(a,x,mid+1,hi)
    return search(a,x,lo,mid-1)

if __name__ == "__main__":
    print(search([2,5,8,11,19,24],19))
