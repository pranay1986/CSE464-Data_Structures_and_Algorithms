"""CSE464 | Count Occurrences.
Algorithm: Compute lower/upper bounds to count duplicates.
Logic: Two logarithmic binary searches.
"""

def bound(a,x,strict):
    lo,hi=0,len(a)
    while lo<hi:
        mid=(lo+hi)//2
        if a[mid]<x or (strict and a[mid]==x):lo=mid+1
        else:hi=mid
    return lo

def count(a,x):return bound(a,x,True)-bound(a,x,False)

if __name__ == "__main__":
    print(count([1,2,2,2,2,5,7,7,9],2))
