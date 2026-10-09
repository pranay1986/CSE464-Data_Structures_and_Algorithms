"""CSE464 | Binary Search.
Algorithm: Halve a sorted search interval until matching or empty.
Logic: Maintain inclusive low/high boundaries.
"""

def binary_search(a,key):
    lo,hi=0,len(a)-1
    while lo<=hi:
        mid=(lo+hi)//2
        if a[mid]==key:return mid
        if a[mid]<key:lo=mid+1
        else:hi=mid-1
    return -1

if __name__ == "__main__":
    print(binary_search([5,9,13,20,27,31,38,42,50,61],42))
