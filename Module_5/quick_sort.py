"""CSE464 | Quick Sort.
Algorithm: Sort using quick sort.
Logic: Work on a copy; return ascending sequence.
"""

def sort(a):
    a=a[:]
    def rec(lo,hi):
        if lo>=hi:return
        pivot=a[hi];i=lo
        for j in range(lo,hi):
            if a[j]<=pivot:a[i],a[j]=a[j],a[i];i+=1
        a[i],a[hi]=a[hi],a[i];rec(lo,i-1);rec(i+1,hi)
    rec(0,len(a)-1);return a

if __name__ == "__main__":
    print(sort([5,1,4,2,3]))
