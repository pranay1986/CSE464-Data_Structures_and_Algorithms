"""CSE464 | Heap Sort.
Algorithm: Sort using heap sort.
Logic: Work on a copy; return ascending sequence.
"""

def sort(a):
    a=a[:];n=len(a)
    def heapify(i,size):
        while True:
            big=i;l=2*i+1;r=l+1
            if l<size and a[l]>a[big]:big=l
            if r<size and a[r]>a[big]:big=r
            if big==i:return
            a[i],a[big]=a[big],a[i];i=big
    for i in range(n//2-1,-1,-1):heapify(i,n)
    for end in range(n-1,0,-1):a[0],a[end]=a[end],a[0];heapify(0,end)
    return a

if __name__ == "__main__":
    print(sort([5,1,4,2,3]))
