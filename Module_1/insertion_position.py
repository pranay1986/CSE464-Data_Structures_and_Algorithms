"""CSE464 | Insertion Position.
Algorithm: Lower-bound binary search.
Logic: Return the first index whose value is not smaller than target.
"""

def insertion_index(a,x):
    lo,hi=0,len(a)
    while lo<hi:
        mid=(lo+hi)//2
        if a[mid]<x:lo=mid+1
        else:hi=mid
    return lo

if __name__ == "__main__":
    print([insertion_index([3,8,12,20,31],x) for x in (12,15,40)])
