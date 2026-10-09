"""CSE464 | First Occurrence.
Algorithm: Modified binary search continues left after a match.
Logic: Record the candidate index.
"""

def first(a,x):
    lo,hi,ans=0,len(a)-1,-1
    while lo<=hi:
        mid=(lo+hi)//2
        if a[mid]>=x:
            if a[mid]==x:ans=mid
            hi=mid-1
        else:lo=mid+1
    return ans

if __name__ == "__main__":
    print(first([2,4,4,4,7,9,12],4))
